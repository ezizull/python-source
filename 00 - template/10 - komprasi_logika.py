# logika dan komperasi

# +++++3--------10+++++
'''
    kita akan membuat :
    angka KURANG dari 3 & LEBIH dari 10 = TRUE. yg diantara 3 & 10 = FALSE. 
'''

inputUser = float(input("\nmasukan angka, \nkurang dari 3\n     ato\nlebih dari 10\n= "))

# +++++3---------------
'''
    memeriksa angka kurang dari 3
'''

isKurangDari = (inputUser < 3)
print("kurang dari 3 =",isKurangDari)

# --------------10+++++
'''
    memeriksa angka lebih dari 10
'''

isLebihDari = (inputUser > 10)
print("lebih dari 10 =",isLebihDari)


# +++++3--------10+++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan :", isCorrect,"\n")

print("====="*6,"\n")

# -----3++++++++10-----
inputUser = float(input("masukan angka,\nlebih dari 3\n     ato\nkurang dari 10\n= "))

isLebihDari = (inputUser > 3)
print("lebih dari 3    =",isLebihDari)

isKurangDari = (inputUser < 10)
print("kurang dari 10 =",isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan :", isCorrect,"\n")