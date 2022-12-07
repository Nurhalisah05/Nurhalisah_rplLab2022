#PROGRAM LATIHAN SEDERHANA
#Program Konversi celcius ke satuan lain
print ("PROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("MAsukkan Suhu dalam celcius : "))
print ("Suhu adalah", celcius, "Celcius")

#Reamur
#Rumus (4/5) c
reamur = (4/5) * celcius
print ("Suhu dalam reamur adalah", reamur, "Celcius")

#fahrenheit
fahrenheit = ((9/5) *celcius) + 32
print ("Suhu dalam fahrenheit adalah", fahrenheit, "Celcius")

#Kelvin
kelvin = celcius + 273
print ("Suhu dalam kelvin adalah", kelvin, "Celcius")