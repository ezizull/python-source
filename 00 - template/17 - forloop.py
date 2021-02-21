# list sebagai iterable
# gorengan = ['bakwan','cireng','panada','tahu','molen','ubi']

# for g in gorengan:
#     print(g)
#     print(len(g))

# # string sebagai iterable
# bakwan = 'bakwan'

# for i in bakwan:
#     print(i)

# for di dalan for
print("")
gorengan = ['bakwan','cireng','panada','tahu','molen','ubi',]
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','tomat','kentang','wortel']

daftar_belanja = [gorengan,buah,sayur]

print("",gorengan,"\n",buah,"\n",sayur)

print("")

print("====="*3,"masing\" semua yang di box","====="*3)

for subdaftarbelanja in daftar_belanja:
    print("\n",subdaftarbelanja,"\n")
    for komponen in subdaftarbelanja:
        print(komponen)

print("")



