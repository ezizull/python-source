import numpy as np
import matplotlib.pyplot as plt

# print(plt.style.available)
plt.style.use('fivethirtyeight')

pi = np.pi
sudut = np.linspace(0,2*pi,100)
radius = 5;

x = radius + np.cos(sudut)
y = radius + np.sin(sudut)

plt.plot(x,y, color='#503143', linewidth=1, marker='.', label='kejadian')
plt.title('Lingkaran Kehidupan', size=10)

plt.legend(loc=2, prop={'size':10})

plt.grid(True)

plt.tight_layout()

plt.show()
