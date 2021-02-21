# OPERASI LOGIKA ato BOOLEAN

# NOT , OR , AND , XOR

# NOT
'''
    akan selalu KEBALIKAN
'''
print("==== NOT ====")
a = False
c = not a 
print('data a =',a)
print('---- NOT ----')
print('data c =' , c)

# OR : seperti pertambahan TRUE = 1 , FALSE = 0
'''
    akan TRUE jika ada yang TRUE
'''
print("==== OR ====")
a = True
b = True
c = a or b 
print(a,' OR',b,' =',c)
a = False
b = False
c = a or b 
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b 
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b 
print(a,' OR',b,'=',c)

# AND : seperti perkalian TRUE = 1 , FALSE = 0
'''
    akan TRUE kalo keduanya TRUE
'''
print("==== AND ====")
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)

# XOR
'''
    akan TRUE jika keduanya BERBEDA
'''
print("==== XOR ====")
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)