
# while True:
#     try:
#         angka = int(input("\nmasukan angka: "))
#         break
#     except:
#         print("itu bukan angka pintar! -_- ")

# print("betul,",angka,"adalah angka 'v' ")

# print("")
print("\n\tprogram bembagian")
print("====="*7,"\n")

while True:
    try:
        penyebut = int(input("penyebut = "))
        pembilang = int(input("pembilang = "))
        hasil = penyebut/pembilang
        break
# DEFAULT
    # except Exception as err:
    #     print(err,"\n")
    except ValueError:
        print("ada yang bukan angka, mungkin impostor!\n")
    except ZeroDivisionError:
        print("karena 0, hasilnya tak hingga\n")

'''
    type" exception errors:
    1. IOError
    2. ImportError
    3. ValueError
    4. Division by zero
    5. KeyboardInterupted
    6. E0FError
'''

print("hasil pembagian adalah =",hasil,"\n")