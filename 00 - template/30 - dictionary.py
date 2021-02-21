list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}

print(type(list))
print(type(tuple))
print(type(set))

# dictionary = membuat kamus

member1 = {"ID":101,
           "Nama":"faqihza mukhlish",
           "pekerjaan":"mahasiswa",
           "status member":"gold"}

member2 = {"ID":102,
           "Nama":"Ujang pintu",
           "pekerjaan":"reparasi pintu",
           "status member":"berlian"}

memberlist = {101:member1,102:member2}

print(memberlist[101])
print(memberlist.keys())
print(memberlist.values())
