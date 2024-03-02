from scipy import signal
import matplotlib.pyplot as plt
import numpy as np 

w=float(input('ingrese la frecuencia natural: '))
k=float(input('ingrese ganacía del sistema: '))
s=float(input('ingrese coeficiente de amortiguamiento: '))
n=k*(w**2)
a=1
b=2*s*w
c=w**2

print('ganacia total: ',n)
print('primer polo: ',a) 
print('segundo polo: ',b)
print(c)

   
if 0<s<1:
   sistema='Subamortiguado'
elif s==1:
      sistema='Criticamente Amortiguado'
elif s>1: 
        sistema='Sobreamortiguado'
else:
    sistema='inestable'

print('El sistema es:' ,sistema)


t= np.linspace (0,20,1000)
num= [n]
den=[a,b,c]
tout, yout = signal.step ((num,den), T=t)
plt.plot (tout, yout)
plt.title('Respuesta en dominio tiempo')
plt.xlabel('Tiempo')
plt.ylabel ('Respuesta')
plt.grid()
plt.show()