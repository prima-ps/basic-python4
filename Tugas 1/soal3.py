ujian_teori= float(input("Masukkan nilai ujian teori: "))
ujian_praktek = float(input("Masukkan nilai ujian praktek: "))
if(ujian_teori>=70 and ujian_praktek>=70):
    print("Selamat anda lulus")
elif(ujian_teori<70 and ujian_praktek>=70):
    print("Anda harus mengulang ujian teori")
elif(ujian_teori>=70 and ujian_praktek<70):
    print("Anda harus mengulang ujian praktek")
else :
    print("Anda harus mengulang ujian teori dan praktek")