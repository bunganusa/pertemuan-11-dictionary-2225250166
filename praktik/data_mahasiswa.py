

def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM secara aman."""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

def main():
    # 1. Inisialisasi data minimal 5 mahasiswa
    data_mahasiswa = {
        "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
        "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
        "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
        "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
        "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
    }

    print("=" * 45)
    print("      SISTEM DATA MAHASISWA (PERTEMUAN 11)   ")
    print("=" * 45)

    # 2. Uji Pencarian Data (Tersedia dan Tidak Tersedia)
    print("\n--- 1. PENCARIAN MAHASISWA ---")
    nim_cari_1 = "A003"
    hasil_1 = cari_mahasiswa(data_mahasiswa, nim_cari_1)
    if hasil_1 is not None:
        print(f"Cari [{nim_cari_1}] -> Nama: {hasil_1['nama']}, Kelas: {hasil_1['kelas']}, Nilai: {hasil_1['nilai']}")
    else:
        print(f"Cari [{nim_cari_1}] -> Data tidak ditemukan")

    nim_cari_2 = "A999"
    hasil_2 = cari_mahasiswa(data_mahasiswa, nim_cari_2)
    if hasil_2 is not None:
        print(f"Cari [{nim_cari_2}] -> Nama: {hasil_2['nama']}, Kelas: {hasil_2['kelas']}, Nilai: {hasil_2['nilai']}")
    else:
        print(f"Cari [{nim_cari_2}] -> Data tidak ditemukan")

    # 3. Ubah Nilai Salah Satu Mahasiswa (A002 menjadi 82)
    print("\n--- 2. PEMBARUAN DATA ---")
    data_mahasiswa["A002"]["nilai"] = 82
    print("Nilai A002 berhasil diperbarui menjadi 82")

    # 4. Tambah Mahasiswa Baru (A006)
    print("\n--- 3. PENAMBAHAN DATA MAHASISWA BARU ---")
    data_mahasiswa["A006"] = {
        "nama": "Fajar",
        "kelas": "B",
        "nilai": 80
    }
    print("Data mahasiswa A006 (Fajar) berhasil ditambahkan")

    # 5. Rekap Seluruh Data Menggunakan items()
    print("\n--- 4. REKAP SELURUH DATA MAHASISWA ---")
    print("-" * 45)
    print(f"{'NIM':<6} | {'Nama':<10} | {'Kelas':<6} | {'Nilai':<5}")
    print("-" * 45)
    for nim, info in data_mahasiswa.items():
        print(f"{nim:<6} | {info['nama']:<10} | {info['kelas']:<6} | {info['nilai']:<5}")
    print("-" * 45)

    # 6. Hitung dan Tampilkan Rata-Rata Nilai
    rata = rata_rata_nilai(data_mahasiswa)
    print(f"\nRata-rata nilai seluruh mahasiswa: {rata:.2f}")
    print("=" * 45)

if __name__ == "__main__":
    main()