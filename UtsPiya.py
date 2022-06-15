#kasir sederhana toko buah
print(35*'=')
print("Welcome di frutifut")
print(35*'=')
class Daftar:
    def Menu ():
        print("""Daftar Buah perkilo\n
    1. apple   = 40000 
    2. banana  = 13000
    3. cherry  = 20000
    4. alpukat = 30000
    5. melon   = 25000
    """)
    Menu()
print(35*'=')
pilih = int(input("Masukan kode buah :"))
if pilih == 1:
        print("buah apple 1kg seharga 40000")
        jml = int(input("berapa kilo buah yang dibeli :"))
        print(35*'=')
        total = jml*40000
        print("total pembayaran :",total)
        print(35*'=')
        print("Terimakasih sudah berbelanja disini")
elif pilih == 2:
        print("buah banana 1kg seharga 13000")
        jml = int(input("berapa kilo buah yang dibeli :"))
        print(35*'=')
        total = jml*13000
        print("total pembayaran :",total)
        print(35*'=')
        print("Terimakasih sudah berbelanja disini")
elif pilih == 3:
        print("buah cherry  1kg seharga 20000")
        jml = int(input("berapa kilo buah yang dibeli :"))
        print(35*'=')
        total = jml*20000
        print("total pembayaran :",total)
        print(35*'=')
        print("Terimakasih sudah berbelanja disini")
elif pilih == 4:
        print("buah alpukat 1kg seharga 30000")
        jml = int(input("berapa kilo buah yang dibeli :"))
        print(35*'=')
        total = jml*430000
        print("total pembayaran :",total)
        print(35*'=')
        print("Terimakasih sudah berbelanja disini")
elif pilih == 5:
        print("buah melo 1kg seharga 25000")
        jml = int(input("berapa kilo buah yang dibeli :"))
        print(35*'=')
        total = jml*25000
        print("total pembayaran :",total)
        print(35*'=')
        print("Terimakasih sudah berbelanja disini")
else:
    pass
#Sekian