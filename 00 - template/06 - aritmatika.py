# operasi aritmatika

a = 10
b = 3

# operasi TAMBAH +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi KURANG -
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi KALI *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi BAGI /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi EKSPONEN (PANGKAT) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi MODULUS %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi FLOOR DEVISION //
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, oprational precedence

x = 3
y = 2
z = 4

'''
    1. (Tanda Kurung)   ()
    2. Exponen          **
    3. Kali & Bagi      * , / , % , //
    4. Tambah & Kurang  + , -
'''

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# kurung mengambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)