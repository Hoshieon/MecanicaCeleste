
# coding: utf-8

# In[1]:


#programa para determinar elementos orbitales del planeta asumiendo elipse instantánea en ese punto

from numpy import *
from astropy import 

print("A continuación escriba las componentes del vector posición de m2 en coordenadas heliocéntricas eclípticas")

x=float(input("x"))
y=float(input("y"))
z=float(input("z"))


# In[ ]:


print("Ahora escriba las componentes del vector velocidad ")
vx=float(input("vx"))
vy=float(input("vy"))
vz=float(input("vz"))


# In[ ]:


r = (x**2+y**2+z**2)**(0.5)
print("El vector r es {:.8f}.format(r)")
v = (vx**2+vy**2+vz**2)**(0.5)
print("El vector v es {:.8f}.format(v)")


# In[5]:


m1=float(input("m1"))
m2=float(input("m2"))
mr=(m2/m1)
print("La razon entre la masa 2 y la masa 1 es{:f}".format(mr))

