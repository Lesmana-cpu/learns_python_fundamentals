# Latihan

list_buku = []

while True:
    x = 1
    while x <= 5:
        x += 1
        judul = input('\nmasukkan judul buku = ')
        penulis = input('siapa penulisnya = ')
        
        judul_rapi = judul.ljust(25)
        penulis_rapi = penulis.ljust(25)
        data_buku = [judul_rapi,penulis_rapi]
        list_buku.append(data_buku)
        
        print(f'{'NO'}| {'judul'.center(25)} | {'penulis'.center(25)}')
        for index, buku in enumerate (list_buku):
            print(f'{index + 1} | {(buku[0])} | {buku[1]}')
            
        
    pilihan = input('\n\n\t\tingin lanjut? y/n\n')
    if pilihan == 'n':
        print('program telah di hentikan')
        break
    else:
        print('\n\n' + 'program pengumpulan data di lanjutkan'.center(115))