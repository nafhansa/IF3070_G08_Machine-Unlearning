# Laporan transkripsi IF3270 Decision Tree Learning

## Hasil

Sembilan transkrip Markdown dan `ALL_TRANSCRIPTS.md` dibuat berurutan sesuai daftar video. Bahasa asli seluruh subtitle adalah Indonesia. Heading bagian ditambahkan sebagai penanda editorial; heading tersebut bukan ucapan dalam video.

| No. | Video | Berkas | Durasi | Metode |
|---:|---|---|---:|---|
| 01 | Attribute Types | `01_Attribute_Types.md` | 06:50 | Subtitle otomatis asli YouTube (`id-orig`) |
| 02 | What, Why, and When | `02_What_Why_and_When.md` | 04:47 | Subtitle otomatis asli YouTube (`id-orig`) |
| 03 | Basic DTL Algorithm (ID3) | `03_Basic_DTL_Algorithm_ID3.md` | 08:49 | Subtitle otomatis asli YouTube (`id-orig`) |
| 04 | Information Gain | `04_Information_Gain.md` | 20:17 | Subtitle otomatis asli YouTube (`id-orig`) |
| 05 | Overfitting | `05_Overfitting.md` | 21:10 | Subtitle otomatis asli YouTube (`id-orig`) |
| 06 | Continuous-Valued Attribute | `06_Continuous_Valued_Attribute.md` | 07:13 | Subtitle otomatis asli YouTube (`id-orig`) |
| 07 | Missing Attribute Values | `07_Missing_Attribute_Values.md` | 09:20 | Subtitle otomatis asli YouTube (`id-orig`) |
| 08 | Alternative Measures | `08_Alternative_Measures.md` | 09:23 | Subtitle otomatis asli YouTube (`id-orig`) |
| 09 | Attributes with Differing Costs | `09_Attributes_with_Differing_Costs.md` | 06:16 | Subtitle otomatis asli YouTube (`id-orig`) |

## Pemrosesan dan verifikasi

- `yt-dlp` mengambil metadata, subtitle asli, dan audio sementara. `ffmpeg` serta `ffprobe` tersedia. Tidak ada MP4 yang diunduh.
- Cue WebVTT YouTube yang bertumpang tindih dibersihkan: teks lama dalam cue bergulir dan cue duplikat 10 ms dibuang, sedangkan frasa baru dipertahankan sesuai urutan dan timestamp sumber. Beberapa salah eja istilah yang jelas dari konteks dinormalisasi secara terbatas.
- Setiap transkrip dicek terhadap seluruh frasa baru pada subtitle sumber; teksnya harus sama urutan dan jumlahnya. File gabungan dicek memuat sembilan transkrip secara utuh dan berurutan. Cakupan subtitle mencapai sekitar 2–5 detik dari akhir durasi video.

## Keterbatasan dan hambatan

- **Akurasi:** Subtitle `id-orig` dihasilkan otomatis oleh YouTube. Beberapa istilah teknis, nama atribut, angka, dan rumus matematika tampak salah dikenali. Transkrip mempertahankan teks sumber yang belum dapat dipastikan; jangan menganggapnya hasil audit audio kata demi kata. Ucapan yang tidak jelas tidak direka ulang.
- **Whisper:** Model `mlx-whisper` yang telah terpasang tidak dapat mengakses perangkat Metal dalam sandbox ini. Fallback `faster-whisper` berhasil terpasang, tetapi unduhan modelnya gagal karena `huggingface.co` tidak dapat di-resolve. Tidak ada keluaran Whisper yang digunakan.
- **Lokasi:** Sandbox menolak pembuatan direktori `~/Downloads/IF3270_DTL_Transcripts/` (`Operation not permitted`). Sesuai instruksi untuk tidak meminta izin tambahan, berkas disimpan di direktori kerja yang dapat ditulis: `/Users/owfaris/Documents/kuliah2/dai/tubes kaggle/IF3270_DTL_Transcripts/`.
- Audio sementara di `/private/tmp/IF3270_dtl_audio/` telah dihapus setelah verifikasi akhir berhasil. Berkas subtitle sumber disimpan di `.dtl_work/` agar koreksi nantinya dapat ditelusuri.
