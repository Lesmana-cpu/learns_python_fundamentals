while True:
    angka_tersembunyi = int(input('masukkan angka nya 0 - 77 = '))

    while angka_tersembunyi < 77:
        angka_tersembunyi += 1
        if angka_tersembunyi == 7:
            print(f'ini angka favorit ku ({angka_tersembunyi}) atau biner nya = {format(angka_tersembunyi, '08b')}')
        elif angka_tersembunyi == 1:
            print(f'tuhan itu hanya ada satu ({angka_tersembunyi})')
        elif angka_tersembunyi == 9:
            print(f'{angka_tersembunyi} <-- ini adalah angka pemecahan misteri alam semesta')
        elif angka_tersembunyi <= -1:
            print(f'di baca perintahnya dongo dari 0 bukan dari minus --> {angka_tersembunyi}')
        elif angka_tersembunyi == 6:
            pass
        elif angka_tersembunyi == 8:
            continue
        else:
            print(f'ini adalah angka biasa {angka_tersembunyi}')
            
    angka_benar = 6, 8

    pilihan = int(input('berapa angka yang tidak ada dalam hasil di atas? \n'))

    if pilihan == 6:
        print('kamu pintar dan cepat')
    elif pilihan == 8:
        print('kamu pintar dan cepat')
    elif pilihan == 7:
        print(f'karena {pilihan} angka kesukaan ku, ku kasih aja la \U0001F604, bit nya = {format(pilihan, '08b')}')
    else:
        print('kamu kurang beruntung')

    loop_and = str(input('mau ulang? y/n\n'))
    if loop_and == 'n':
        break
    else:
        continue
    
print('program telah selesai')
