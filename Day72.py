#Menghitung Harga Total Penjualan
HrgPerSakSemen = 60000 
JumalahSemenYgDiBeli = int(input("Masukkan Jumlah Semen yang Dibei : "))
HrgSemenYgDibeli = HrgPerSakSemen * JumalahSemenYgDiBeli
Diskon1 = 2/100 #Sama Dengan 2%
Diskon2 = 5/100 #Sama Dengan 5%
if JumalahSemenYgDiBeli >=200  :
    print("Mendapatkan Potongan Sebesar 5%, Total yang Dibayar :Rp.",HrgSemenYgDibeli - Diskon2)
elif JumalahSemenYgDiBeli >= 100 :
    print ("Mendapatkan Potongan Sebesar 2%, Total yang Dibayar :Rp.",HrgSemenYgDibeli - Diskon1)
else:
    print("Tidak Mendapatkan Diskon")