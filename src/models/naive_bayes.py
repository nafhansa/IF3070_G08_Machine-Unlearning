# Acuan utama: Materi09, halaman 16-22.
# Tambahan Gaussian dan smoothing:
# T. Mitchell, Machine Learning, 1997, Bab 6.
# https://scikit-learn.org/stable/modules/naive_bayes.html

import numpy as np

from .base import BaseModel


def _missing_mask(column):
    # True berarti nilai pada posisi tersebut kosong.
    missing = []

    for value in column:
        kosong = value is None

        if isinstance(value, (float, np.floating)):
            kosong = kosong or np.isnan(value)

        missing.append(kosong)

    return np.array(missing, dtype=bool)


class NaiveBayes(BaseModel):
    def __init__(
        self,
        categorical_features="auto",
        max_categories=15,
        alpha=1.0,
        var_smoothing=1e-9,
    ):
        self.categorical_features = categorical_features
        self.max_categories = max_categories
        self.alpha = alpha
        self.var_smoothing = var_smoothing

    def _to_columns(self, X):
        # Bisa menerima DataFrame tanpa mengimpor pandas.
        if hasattr(X, "columns"):
            names = list(X.columns)
            columns = []

            for name in names:
                columns.append(X[name].to_numpy())

            return columns, names, True

        X = np.asarray(X)

        if X.ndim != 2:
            raise ValueError("X harus berupa tabel dua dimensi")

        columns = []
        for j in range(X.shape[1]):
            columns.append(X[:, j])

        return columns, list(range(X.shape[1])), False

    def _decide_categorical(self, columns):
        mode = self.categorical_features

        if isinstance(mode, str):
            if mode == "all":
                return [True] * len(columns)

            if mode != "auto":
                raise ValueError(
                    "categorical_features harus 'auto', 'all', "
                    "atau daftar indeks kolom"
                )

            flags = []

            for column in columns:
                known = column[~_missing_mask(column)]
                numeric = column.dtype.kind in "fiub"

                if numeric:
                    categorical = (
                        len(np.unique(known)) <= self.max_categories
                    )
                else:
                    categorical = True

                flags.append(categorical)

            return flags

        indices = list(mode)

        for index in indices:
            if not isinstance(index, (int, np.integer)):
                raise ValueError("Indeks kolom harus berupa integer")

            if index < 0 or index >= len(columns):
                raise ValueError("Indeks kolom kategorikal tidak tersedia")

        return [j in indices for j in range(len(columns))]

    def _category_values(self, column, numeric):
        if numeric:
            return column

        # Mengikuti baseline: kategori nonnumerik disimpan sebagai string.
        return column.astype(str)

    def fit(self, X, y):
        if not np.isfinite(self.alpha) or self.alpha < 0:
            raise ValueError("alpha harus bernilai nonnegatif")

        if not np.isfinite(self.var_smoothing) or self.var_smoothing <= 0:
            raise ValueError("var_smoothing harus lebih dari nol")

        if self.max_categories < 1:
            raise ValueError("max_categories minimal 1")

        columns, names, is_dataframe = self._to_columns(X)
        y = np.asarray(y)

        if len(columns) == 0:
            raise ValueError("X harus memiliki minimal satu fitur")

        if y.ndim != 1 or len(y) == 0:
            raise ValueError("y harus berupa array satu dimensi yang berisi")

        if len(columns[0]) != len(y):
            raise ValueError("Jumlah baris X dan y harus sama")

        if _missing_mask(y).any():
            raise ValueError("Label training tidak boleh kosong")

        self.feature_names_ = names
        self.dataframe_input_ = is_dataframe
        self.n_features_in_ = len(columns)
        self.classes_ = np.unique(y)
        self.is_categorical_ = self._decide_categorical(columns)

        # Prior kelas berasal dari proporsi label pada data training.
        priors = []
        for label in self.classes_:
            priors.append(np.mean(y == label))

        self.class_log_prior_ = np.log(priors)
        self.params_ = []

        # Besar penyesuaian varians dihitung hanya dari data training.
        max_variance = 0.0

        for j, column in enumerate(columns):
            if not self.is_categorical_[j]:
                known = column[~_missing_mask(column)].astype(float)

                if len(known) > 0:
                    if not np.isfinite(known).all():
                        raise ValueError("Fitur numerik mengandung infinity")

                    max_variance = max(
                        max_variance, float(np.var(known))
                    )

        # Batas kecil tetap diperlukan jika seluruh fitur kontinu konstan.
        epsilon = max(
            self.var_smoothing * max_variance,
            np.finfo(float).eps,
        )

        for j, column in enumerate(columns):
            known_mask = ~_missing_mask(column)

            # Tidak ada informasi yang bisa dipelajari dari kolom ini.
            if not known_mask.any():
                self.params_.append({"type": "skip"})
                continue

            if self.is_categorical_[j]:
                numeric = column.dtype.kind in "fiub"
                known_values = self._category_values(
                    column[known_mask], numeric
                )
                categories = np.unique(known_values)

                log_prob = np.zeros(
                    (len(self.classes_), len(categories))
                )

                for c, label in enumerate(self.classes_):
                    class_values = self._category_values(
                        column[known_mask & (y == label)], numeric
                    )

                    if len(class_values) == 0:
                        raise ValueError(
                            f"Fitur {names[j]} kosong pada kelas {label}"
                        )

                    denominator = (
                        len(class_values) + self.alpha * len(categories)
                    )

                    for k, value in enumerate(categories):
                        count = np.sum(class_values == value)
                        probability = (
                            count + self.alpha
                        ) / denominator

                        # alpha=0 tetap boleh, sesuai contoh pada slide.
                        if probability == 0:
                            log_prob[c, k] = -np.inf
                        else:
                            log_prob[c, k] = np.log(probability)

                self.params_.append({
                    "type": "cat",
                    "categories": categories,
                    "numeric": numeric,
                    "log_prob": log_prob,
                })

            else:
                numeric_column = column.astype(float)
                means = []
                variances = []

                for label in self.classes_:
                    values = numeric_column[
                        known_mask & (y == label)
                    ]

                    if len(values) == 0:
                        raise ValueError(
                            f"Fitur {names[j]} kosong pada kelas {label}"
                        )

                    means.append(np.mean(values))
                    variances.append(np.var(values) + epsilon)

                self.params_.append({
                    "type": "gauss",
                    "mean": np.array(means),
                    "var": np.array(variances),
                })

        return self

    def _joint_log_likelihood(self, X):
        if not hasattr(self, "params_"):
            raise ValueError("Model harus di-fit sebelum prediksi")

        columns, names, is_dataframe = self._to_columns(X)

        if len(columns) != self.n_features_in_:
            raise ValueError("Jumlah fitur berbeda dari data training")

        if self.dataframe_input_ and is_dataframe:
            if names != self.feature_names_:
                raise ValueError(
                    "Nama dan urutan kolom harus sama dengan training"
                )

        n_rows = len(columns[0])
        scores = np.tile(self.class_log_prior_, (n_rows, 1))

        for j, column in enumerate(columns):
            param = self.params_[j]

            if param["type"] == "skip":
                continue

            known_mask = ~_missing_mask(column)

            # Missing tidak memberi tambahan likelihood untuk baris itu.
            if param["type"] == "cat":
                values = self._category_values(
                    column[known_mask], param["numeric"]
                )
                categories = param["categories"]

                if not np.isin(values, categories).all():
                    raise ValueError(
                        f"Fitur {self.feature_names_[j]} "
                        "memiliki kategori baru yang tidak dikenal"
                    )

                known_rows = np.where(known_mask)[0]

                for k, value in enumerate(categories):
                    rows = known_rows[values == value]
                    scores[rows] += param["log_prob"][:, k]

            else:
                values = column[known_mask].astype(float)

                if not np.isfinite(values).all():
                    raise ValueError("Fitur numerik mengandung infinity")

                for c in range(len(self.classes_)):
                    mean = param["mean"][c]
                    variance = param["var"][c]

                    # Log dari rumus probability density Gaussian.
                    log_prob = -0.5 * np.log(
                        2 * np.pi * variance
                    )
                    log_prob = log_prob - (
                        (values - mean) ** 2 / (2 * variance)
                    )

                    scores[known_mask, c] += log_prob

        if np.isnan(scores).any() or np.isposinf(scores).any():
            raise ValueError("Perhitungan menghasilkan skor tidak valid")

        if np.isneginf(scores).all(axis=1).any():
            raise ValueError(
                "Semua kelas memiliki likelihood nol. "
                "Periksa data atau gunakan alpha lebih dari nol."
            )

        return scores

    def predict_proba(self, X):
        scores = self._joint_log_likelihood(X)

        # Kurangi skor terbesar agar exp tidak terlalu besar.
        max_score = np.max(scores, axis=1, keepdims=True)
        probabilities = np.exp(scores - max_score)

        total = np.sum(probabilities, axis=1, keepdims=True)
        return probabilities / total

    def predict(self, X):
        scores = self._joint_log_likelihood(X)
        best_class = np.argmax(scores, axis=1)

        return self.classes_[best_class]