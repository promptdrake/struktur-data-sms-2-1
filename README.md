# Aplikasi Voting Ketua Kelas

Aplikasi Voting Ketua Kelas adalah program sederhana berbasis Python (CLI) yang digunakan untuk melakukan pemilihan ketua kelas secara digital.
Program ini dibuat untuk memenuhi tugas implementasi Struktur Data (List, Dictionary, dan Set).

## Tujuan Project

Mengimplementasikan minimal dua struktur data Python

Membuat sistem voting sederhana

Mencegah voting ganda

Menampilkan hasil dan menentukan pemenang

### Struktur Data yang Digunakan
- List

Digunakan untuk menyimpan daftar kandidat.

kandidat = ["Andi", "Budi", "Citra"]

-  Dictionary

Digunakan untuk menyimpan jumlah suara setiap kandidat.

hasil_suara = {
    "Andi": 0,
    "Budi": 0,
    "Citra": 0
}
- Set

Digunakan untuk menyimpan nama siswa yang sudah voting agar tidak bisa memilih dua kali.

sudah_voting = set()

 ## Fitur Aplikasi

- Menampilkan daftar kandidat
- Melakukan voting
- Mencegah voting ganda
- Menampilkan hasil sementara
