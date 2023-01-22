#Width AND Multiline
#Data
data_nama = "Nur halisah"
umur = 19
data_tinggi = 156
data_noSepatu = 37

#String standard
data_String = f"nama = {data_nama}, umur = {umur}, tinggi = {data_tinggi}, sepatu = {data_noSepatu}"
print(5*"="+"DATA STRIN"+5*"=")
print(data_String)

#String multiline (Menggunakan enter, newLine, \n)
data_String = f"nama = {data_nama}, \numur = {umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_noSepatu}"
print(5*"="+"DATA STRIN"+5*"=")
print(data_String)

#String multiline triplrts
data_String = f"""nama = {data_nama}
umur = {umur}
tinggi = {data_tinggi}
sepatu = {data_noSepatu}
"""
print(5*"="+"DATA STRIN"+5*"=")
print(data_String)

#Mengatur lebar
data_nama = "halisah"
data_String = f"""
nama = {data_nama:>6}
umur = {umur:>6}
tinggi = {data_tinggi:>3}
sepatu = {data_noSepatu:>3}
"""
print(5*"="+"DATA STRIN"+5*"=")
print(data_String)