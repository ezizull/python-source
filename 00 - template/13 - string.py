
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat STRING

'''
    1. dengan menggunakan single QUOTE '...'
    2. menggunakan double QUOTE "..."
'''

data =  'menggunakan single quote'
print(data)

data =  "menggunakan double quote"
print(data)

print('"Halo apa kabar?"')
print("'Halo apa kabar?'")
print("ini adalah hari jum'at")

# 2. Penggunaan tanda"
'''
    menggunakan tanda ' sebagai STRING
'''
print('mari kita sholat jum\'at') # print('mari kita sholat jum'at') jd ERROR
print('g\'day, isn\'t it?') # tanda \ tidak akan muncul

'''
    penggunaan tanda \ dlam STRING
'''
print("C:\\user\\saya") # kalo : print("C:\user\saya") jadi ERROR

'''
    menambah TAB dlam STRING
'''
print("ini di\t\tTAB") # kalo : print("ini di   TAB") tdk akan muncul

'''
    menambah BACKSPACE dlam STRING
'''
print("tanpa \bBACKSPACE") # bisa juga print("tanpaBACKSPACE")

'''
    menambah NEWLINE
'''
print("baris awal \nBARIS BARU") # kalo "\n" diganti ENTER tdk akan muncul
print("baris awal \rBARIS BARU") # jdi BARIS BARU
print("baris awal \r\nBARIS BARU") # sama yg pertama

# 3. STRING literal atau raw
'''
    menggunakan raw
'''
print(r'C:\new folder') # print('C:\\new folder') bisa capek klo banyak"
''' 
                MENGABAIKAN semua simbol CODING di STRING
'''


'''
    menggunakan multiline
'''
print("""
Nama   : Saya
Umur   : Berapa?
""")

# TERPRINT sesua yang TERCODING, tanpa tanda ( """ )

'''
    menggunakan multiline + raw
'''
print(r"""
Nama    : Saya
Umur    : Berapa?
Website : www.saya.com/cool
""")

# TERPRINT sesuai yang TERCODING + MENGABAIKAN semua simbol CODING di STRING