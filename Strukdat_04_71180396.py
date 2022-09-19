import json

with open("mahasiswa.json","a+") as file:
    nMahasiswa = int(input("Masukkan jumlah mahasiswa baru: "))
    for i in range(0,nMahasiswa):
        NamaMahasiswa = input(" Masukkan nama anda : ")
        nHobi = int(input("Masukkan Jumlah hobi : "))
        for j in range(0, nHobi):
            hobby = input(f"Masukkan Hobi ke-{(j+1)}: ")
        Prestasi = input("Masukkan Prestasi Anda : ")
        print("="*3,"Data Berhasil Ditambahkan","="*3)

print(hobby)