def menu():
    print("---Menu---")
    print("1.Daftar Kontak")
    print("2.Tambah Kontak")
    print("3. Keluar")

    
print("Selamat Datang!")
n=0
nama = []
nomor = []
while (n!=3):
    menu()
    n= int(input("Pilih menu: "))
    if n==1:
        for a in range(len(nama)):
            print("Nama: " +nama[a])
            print("Nomor Telepon: " +nomor[a])
        input("Press enter to continue")
    if n==2:
        nama.append(input("Masukkan nama: "))
        nomor.append(input("Masukkan nomor: "))
        print("Kontak berhasil ditambahkan")
        input("Press enter to continue")
    if n==3:
        print("Program selesai, sampai jumpa!")
    if n<1 or n>3:
        print("Menu tidak tersedia")

