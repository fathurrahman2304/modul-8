def jumlah(angka = 0,jml = 0,i = 1):
    if jml < 1:
        return 0
    else:
        angka = int(input(f'Masukkan angka ke-{i}: '))
        if jml == 1:
            return angka
        else:
            i += 1
            return angka + jumlah(angka,jml - 1,i)
x = int(input('Masukkan jumlah angka: '))
nilai = jumlah(jml = x)
print(f'Hasil penjumlahan {nilai}')