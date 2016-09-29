
# coding: utf-8

# In[52]:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-25, 25)
y = np.e

def s(x, y):
    return (1/np.sqrt(1+y**-x))

plt.plot(x, s(x,y),'b')

plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title('FUNSION SIGMOIDAL')
plt.grid(True)


# In[47]:

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,120)
w=15
y=60
z=100

def f(x,w,y,z):
    if ((x<w) | (x>=y)):
        ans=0
    if ((w<=x) & (x<y)):
         ans=(x-w)
    if ((y<=x) & (x<=z)):
        ans=z-x
    return ans

f_vec = np.vectorize(f)
func=f_vec(x,w,y,z)
plt.plot(x,f_vec(x,w,y,z)) 

plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title('FUNCION TRIANGULAR')
plt.grid(True)
plt.show()


# In[ ]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-15,15)
a=np.linspace(0,5)
b=np.linspace(0,7)

def escala(x, a, b):
    return np.piecewise(x, [x < a ],if [a <= x <= b], if[x > b])
plt.plot(x, escala(x, a, b ), 'y')
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title('FUNCION HOMBRO')
plt.grid(True)


# In[ ]:



