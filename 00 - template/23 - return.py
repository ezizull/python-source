# fungsi dgn return value

print("")

def kuadrat(argument):
    total = argument**2
    print('nilai kuadrat dari',argument,'adalah : ',total)
    return total

a = kuadrat(3)

print('\n','====='*3,'batas','====='*3,'\n')

# fungsi dgn return value & multiple argumen

def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return [total,2,3,4]

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total

a = tambah (3,4)
b = kali (3,4)
print(a)
print(b)
print("")