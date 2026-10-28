# Pertemuan 11 - Dictionary/Map dan Pasangan Key-Value

- **Nama**: Bunga Nusa Pertiwi
- **NIM**: 2225250166
- **Kelas**: 3F

---

## Deskripsi Tugas
Praktikum Pertemuan 11 berfokus pada pemodelan data pendidikan menggunakan dictionary (map) dalam Python, yang meliputi penggunaan pasangan key-value, akses aman dengan method `get()`, manipulasi data (tambah, ubah, hapus), iterasi dengan `items()`, penanganan dictionary bersarang, serta pembuatan fungsi modular.

---

## Struktur Data
Struktur data yang digunakan dalam program utama `praktik/data_mahasiswa.py` adalah **dictionary bersarang**:
- **Key Utama**: NIM Mahasiswa (contoh: `"A001"`, `"A002"`).
- **Value**: Dictionary berisi atribut identitas dan nilai mahasiswa (`{"nama": str, "kelas": str, "nilai": int}`).

---

## Daftar File dan Ringkasan Kodingan

| No | File / Folder | Keterangan Ringkas Program |
| :---: | :--- | :--- |
| **1** | `README.md` | Dokumentasi tugas, daftar file, test case, dan refleksi |
| **2** | `.gitignore` | Mengabaikan file cache Python (`__pycache__`) dan settingan editor |
| **3** | `latihan/01_dasar_dictionary.py` | Memuat pasangan key-value dasar dan menampilkan nilainya |
| **4** | `latihan/02_akses_get.py` | Mengakses key secara aman dengan `get()` untuk mencegah KeyError |
| **5** | `latihan/03_manipulasi_dictionary.py` | Menambah, mengubah, dan menghapus pasangan key-value |
| **6** | `latihan/04_iterasi_dictionary.py` | Menelusuri pasangan key dan value menggunakan `items()` |
| **7** | `latihan/05_dictionary_bersarang.py` | Mengakses data pendidikan pada dictionary bersarang |
| **8** | `latihan/06_fungsi_dictionary.py` | Pencarian data mahasiswa berdasarkan NIM menggunakan fungsi |
| **9** | `praktik/data_mahasiswa.py` | Sistem data mahasiswa (pencarian, ubah, tambah, rekap, & rata-rata) |

---

## Cara Menjalankan Program

Jalankan perintah berikut di Terminal VS Code dari folder utama proyek:

### 1. Menjalankan File Latihan
```bash
python latihan/01_dasar_dictionary.py
python latihan/02_akses_get.py
python latihan/03_manipulasi_dictionary.py
python latihan/04_iterasi_dictionary.py
python latihan/05_dictionary_bersarang.py
python latihan/06_fungsi_dictionary.py
```

### 2. Menjalankan Program Praktik Utama
```bash
python praktik/data_mahasiswa.py
```

---

## Hasil Pengujian (Test Case)

| No | Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Cari NIM `A003` | Data Citra (Kelas B, Nilai 92) ditampilkan | Data Citra ditampilkan | **Sesuai** |
| **2** | Cari NIM `A999` | Pesan `'Data tidak ditemukan'` tanpa KeyError | Pesan `'Data tidak ditemukan'` | **Sesuai** |
| **3** | Pembaruan Nilai | Nilai `A002` berubah menjadi `82` | Nilai `A002` menjadi `82` | **Sesuai** |
| **4** | Penambahan Data | Key `A006` (Fajar) tersedia setelah ditambahkan | Key `A006` ditambahkan | **Sesuai** |
| **5** | Rekap `items()` | Semua NIM dan data mahasiswa tampil rapi | Seluruh data tampil rapi | **Sesuai** |
| **6** | Rata-Rata Kelas | Rata-rata nilai kelas dihitung dengan benar | Rata-rata: `82.83` | **Sesuai** |

---

## Refleksi Praktik

| No | Topik Refleksi | Penjelasan / Solusi |
| :---: | :--- | :--- |
| **1** | **Kesalahan `KeyError`** | Mengakses key yang tidak ada menggunakan kurung siku (misal `data['A999']`) memicu program error. |
| **2** | **Solusi Penggunaan `get()`** | Menggunakan method `.get(nim)` atau pengecekan `if nim in data` untuk menangani key tak ada secara aman. |
| **3** | **Iterasi Tepat dengan `items()`** | Menggunakan `for key, value in data.items()` untuk menelusuri key utama dan value dictionary bersarang sekaligus. |