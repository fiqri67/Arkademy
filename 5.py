string = ""

angka = int(input("Masukkan angka :"))
baris = angka
# Looping Baris
while baris >= 0:

    # Looping Kolom Spasi Kosong
    kolom = baris
    while kolom > 0:
        string = string + "   "
        kolom = kolom - 1

    # Looping Kolom Bintang
    kanan = 1
    while kanan < (angka - (baris - 1)):
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n"
    baris = baris - 1

print(string)