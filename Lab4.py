#SOAL 1 - MENCETAK NAMA
#TULISKAN PROGRAM UNTUK SOAL NO 1 DI BAWAH INI
nama = input("masukkan nama: ")
#INPUT NAMA
jumlahkata = len(nama)
#HITUNG JUMLAH KATA DENGAN LEN
i = 0
while i < jumlahkata:
#KETIK I < JUMLAH KATA, BAGIAN INI AKAN DI LOOPING
	i = i + 1
	print(nama[0:i])
#PRINT NAMA MENGGUNAKAN STRING SLICING, MAKA AKAN MEMBENTUK PERKATA SETIAP LOOP
print("============================")

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
while True:
  text = input("Masukkan sebuah teks : ")
  #input text
  jumlahtext = len(text)
  #hitungjumlah text

  if (jumlahtext >= 8 
  # validasi text jumlah text diatas 8 
  and (text.endswith("YYY") or text.endswith("yyy"))
  # validasi text ujungnya YYY atau yyy 
  and (text.startswith('NF') or text.startswith('nf') or text.startswith('Nf') or text.startswith('nF'))
  # validasi text berupa NF, nf, Nf, atau nF di awal text 
  and not (text.isalpha())
  #dan tidak text semua

  ):
  # validasi text tersebut harus berisi nomor
    print("Teks valid, Selamat Datang.")
    #jika semuanya tersedia maka valid
    break
    #end looping dengan break
  else:
    print("Teks tidak valid.")
    # jika salah satunya saja tidak ada maka tidak valid
  
print("============================")