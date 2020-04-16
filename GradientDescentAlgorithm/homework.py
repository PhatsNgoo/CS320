import numpy as np
import matplotlib.pyplot as plt


#parabol equation y=ax**2+b
data=np.random.rand(3,1000)
data[0]=data[0]*10-5
data[1]=data[0]**2+data[2]

plt.plot(data[0],data[1],'.')
plt.show()

#linear equation y=ax+b
data=np.random.rand(3,1000)
data[0]=data[0]*10
data[1]=data[0]

plt.plot(data[0],data[1],'.')
plt.show()
