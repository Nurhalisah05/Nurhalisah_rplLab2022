# Menginput Jarak dalam Satuan Kilometer
kilometer = float(input("Tuliskan Jarak dalam Kilometer: "))
 
# Nilai Faktor Konversi
faktor_konversi = 0.621371
 
# Menghitung Jarak dalam Satuan Mil
mil = kilometer * faktor_konversi
 
# Menampilkan Hasil Konversi Jarak
print('%0.2f Kilometer sama dengan %0.2f Mil' %(kilometer,mil))
