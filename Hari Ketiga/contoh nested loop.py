name= []
mata_kuliah = [[],[]]
nilai = [[[],[],[]],[[],[],[]]] #bentuk list tiga dimensi

n= int(input("Masukkan jumlah mahasiswa: "))
m= int(input("Masukkan jumlah mata kuliah: "))
for x in range(n):
    print(x+1,".", end=" ")
    name.append(input("Masukkan nama mahasiswa: "))
    for y in range(m):
        print("    ",y+1,".",end=" ")
        mata_kuliah[x].append(input("Masukkan nama mata kuliah: "))
        o=int(input("Masukkan jumlah ujian: "))
        for z in range(o):
             print("       ",z+1,". Masukkan nilai ujian ",z+1, " :",end=" ")
             nilai[x][y].append(input())


            


print("Berikut rekap nilai dari para mahasiswa")
for x in range(n):
    print(x+1,". Nama mahasiswa adalah:", x+1, "adalah", name[x])
    for y in range(m):
        print("    ",y+1,". Mata kuliah", y+1, "adalah ",mata_kuliah[x][y])
        total_nilai= 0
        for z in range(len(nilai[x][y])):
            print("        Nilai ujian",mata_kuliah[x][y], "adalah ",nilai[x][y][z])
            total_nilai = total_nilai+int(nilai[x][y][z])
            print(total_nilai)
            if z==(len(nilai[x][y])-1):
                mean = total_nilai/len(nilai[x][y])
                print("Dengan nilai rata-rata sebesar :{:.2f}".format(mean))

            
