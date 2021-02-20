name =[]
umur =[]

n =int(input("Masukkan jumlah pengunjung: "))
for x in range(n):
    print(x+1,".", end=" ")
    name.append(input("Masukkan nama: "))
    umur.append(input("    Masukkan umur: "))

print("Jumah pengunjung hari ini")
for x in range(n):
    print(x+1,".",name[x],"dengan umur",umur[x])
