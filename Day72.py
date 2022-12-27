#Menghitung Harga Total Penjualan
HrgPerSakSemen = 60000 
JumalahSemenYgDiBeli = int(input("Masukkan Jumlah Semen yang Dibei"))
if JumalahSemenYgDiBeli > 100 :
    print("Mendapatkan Potongan Sebesar 2%", JumalahSemenYgDiBeli - 2/100)
elif JumalahSemenYgDiBeli > 200 :
    print ("Mendapatkan potongan sebesar 5%", JumalahSemenYgDiBeli - 5/100)
else:
    print("Tidak Mendapatjan Diskon")
