# Instruksi untuk AI assistant (Cursor, Copilot, ChatGPT, dll.)

Sebelum menulis atau mengubah kode di repo ini, BACA berurutan:
1. `PANDUAN.md`    -> konteks proyek, arsitektur, keputusan desain, setup, Git, submisi
2. `CONSTRAINT.md` -> aturan yang TIDAK BOLEH dilanggar (from scratch, anti-leakage, reproducible, dll.)
3. `MATERI.md`     -> materi kuliah resmi (slide + video) yang menjadi acuan algoritma
4. `CHECKLIST.md`  -> tugas tiap anggota, pembagian kerja, timeline
5. `instruction/spek.md` -> spesifikasi resmi tugas

Aturan singkat paling penting:
- Model (KNN, C4.5, Logistic Regression, Naive Bayes, Linear Regression) hanya boleh memakai NumPy (+ math). Tidak boleh sklearn di folder `src/models/`.
- Preprocessing selalu `fit` pada data latih saja, lalu `transform` data lain. Train dan test tidak boleh digabung.
- Teknik di luar materi kelas wajib diberi komentar sumber/referensi di kode.
- Jalankan `python tests/test_models.py` setelah mengubah model. Semua test harus lulus.
- Jangan ubah file submisi final tanpa persetujuan leader (lihat PANDUAN.md §9.2).
- Bahasa dokumentasi dan komentar: Bahasa Indonesia.
