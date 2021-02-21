import numpy as np

print()

a = np.array((
            [1,2,3],
            [4,5,6]
            ))

print('matrix a dengan ukuran:',a.shape)
print(a)
print()

# Transpose Matrix
'''
    transpose matrix a:
    [[1 4]
     [2 5]
     [3 6]]

'''
print('transpose matrix a:')
print(a.transpose())
print('-----'*2)
print(np.transpose(a))
print('-----'*2)
print(a.T)
print()

# Flatten Array, Vector Baris
print('flatten matrix a:')
print(a.ravel())
print('-----'*3)
print(np.ravel(a))
print('-----'*3)
print()

# Reshape Matrix 
'''
    reshape matrix a:
    [[1 2]
     [3 4]
     [5 6]]

'''
print('reshape matrix a:')
print(a.reshape(3,2))
print()

# Resize Matrix = Mengubah "a" 
print('resize matrix a:')
print(a.resize(3,2))
print('matrix a dengan ukuran:',a.shape)
print(a)

print()