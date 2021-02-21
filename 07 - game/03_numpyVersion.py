import numpy as np

BARIS_COUNT = 6
COLOM_COUNT = 7

def buat_papan():
    papan = np.zeros((BARIS_COUNT,COLOM_COUNT))
    return papan

def pilih_taroh(papan, baris, col, bulat):
    papan[baris][col] = bulat

def penempatan(papan, col):
    return papan[BARIS_COUNT-1][col] == 0

def tambah_bulat(papan, col):
    for b in range(BARIS_COUNT):
        if papan[b][col] == 0:
            return b

def print_papan(papan):
    print(np.flip(papan, 0))

def pemenang_true(papan, bulat):
    # check horizontal
    for c in range(COLOM_COUNT-3):
        for b in range(BARIS_COUNT):
            if papan[b][c] == bulat and papan[b][c+1] == bulat and papan[b][c+2] == bulat and papan[b][c+3] == bulat:
                return True

    # check vertical
    for c in range(COLOM_COUNT):
       for b in range(BARIS_COUNT-2):
           if papan[b][c] == bulat and papan[b+1][c] == bulat and papan[b+2][c] == bulat and papan[b+3][c] == bulat:
               return True

    # check miring kanan
    for c in range(COLOM_COUNT-3):
       for b in range(BARIS_COUNT-2):
           if papan[b][c] == bulat and papan[b+1][c+1] == bulat and papan[b+2][c+2] == bulat and papan[b+3][c+3] == bulat:
               return True

    # check miring kiri
    for c in range(COLOM_COUNT-3):
       for b in range(2, BARIS_COUNT):
           if papan[b][c] == bulat and papan[b-1][c+1] == bulat and papan[b-2][c+2] == bulat and papan[b-3][c+3] == bulat:
               return True


papan = buat_papan()
print("\n")
print_papan(papan)
babak = 1
turn = 0

while  babak > 0:
    print("\nturns: ", babak)
    # input player 1
    if turn == 0 and babak < 22:
        col = int(input("\t| Player 1: "))
        turn += 1
        print("\n")

        if penempatan(papan , col):
            baris = tambah_bulat(papan, col)
            pilih_taroh(papan, baris, col, 1)
        print_papan(papan)
        print("\n")
        
        if pemenang_true(papan, 1):
            print("\t| selamat Player 1 menang :)")
            babak = 22

    # # input player 2
    if turn > 0 and babak < 22:
        col = int(input("\t| Player 2: "))
        turn = 0
        print("\n")

        if penempatan(papan , col):
            baris = tambah_bulat(papan, col)
            pilih_taroh(papan, baris, col, 2)
        print_papan(papan)
        print("\n")
        
        if pemenang_true(papan, 2):
            print("\t| selamat Player 2 menang :)")
            babak = 22

    babak += 1