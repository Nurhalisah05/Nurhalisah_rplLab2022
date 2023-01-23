# DATE AND TIME
import datetime as dt

tanggal = dt.date(2003,10,5)
print(tanggal)
print(f"INI ADALAH HARI = {tanggal:%A}")

print("Masukkan tanggal, \nbulan, dan tahun lahir mu\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("bulan \t\t: "))
tahun =int(input("tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal_lahir anda adakah : ", tanggal_lahir)
print(f"Hari nya adalah {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")

umur_hari = hari_ini -tanggal_lahir
umur_tahun = umur_hari / 365
umur_tahunn = umur_hari.days // 365
print("Umur anda adalah",umur_tahunn, "tahun") #MENAMPILKAN BERDASARKAN TAHUN
print(umur_tahun ,"Berdasarkan hari") #MENAMPILKAN BERDASRKAN HARI
print("Umur anda adalah :", umur_hari) 
