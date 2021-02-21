import numpy as np
print()

a = np.array([(1,-1),(1,1)])
print(a,'\n')

# inverse matrix
aInv = np.linalg.inv(a)
print(aInv,'\n')
print(np.dot(a,aInv),'\n')

# determinan matrix
detA = np.linalg.det(a)
print(detA)
detAinv = np.linalg.det(aInv)
print(detAinv)

print()