from collections import deque

print("\n\tRUMAH SAKIT KITA")

print("======"*5,"\n")

antrian = deque([])
tombol = int(input("masukan [no] antrian: "))

while tombol >= 1:
    
    while tombol >= 1:
        
        antrian.append(tombol)
        print('antrian masuk: ',tombol)
        print('antrian sekarang:',antrian)
        print("")
        tombol = int(input("masukan [no] antrian: "))
        
        if  tombol in antrian:
            print("nomor antrian",tombol,"sudah dipakai!")
            antrian.remove(tombol)
            print("")
            continue

        if  tombol > 4 in antrian:
            out = antrian.popleft()
            print('antrian keluar: ',out)
            print('antrian sekarang: ',antrian)
            print("")
            continue

print("")