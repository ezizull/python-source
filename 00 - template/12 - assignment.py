# operator assignment

'''
    operasi yg bisa dilakukan dengan penyingkatan / operasi yg + assignment
'''

a = 5 # ini adalah assignment
print('nilai a = ', a)

a += 1 # Artinya "a = a + 1"
print('nilai a +=1, menjadi a = ', a)

a -= 2 # Artinya "a = a - 2"
print('nilai a -=2, menjadi a = ', a)


a *= 5 # Artinya "a = a * 5"
print('nilai a *=5, menjadi a = ', a)

a /= 2 # Artinya "a = a / 2"
print('nilai a /=2, menjadi a = ', a)

b = 10
print("\nnilai b=",b)

# MODULUS & FLOOR DIVISON
b %= 3
print('nilai b %=3, menjadi b = ', b)

b = 10
print("\nnilai b=",b)

b //= 3
print('nilai b //=3, menjadi b = ', b)

# PANGKAT / EXPONEN
a = 5
print('\nnilai a = ', a)

a **= 3
print('nilai a **=3, menjadi a = ', a)

# operasi bitewise

'''
    OR ( | )
'''
c = True
print('\nnilai c =', c)
c |= False
print('nilai c |= False, menjadi c = ', c)

c = False
print('\nnilai c =', c)
c |= False
print('nilai c |= False, menjadi c = ', c)

'''
    AND ( & )
'''
c = True
print('\nnilai c =', c)
c &= False
print('nilai c &= False, menjadi c = ', c)

c = True
print('\nnilai c =', c)
c &= True
print('nilai c &= False, menjadi c = ', c)

'''
    XOR ( ^ )
'''
c = True
print('\nnilai c =', c)
c ^= False
print('nilai c ^= False, menjadi c = ', c)

c = True
print('\nnilai c =', c)
c ^= True
print('nilai c ^= False, menjadi c = ', c)

# shift / geser geser

d = 0b0100
print('\nnilai d = ', format(d,'04b'))
d >>= 2
print('nilai d >>= 2, menjadi d = ', format(d,'04b'))
d <<= 1
print('nilai d <<= 1, menjadi d = ', format(d,'04b'))