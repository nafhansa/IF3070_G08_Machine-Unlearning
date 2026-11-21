"""Helper kecil untuk membangun notebook .ipynb dari daftar sel (dipakai tools/build_*.py)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "instruction" / "template_notebook_asisten.ipynb"


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n")}


def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text.strip("\n")}


def section(num, title):
    return md(f"---\n\n# {title} <a name=\"{num}\"></a>\n\n---")


def write_notebook(cells, path):
    meta = json.loads(TEMPLATE.read_text())["metadata"] if TEMPLATE.exists() else {}
    meta.pop("colab", None)
    meta["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb = {"cells": cells, "metadata": meta, "nbformat": 4, "nbformat_minor": 5}
    for i, c in enumerate(nb["cells"]):
        c["id"] = f"cell-{i:03d}"
    Path(path).write_text(json.dumps(nb, indent=1, ensure_ascii=False))
    print("ditulis:", path)


HEADER = """
---

# Tugas Besar 2 IF3070 Dasar Inteligensi Artifisial

*Notebook ini dibangun dari template resmi asisten. Struktur 11 section dipertahankan; sel dan sub-bagian ditambah sesuai kebutuhan.*
"""

GROUP = """
---

## Kelompok G08 - Machine Unlearning

| Nama | NIM |
|---|---|
| M. Faris Daffa | 18224025 |
| *(isi nama)* | 18224009 |
| *(isi nama)* | 18224016 |
| *(isi nama)* | 18224027 |
| *(isi nama)* | 18224096 |
"""

TOC = """
---

## Daftar Isi

1. [**Introduction**](#1)
2. [**Initialization**](#2)
3. [**Data Understanding**](#3)
4. [**Training and Validation Split**](#4)
5. [**Data Preparation**](#5)
6. [**Preparation Pipeline**](#6)
7. [**Modeling and Validation**](#7)
8. [**Comparison with scikit-learn**](#8)
9. [**Saving and Loading Models**](#9)
10. [**Kaggle Submission**](#10)
11. [**Error Analysis**](#11)
"""

INIT_CODE = """
import os
import sys
import random
import time
import hashlib
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 100)

# Root repo: notebook bisa dijalankan dari folder src/ maupun dari root
ROOT = Path.cwd() if (Path.cwd() / 'src').exists() else Path.cwd().parent
sys.path.insert(0, str(ROOT))

from src import metrics as M
from src.models import (C45DecisionTree, KNNClassifier, KNNRegressor, LinearRegression,
                        LogisticRegression, NaiveBayes)
from src.preprocessing import (PhishingPreprocessor, PlayerPreprocessor, QuantileScaler,
                               StandardScaler as OurStandardScaler)
from src import visualization as V
"""
