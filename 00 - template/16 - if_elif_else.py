
print("")

nilai1 = input("masukan nilai matkul A : ") 
nilai2 = input("masukan nilai matkul B : ")

print("\n===== yang dilihat siswa =====\n")

print("matkul 1 = ",nilai1)
print("matkul 2 = ",nilai2)

nilai = (float(nilai1)+float(nilai2))/2

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah T, lakukan perbaikan!")
else:
    print("maaf anda tidak lulus mata kuliah ini!")


print("\n===== OPERATOR LOGIKA & STRING =====")

gorengan=["bakwan","cireng","konto'","panada","siomay","risoles","molen","papeda"]
print("""
menu : 
. bakwan   . konto'
. cireng   . panada
. siomay   . risoles
. molen    . papeda
""")
beli = input("mau pesan apa? : ")

if beli in gorengan:
    print('" ya saya jual',beli,'"')

if not beli in gorengan:
    print('" saya nggak jual',beli,'"')

print("\nmasukan 1 huruf dari ", beli)
karakter = input("(untuk menangkan hadiah) : ")
if karakter in beli:
    print("\nselamat, ada!",karakter,"di",beli)
else:
    print("\nyahh, tidak ada!",karakter,"di",beli)

print(" ")
