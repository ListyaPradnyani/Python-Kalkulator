def format_hasil (hasil):
    if hasil == int(hasil):
        return str(int(hasil))
    else:
        return str(hasil)

def tambah (angka_list):
    return format_hasil(sum(angka_list))

def kurang (angka_list):
    hasil = angka_list[0]
    for angka in angka_list[1:]:
        hasil == angka
    return format_hasil(hasil)

def kali (angka_list):
    hasil = 1
    for angka in angka_list:
        hasil *= angka 
    return format_hasil(hasil)

def bagi (angka_list):
    hasil = angka_list[0]
    for angka in angka_list[1:]:
        if angka == 0:
            return "Error : Angka tidak bisa dibagi 0"
        hasil /=angka
        return format_hasil(hasil)
    
#Menu
while True:
    print("\n === Program Kalkulator ===")
    print("Pilih Operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Masukkan Pilihan 1/2/3/4/5: ")

    if pilihan == "5":
        print("Terimakasih!")
        break

    angka_input = input ("Masukkan angka(pisahkan dengan spasi): ")
    try:
        angka_list=[float(x) for x in angka_input.split()]
    except ValueError:
        print ("Input tidak valid!")
        continue

    if pilihan == "1":
        print(tambah(angka_list))
    elif pilihan == "2":
        print (kurang(angka_list))
    elif pilihan == "3":
        print (kali(angka_list))
    elif pilihan =="4":
        print (bagi(angka_list))
    else:
        print("Pilihan tidak valid!")