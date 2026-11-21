#!/usr/bin/env bash
# Jalankan kedua notebook dari awal sampai akhir (dipakai juga untuk cek reproducibility).
# Pakai: bash tools/run_all.sh   (dari root repo; butuh venv di .venv/ atau set JUPYTER=jupyter)
set -e
cd "$(dirname "$0")/../src"
JUPYTER=${JUPYTER:-../.venv/bin/jupyter}
for nb in tubes2_klasifikasi.ipynb tubes2_regresi.ipynb; do
  echo ">> menjalankan $nb"
  $JUPYTER nbconvert --to notebook --execute --inplace "$nb" --ExecutePreprocessor.timeout=3600
done
cd ..
echo ">> MD5 submisi:"
md5 -r output/submissions/*.csv 2>/dev/null || md5sum output/submissions/*.csv
