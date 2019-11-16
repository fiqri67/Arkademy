
def jumlah_kata():
    masukan_kata = input('Masukan Kata: ') #inputan kata
    jadikan_list = masukan_kata.split()
    hitung_kata = len(jadikan_list)
    hitung_string=0
    for i in jadikan_list:
        #proses merubah angka tipe data str menjadi int
      try:
          int(i)

      except:
          #jika sudah dicek apakah kata tersisa termasuk string jika iya hitung_string +1
          if isinstance(i,str):
              hitung_string+=1

    print (hitung_string,"/",hitung_kata)




jumlah_kata()