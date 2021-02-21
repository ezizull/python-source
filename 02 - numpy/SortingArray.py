import numpy as np

'''
    Sorting Default
'''

# a= np.floor(np.random.randn(2,2)*10)

# print('default nilai a:')
# print(a)
# print('nilai max a = ',a.max())
# print('posisi max a = ',a.argmax())
# print('nilai min a = ',a.min())
# print('posisi min a = ',a.argmin())

# print('\nurutan nilai a: ')
# print(np.sort(a))
# print(np.argsort(a))

'''
    Sorting
'''

dtipe = [('nama','S10'),('tinggi',int)]
data = [
    ('Badak', 150),
    ('Cicak', 160),
    ('Angsa', 170)
]

a = np.array(data, dtype = dtipe)
print('Default Display:\n',a,'\n')
print('Sort Tinggi Display:\n',np.sort(a, order='tinggi'))
print('\nSort Nama Display:\n',np.sort(a, order='nama'))

print()