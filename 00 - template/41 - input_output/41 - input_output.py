
'''
w = write / menghapus file lama 
r = read / hanya bisa baca
a = appending / menambahkan data di akhir baris
r+ = write and read
'''

# membuat file text
file = open("data.txt",'w')
file.write("data text buatan python")
file.write("\nkita di baris kedua jhon")

file.close()

# appending mode

file3 = open("data.txt",'a')

file3.write('\njos!! baris buatan append mode')
file.close()

# membaca file text
file2 = open("data.txt",'r')

print(file2.read())
#print(file2.read(20))
#print(file2.readline())

file2.close()
