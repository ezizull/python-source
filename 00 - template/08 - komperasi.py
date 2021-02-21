
a = 4
b = 2

print('')
print('====='*2,"lebih dari (>)")
hasil = a >3
print(a,'>',3,'=',hasil)
hasil = b >3
print(b,'>',3,'=',hasil)
hasil = b >2
print(b,'>',2,'=',hasil,"\n")

print('====='*2,"kurang dari (<)")
hasil = a <3
print(a,'<',3,'=',hasil)
hasil = b <3
print(b,'<',3,'=',hasil)
hasil = b <2
print(b,'<',2,'=',hasil,"\n")

print('====='*2,"lebih dari sama (>=)")
hasil = a >= 3
print(a,'>= ',3,'=',hasil)
hasil = b >= 3
print(b,'>= ',3,'=',hasil)
hasil = b >= 2
print(b,'>= ',2,'=',hasil,"\n")

print('====='*2,"lebih dari sama (<=)")
hasil = a <= 3
print(a,'<= ',3,'=',hasil)
hasil = b <= 3
print(b,'<= ',3,'=',hasil)
hasil = b <= 2
print(b,'<= ',2,'=',hasil,"\n")

print('====='*2,"sama dengan (==)")
hasil = a == 4
print(a,'== ',4,'=',hasil)
hasil = b == 4
print(b,'== ',4,'=',hasil,"\n")

print('====='*2,"tidak sama dengan (!=)")
hasil = a != 4
print(a,'!= ',4,'=',hasil)
hasil = b != 4
print(b,'!= ',4,'=',hasil,"\n")

x = 5
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)