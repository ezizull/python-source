# 1.----- 0 +++++ 5 ----- 8 +++++ 11 ----- 

inputUser = float(input("masukkan angka\nlebih dari 0\n--- & ---\nkurang dari 5\n--- ATO ---\nlebih dari 8\n--- & ---\nkurang dari 11\n= "))

isLebihDari_A = (inputUser > 0)
print("angka lebih dari 0 =",isLebihDari_A)

isKurangDari_B = (inputUser < 5)
print("angka Kurang dari 5 =",isKurangDari_B)

isLebihDari_C = (inputUser > 8)
print("angka lebih dari 8 =",isLebihDari_C)

isKurangDari_D = (inputUser < 11)
print("angka Kurang dari 11 =",isKurangDari_D)

isCorrect = (isLebihDari_A and isKurangDari_B) or (isLebihDari_C and isKurangDari_D)
print("angka yang anda masukkan =", isCorrect)

print("\n")

# 1.+++++ 0 ----- 5 +++++ 8 ----- 11 +++++ 

inputUser = float(input("masukkan angka\nkurang dari 0\n--- & ---\nlebih dari 5\n--- ATO ---\nkurang dari 8\n--- & ---\nlebih dari 11\n= "))

isLebihDari_A = (inputUser < 0)
print("angka lebih dari 0 =",isLebihDari_A)

isKurangDari_B = (inputUser > 5)
print("angka Kurang dari 5 =",isKurangDari_B)

isLebihDari_C = (inputUser < 8)
print("angka lebih dari 8 =",isLebihDari_C)

isKurangDari_D = (inputUser > 11)
print("angka Kurang dari 11 =",isKurangDari_D)

isCorrect = (isLebihDari_A or isKurangDari_B) and (isLebihDari_C or isKurangDari_D)
print("angka yang anda masukkan =", isCorrect)

print("\n")


# CHEAT : ----- 0 +++++ 5 ----- 8 +++++ 11 ----- 
x = float(input("masukkan angka\nlebih dari 0\n--- & ---\nkurang dari 5\n--- ATO ---\nlebih dari 8\n--- & ---\nkurang dari 11\n= "))
if (x > 0 and x < 5) or (x > 8 and x < 11):
    print(True)
else:
    print(False)

print("\n")


# CHEAT : +++++ 0 ----- 5 +++++ 8 ----- 11 +++++ 
x = float(input("masukkan angka\nkurang dari 0\n--- & ---\nlebih dari 5\n--- ATO ---\nkurang dari 8\n--- & ---\nlebih dari 11\n= "))
if (x < 0 or x > 5) and (x < 8 or x > 11):
    print(True)
else:
    print(False)