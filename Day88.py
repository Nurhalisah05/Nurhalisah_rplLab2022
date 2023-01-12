def main():
    # cetak judul program
    print('program menentukan nilai maksimum tiga bilangan Cara Pertama')
 
    # input user
    a = int(input('masukan bilangan ke-1: '))
    b = int(input('masukan bilangan ke-2: '))
    c = int(input('masukan bilangan ke-3: '))
 
    # menenukan nilai terbesar
    if a > b:
        if a > c:
            maks = a
    else:
        if b > c:
            maks = b
        else:
            maks = c
 
    print('Nilai yang terbesar adalah: %d' % maks)
         
if __name__=='__main__':
    main()