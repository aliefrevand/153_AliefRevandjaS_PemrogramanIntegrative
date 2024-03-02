# masukkan angka
angka = int(input("Masukkan angka: "))

# tentukan kategori angka
if angka < 100:
  kategori = "Small"
elif angka > 200:
  kategori = "Large"
else:
  kategori = "Medium"

# Menampilkan kategori
print(f"Angka yang anda masukkan {angka} termasuk kedalam kategori {kategori}")
