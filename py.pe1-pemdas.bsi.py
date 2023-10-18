print("----------------------------------------------------")
print("Kode Jurusan   Nama Prodi                     Harga ")
print("    SI         Sistem Informasi             2.400.000")
print("    SIA        Sistem Informasi Akutansi    2.000.000")
print("-----------------------------------------------------")

inpt_nis = int(input("Masukan NIS : "))
inpt_nama = str(input("Masukan Nama : "))
inpt_jurusan = str(input("Masukan Kode Jurusan : "))

data_SI = 2400000
data_SIA = 2000000

if inpt_jurusan == "SI" or inpt_jurusan == "si":
    print("-----------------------------------------------------")
    print("Jumlah Biaya Yang Harus Dibayar = Rp.",data_SI)
elif inpt_jurusan == "SIA" or inpt_jurusan == "sia":
    print("-----------------------------------------------------")
    print("Jumlah Biaya Yang Harus Dibayar = Rp.",data_SIA)
else:
    print("-----------------------------------------------------")
    print("                   Input Salah")