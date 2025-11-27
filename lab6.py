# List global untuk menyimpan data mahasiswa
daftar_mahasiswa = []

# --- Fungsi untuk Menambah Data ---
def tambah():
    """Meminta input nama dan nilai, lalu menambahkannya ke daftar_mahasiswa."""
    print("\n--- Tambah Data Mahasiswa ---")
    nama = input("Masukkan Nama Mahasiswa: ").strip()
    
    # Validasi nama agar tidak kosong
    if not nama:
        print("PERINGATAN: Nama tidak boleh kosong.")
        return

    # Validasi nilai
    while True:
        try:
            nilai_str = input("Masukkan Nilai (0-100): ").strip()
            nilai = int(nilai_str)
            if 0 <= nilai <= 100:
                break
            else:
                print("PERINGATAN: Nilai harus dalam rentang 0 hingga 100.")
        except ValueError:
            print("PERINGATAN: Input nilai tidak valid. Harap masukkan angka.")
    
    # Membuat dictionary baru dan menambahkannya ke list
    mahasiswa_baru = {"nama": nama, "nilai": nilai}
    daftar_mahasiswa.append(mahasiswa_baru)
    print(f"\nSUKSES: Data '{nama}' dengan nilai {nilai} berhasil ditambahkan.")

# --- Fungsi untuk Menampilkan Data ---
def tampilkan():
    """Menampilkan seluruh data mahasiswa dalam bentuk tabel."""
    print("\n--- Daftar Nilai Mahasiswa ---")
    if not daftar_mahasiswa:
        print("INFORMASI: Daftar mahasiswa kosong.")
        return

    # Menghitung panjang maksimum untuk format tabel
    # Setidaknya panjang 4 untuk 'Nama'
    max_len_nama = max(len(m['nama']) for m in daftar_mahasiswa) if daftar_mahasiswa else 4 
    
    # Header tabel
    header = f"| {'No.':<4} | {'Nama':<{max_len_nama}} | {'Nilai':<5} |"
    separator = "-" * len(header)
    
    print(separator)
    print(header)
    print(separator)
    
    # Isi tabel
    for i, m in enumerate(daftar_mahasiswa):
        print(f"| {i+1:<4} | {m['nama']:<{max_len_nama}} | {m['nilai']:<5} |")
        
    print(separator)

# --- Fungsi untuk Menghapus Data ---
def hapus(nama):
    """Menghapus data mahasiswa berdasarkan nama yang diberikan."""
    nama_lower = nama.lower()
    
    global daftar_mahasiswa
    panjang_awal = len(daftar_mahasiswa)
    
    # Filter list: hanya simpan data yang namanya tidak cocok (case-insensitive)
    daftar_mahasiswa = [
        m for m in daftar_mahasiswa 
        if m['nama'].lower() != nama_lower
    ]
    
    panjang_akhir = len(daftar_mahasiswa)
    
    if panjang_akhir < panjang_awal:
        print(f"\nSUKSES: Data dengan nama '{nama}' berhasil dihapus.")
    else:
        print(f"\nPERINGATAN: Data dengan nama '{nama}' tidak ditemukan.")

# --- Fungsi untuk Mengubah Data ---
def ubah(nama):
    """Mengubah nilai mahasiswa berdasarkan nama yang diberikan."""
    nama_lower = nama.lower()
    ditemukan = False
    
    print(f"\n--- Ubah Data untuk '{nama}' ---")
    
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa['nama'].lower() == nama_lower:
            ditemukan = True
            
            # Meminta input nilai baru
            while True:
                try:
                    nilai_baru_str = input("Masukkan Nilai Baru (0-100): ").strip()
                    nilai_baru = int(nilai_baru_str)
                    if 0 <= nilai_baru <= 100:
                        mahasiswa['nilai'] = nilai_baru
                        print(f"\nSUKSES: Nilai '{mahasiswa['nama']}' berhasil diubah menjadi {nilai_baru}.")
                        return
                    else:
                        print("PERINGATAN: Nilai harus dalam rentang 0 hingga 100.")
                except ValueError:
                    print("PERINGATAN: Input nilai tidak valid. Harap masukkan angka.")
    
    if not ditemukan:
        print(f"\nPERINGATAN: Data dengan nama '{nama}' tidak ditemukan.")

# --- Fungsi Utama (Main Menu) ---
def main_menu():
    """Menampilkan menu utama dan menjalankan program."""
    while True:
        print("\n" + "="*35)
        print("PROGRAM PENGELOLA NILAI MAHASISWA")
        print("="*35)
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Nilai Mahasiswa")
        print("5. Keluar")
        print("-" * 35)

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama_hapus = input("Masukkan Nama Mahasiswa yang ingin dihapus: ").strip()
            hapus(nama_hapus)
        elif pilihan == '4':
            nama_ubah = input("Masukkan Nama Mahasiswa yang ingin diubah nilainya: ").strip()
            ubah(nama_ubah)
        elif pilihan == '5':
            print("\nProgram selesai. Terima kasih!")
            break
        else:
            print("\nKESALAHAN: Pilihan tidak valid. Silakan coba lagi.")

# Memulai program
if __name__ == "__main__":
    main_menu()