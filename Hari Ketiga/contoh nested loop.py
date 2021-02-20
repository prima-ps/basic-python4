name= []
mata_kuliah = [[],[]]
nilai = [[[],[],[]],[[],[],[]]] #bentuk list tiga dimensi

n= int(input("Masukkan jumlah mahasiswa: "))
m= int(input("Masukkan jumlah mata kuliah: "))
o=int(input("Masukkan jumlah ujian: "))
for x in range(n):
    print(x+1,".", end=" ")
    name.append(input("Masukkan nama mahasiswa: "))
    for y in range(m):
        print("    ",y+1,".",end=" ")
        mata_kuliah[x].append(input("Masukkan nama mata kuliah: "))
        for z in range(o):
             print("       ",z+1,". Masukkan nilai ujian ",z+1,end=" ")
             nilai[x][y].append(input())


            


print("Berikut rekap nilai dari para mahasiswa")
for x in range(n):
    print(x+1,". Mata kuliah", x+1, "adalah", name[x])
    for y in range(m):
        print("    ",y+1,". Mata kuliah", y+1, "adalah ",mata_kuliah[x][y])
        for z in range(o):
            print("        Nilai ujian",mata_kuliah[x][y], "adalah ",nilai[x][y][z])
