#credit to pythonindo.com

import smtplib #agar bisa mengirimkan email via smtp
import getpass #password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

alamat_pengirim = input("Masukkan alamat pengirim email: ")
password = getpass.getpass(prompt = "Masukkan pass: ")
fromaddr = alamat_pengirim
button=0
x=0
alamat_penerima=[]
while button!=5:
    print("---Menu---")
    print("1.Tambah Penerima")
    print("2. List Penerima")
    print("3. Kirim Email")
    print("4. Bersihkan list email")
    print("5. Keluar ")
    button = int(input("Masukkan pilihan yang diinginkan:"))
    if button==1:
        alamat_penerima.append(input("Masukkan email penerima: "))
        f = open("D:/Python/basic-python4/Final-Project/receiver_list.txt", "a")
        f.write(alamat_penerima[x]+'\n')
        f.close()
        x+=1
        print("Kontak berhasil ditambahkan")
        input("Press enter to continue")
    elif button==2:
        print("Data email yang sudah ditambahkan: ")
        for a in range(len(alamat_penerima)):
            print(a+1,". ",alamat_penerima[a])
        input("Press enter to continue")
    elif button==3:
        msg = MIMEMultipart()
        msg['Subject'] = input("Masukkan subject: ")
        body = input("Masukkan pesan: ")
        for a in range(len(alamat_penerima)):
            toaddr = alamat_penerima[a]
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = alamat_penerima[a]
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, password)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
        print("Pesan berhasil terkirim")
        input("Press enter to continue")
    elif button==4:
        open('D:/Python/basic-python4/Final-Project/receiver_list.txt', 'w').close()
        alamat_penerima.clear()
        x=0
        input("Press enter to continue")
    else :
        print("error")

open('D:/Python/basic-python4/Final-Project/receiver_list.txt', 'w').close()