import numpy as np
import matplotlib.pyplot as plt
a=50
print (a)

#y=x^2
eps=1e-6
tmp=a
list_tmp=[]
learning_rate=1e-3
for i in range(0,10000):
    f_p=np.power(tmp+eps,3)
    f_m=np.power(tmp-eps,3)
    grad=(f_p-f_m)/(2*eps)
    tmp=tmp-learning_rate*grad
    list_tmp.append(tmp)
print(list_tmp)
plt.plot(list_tmp,np.square(list_tmp))
plt.show()
