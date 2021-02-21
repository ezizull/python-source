import numpy as np
import pygame
import sys
import math
import tkinter as tk
from tkinter import messagebox

BG_PILIH = (244, 251, 255)
BG_COLOR = (255, 246, 108)
BG_TEMPAT = (245, 255, 244)
KOTAK_BIRU = (41, 255, 242)
KOTAK_MERAH = (249, 40, 40)
TXT_COLOR = (50, 80, 45)

SIZEKOTAK = 70

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

def desain_papan(papan):
    for c in range(COLOM_COUNT):
        for b in range(BARIS_COUNT):
            pygame.draw.rect(screen, BG_PILIH, (c*SIZEKOTAK, b, SIZEKOTAK, SIZEKOTAK-5))
            pygame.draw.rect(screen, BG_COLOR, (c*SIZEKOTAK, b*SIZEKOTAK+SIZEKOTAK, SIZEKOTAK, SIZEKOTAK))
            pygame.draw.rect(screen, BG_TEMPAT, (c*SIZEKOTAK+5,b*SIZEKOTAK+75, SIZEKOTAK-10, SIZEKOTAK-10))

    for c in range(COLOM_COUNT):
        for b in range(BARIS_COUNT):
            if papan[b][c] == 1:
                pygame.draw.rect(screen, KOTAK_BIRU, (c*SIZEKOTAK+5,height-(b*SIZEKOTAK+65), SIZEKOTAK-10, SIZEKOTAK-10))
            elif papan[b][c] == 2:
                pygame.draw.rect(screen, KOTAK_MERAH, (c*SIZEKOTAK+5,height-(b*SIZEKOTAK+65), SIZEKOTAK-10, SIZEKOTAK-10))
    pygame.display.update()

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    root.option_add('*Dialog.msg.font', 'Bahnschrift SemiCondensed 16')
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass



papan = buat_papan()
print("\n")
print_papan(papan)
satu = 0
dua = 0
babak = 1
gameOver = False
turn = 0

pygame.init()

width = COLOM_COUNT * SIZEKOTAK
height = (BARIS_COUNT+1) * SIZEKOTAK
size  = (width, height)

screen = pygame.display.set_mode(size)
desain_papan(papan)
pygame.display.update()

while  not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BG_PILIH, (0,0,width,SIZEKOTAK))
            posx = event.pos[0]-(SIZEKOTAK/2)
            if turn == 0:
                pygame.draw.rect(screen, KOTAK_BIRU, (posx,0,SIZEKOTAK,SIZEKOTAK))
            elif turn == 1:
                pygame.draw.rect(screen, KOTAK_MERAH, (posx,0,SIZEKOTAK,SIZEKOTAK))
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # input player 1
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SIZEKOTAK))
                turn += 1

                print("\n")
                if penempatan(papan , col):
                    baris = tambah_bulat(papan, col)
                    pilih_taroh(papan, baris, col, 1)
                print_papan(papan)
                print("\n")
                
                if pemenang_true(papan, 1):
                    satu += 1
                    gameOver = True

            # # input player 2
            elif turn > 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SIZEKOTAK))
                turn = 0

                if penempatan(papan , col):
                    baris = tambah_bulat(papan, col)
                    pilih_taroh(papan, baris, col, 2)
                print_papan(papan)
                
                if pemenang_true(papan, 2):
                    dua += 1
                    gameOver = True
            
            desain_papan(papan)

            if gameOver:
                if satu > 0:
                    message_box("Game Over","Selamat Player 1 Menang :)",)
                elif dua > 0:
                    message_box("Game Over","Selamat Player 2 Menang :)",)
                pygame.time.wait(2000)