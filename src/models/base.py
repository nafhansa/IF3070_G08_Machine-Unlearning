# Class dasar yang dipakai oleh semua model

import pickle
from pathlib import Path


class BaseModel:
    def fit(self, X, y):
        raise NotImplementedError("Model harus punya fungsi fit")

    def predict(self, X):
        raise NotImplementedError("Model harus punya fungsi predict")

    def save(self, path):
        # Pickle menyimpan seluruh isi model, termasuk hasil training
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "wb") as file:
            pickle.dump(self, file)

        return path

    @classmethod
    def load(cls, path):
        # Hanya buka file model yang dibuat 
        with open(path, "rb") as file:
            model = pickle.load(file)

        if not isinstance(model, cls):
            raise TypeError("Tipe model di file tidak sesuai")

        return model

    def get_params(self):
        params = {}
        for name, value in self.__dict__.items():
            # Hasil training punya nama berakhiran _, misalnya classes_
            if not name.startswith("_") and not name.endswith("_"):
                params[name] = value
        return params

    def __repr__(self):
        parts = []
        for name, value in self.get_params().items():
            parts.append(f"{name}={value!r}")
        return f"{type(self).__name__}({', '.join(parts)})"
