print("")
angka = 0

while angka < 5:
    print(angka,'di dalam while')
    angka += 1
print('\t',angka,'.di luar while')

start = True
angka = 0
finish = 10

print("")
print("-----"*8)
print("")

while start:
    print('pencarian angka... di', angka)
    if angka is finish:
        start = False
        print("yossaa.. angka",angka,"ditemukan")
    angka += 1

print("")
# # LIFO (Last In First Out) queue

# import queue
    
# print ('\nLIFO (Last In First Out) Queue')

# q = queue.LifoQueue()

# for item in range(5):
#     q.put(item) # put item in queue
    
# # Alternative way of emptying queue

# while not q.empty():
#     x = q.get() # put item in queue
#     print (x, end = ' ')
