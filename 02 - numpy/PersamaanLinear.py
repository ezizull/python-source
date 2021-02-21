import numpy as np
print()

a = np.array([(2,3),(1,2)])
y = np.array([23,14])

print(a,'\n')
print(y,'\n')

aInv = np.linalg.inv(a)

# meyelesaikan persamman linear 
x = np.dot(aInv,y)
print(x,'\n')

# cara lain
x = np.linalg.solve(a,y)
print(x)

print()