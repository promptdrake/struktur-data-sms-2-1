# ==============================
# APLIKASI VOTING KETUA KELAS
# ==============================

# List kandidat
kandidat = ["Andi", "Budi", "Citra"]

# Dictionary untuk menyimpan jumlah suara
hasil_suara = {nama: 0 for nama in kandidat}

# Set untuk menyimpan siswa yang sudah voting
sudah_voting = set()

def tampilkan_kandidat():
    print("\n=== DAFTAR KANDIDAT ===")
    for i, nama in enumerate(kandidat, start=1):
        print(f"{i}. {nama}")

def voting():
    nama_siswa = input("\nMasukkan nama Anda: ").strip()

    if nama_siswa in sudah_voting:
        print("⚠️ Anda sudah melakukan voting!")
        return

    tampilkan_kandidat()
    try:
        pilihan = int(input("Pilih nomor kandidat: "))
        if 1 <= pilihan <= len(kandidat):
            kandidat_dipilih = kandidat[pilihan - 1]
            hasil_suara[kandidat_dipilih] += 1
            sudah_voting.add(nama_siswa)
            print("✅ Voting berhasil!")
        else:
            print("❌ Nomor tidak valid!")
    except ValueError:
        print("❌ Input harus berupa angka!")

def tampilkan_hasil():
    print("\n=== HASIL SEMENTARA ===")
    for nama, suara in hasil_suara.items():
        print(f"{nama}: {suara} suara")

def tentukan_pemenang():
    pemenang = max(hasil_suara, key=hasil_suara.get)
    print("\n🏆 PEMENANG VOTING ADALAH:", pemenang)
    print("Dengan total suara:", hasil_suara[pemenang])

# Menu utama
while True:
    print("\n===== MENU VOTING =====")
    print("1. Voting")
    print("2. Lihat Hasil")
    print("3. Tentukan Pemenang")
    print("4. Keluar")

    pilihan_menu = input("Pilih menu: ")

    if pilihan_menu == "1":
        voting()
    elif pilihan_menu == "2":
        tampilkan_hasil()
    elif pilihan_menu == "3":
        tentukan_pemenang()
    elif pilihan_menu == "4":
        print("Terima kasih sudah menggunakan aplikasi voting!")
        break
    else:
        print("❌ Pilihan tidak valid!")
