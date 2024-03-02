# Menginisialisasi variabel 
jumlah = 0
angka = 0

# Menampilkan dan memasukkan angka
print("Masukkan angka-angka (akhiri dengan -1):")

# Perulangan untuk membaca angka-angka sampai -1 dimasukkan
while angka != -1:
  # Membaca angka dari pengguna
  angka = int(input())

  # Jika angka bukan -1, tambahkan ke total
  if angka != -1:
    jumlah += angka

# tampilan total
print(f"Jumlah dari semua angka yang dimasukkan adalah {jumlah}")
