siswa_list = []

def tampilkan_menu():
    """Menampilkan menu pilihan kepada pengguna."""
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Lihat Siswa")
    print("3. Edit Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")

def tambah_siswa():
    """Menambahkan data siswa baru ke dalam list."""
    nama = input("Masukkan Nama: ")
    while True:
        try:
            usia = int(input("Masukkan Usia: "))
            if usia <=0:
                raise ValueError("Usia harus bilangan bulat positif")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            nilai = float(input("Masukkan Nilai Rata-rata: "))
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai rata-rata harus antara 0 dan 100")
            break
        except ValueError as e:
            print(f"Error: {e}")

    siswa = {"nama": nama, "usia": usia, "nilai": nilai}
    siswa_list.append(siswa)
    print("[Siswa", nama, "berhasil ditambahkan!]")

def lihat_siswa():
    """Menampilkan daftar siswa."""
    if not siswa_list:
        print("Belum ada data siswa.")
        return

    print("\nDaftar Siswa:")
    for i, siswa in enumerate(siswa_list):
        print(f"{i+1}. Nama: {siswa['nama']}, Usia: {siswa['usia']}, Nilai Rata-rata: {siswa['nilai']}")

def edit_siswa():
    """Mengedit data siswa berdasarkan indeks."""
    lihat_siswa()
    while True:
        try:
            indeks = int(input("\nMasukkan indeks siswa yang ingin diedit (atau 0 untuk batal): ")) -1
            if indeks == -1:
                break
            if 0 <= indeks < len(siswa_list):
                siswa = siswa_list[indeks]
                siswa['nama'] = input(f"Nama baru ({siswa['nama']}): ") or siswa['nama']
                while True:
                    try:
                        siswa['usia'] = int(input(f"Usia baru ({siswa['usia']}): "))
                        if siswa['usia'] <= 0:
                            raise ValueError("Usia harus bilangan bulat positif")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
                while True:
                    try:
                        siswa['nilai'] = float(input(f"Nilai rata-rata baru ({siswa['nilai']}): "))
                        if siswa['nilai'] < 0 or siswa['nilai'] > 100:
                            raise ValueError("Nilai rata-rata harus antara 0 dan 100")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
                print("[Data siswa berhasil diubah!]")
                break
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def hapus_siswa():
    """Menghapus data siswa berdasarkan indeks."""
    lihat_siswa()
    while True:
        try:
            indeks = int(input("\nMasukkan indeks siswa yang ingin dihapus (atau 0 untuk batal): ")) - 1
            if indeks == -1:
                break
            if 0 <= indeks < len(siswa_list):
                nama = siswa_list[indeks]['nama']
                del siswa_list[indeks]
                print(f"[Siswa {nama} berhasil dihapus!]")
                break
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


while True:
    tampilkan_menu()
    while True:
        try:
            pilihan = int(input("Pilih menu: "))
            if 1 <= pilihan <= 5:
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 5.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    if pilihan == 1:
        tambah_siswa()
    elif pilihan == 2:
        lihat_siswa()
    elif pilihan == 3:
        edit_siswa()
    elif pilihan == 4:
        hapus_siswa()
    elif pilihan == 5:
        print("Program selesai.")
        break