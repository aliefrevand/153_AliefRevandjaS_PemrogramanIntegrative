import math

#gaji pengguna
gaji_tahunan = int(input("Masukkan gaji tahunan Anda: "))

#hitung gaji bulanan pengguna
gaji_bulanan = math.ceil(gaji_tahunan / 12)

#Tampil gaji bulanan pengguna
print(f"Gaji bulanan Anda adalah: Rp{gaji_bulanan}")
