#
# CODE MADE BY NESTOR ESPINOZA (nsespino@uc.cl)
#
# You are free to do whatever you want with it as 
# long as you credit my work :-).
#

import numpy as np
import pyfits
from scipy.optimize import curve_fit
from matplotlib.pyplot import plot,show

def curva(x,a,T):
    h = 6.62e-34
    c = 3e8
    k = 1.38e-23
    return (1e-11*h*(c**2)*a)/(((x*1e-10)**5)*(np.exp((h*c)/((x*1e-10)*k*T))-1.0))

# Extraemos los datos...
data = pyfits.getdata('/home/nespinoza/Downloads/spec-1594-52992-0153.fits') 
flujo = data.field('flux')
long_de_onda = 10**(data.field('loglam'))
# Fiteamos la curva:
coef,coef_cov = curve_fit(curva,long_de_onda.astype('float64'),flujo.astype('float64'),p0=[1.0,6000.0])
# Imprimimos la temperatura:
print '------------------------------------------------------------------'
print 'Temperatura ajustada: ',coef[1],'+-',np.sqrt(coef_cov[1,1]),' K'
print '------------------------------------------------------------------'
# Dibujamos el espectro fitteado:
plot(long_de_onda,flujo,color = 'blue')
plot(long_de_onda,curva(long_de_onda,coef[0],coef[1]),color = 'black')
show()
