# 3.	Dengan menggunakan Bahasa pemrograman python, tentukan apakah u dan v membentuk 
# sudut lancip, tumpul, orthogonal
# u = (0, 0, -1) dan v = (1, 1, 1)

u = [0, 0, -1]
v = [1, 1, 1]
udotv = []
for i in range (3):
    hasil = u[i] * v[i]
    # untuk menambahkan masuk ke dalam variabel udotv 
    # append berfungsi untuk menambahkan masuk kedalam array atau list 
    udotv.append(hasil)
# sum berfungsi utuk menjumlahkan semua element yang ada dalam array
sudut = sum(udotv)
print (u)
print (v)
print (udotv)

print (sudut)

if(sudut < 0):
    print("u dan v membentuk sudut tumpul")
else:
    if(sudut > 0):
        print("u dan v membentuk sudut lancip")
    else:
        print("u dan v membentuk sudut orthogonal")

