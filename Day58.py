u = [3, 2, -1]
w = [2, 6, 7]
v = [0, 2, -3]
uw = [20, -23, 14]

uKaliW = ((u[1] * w[2] - u[2] * w[1]),(u[2] * w[0] - u[0] * w[2]),(u[0] * w[1] - u[1] * w[0]))
print("hasil perkalian silang dari u dan w : ",uKaliW)
hasil = ((u[1]*uKaliW[2] - u[2]*uKaliW[1]), (u[2]*uKaliW[0] - u[0]*uKaliW[2]),(u[0]*uKaliW[1] - u[1]*uKaliW[0]))
print ("hasil perkalian silang dari u dan hasil perkalian dari u dan v : ", hasil)