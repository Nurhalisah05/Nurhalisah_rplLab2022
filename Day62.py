listBloBTP = [
  'BlokA', 'BlokB', 'BlokC', 'BlokD', 'BlokE',
]

BlokBTP = input('Masukkan nama Blok  yang dicari: ')

i = 0
while i < len(listBloBTP):
  if listBloBTP[i].lower() == BlokBTP.lower():
    print('Ketemu di index', i)
    break

  print('Bukan ', listBloBTP[i])
  i += 1
else:
  print('Maaf, kota yang anda cari tidak ditemukan.')