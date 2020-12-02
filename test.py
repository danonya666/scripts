import scipy.integrate as integrate
import scipy.special as special
import numpy as np

# Constants
q = 1.602 * (10 ** (-19))
h = 6.626 * (10 ** (-34))
m0 = 9.109 * (10 ** (-31))

# Разрывы зон MIM
Xl = 3 * q
Xr = 3 * q
# Эффективная масса электронов и дырок
me = 0.5 * m0
mh = 0
# Толщина барьера
d = 2 * (10 ** (-9))
# Разрывы зон MIS
Xc = 0 * q
Xv = 0 * q
# Диэлектрическая проницаемость
diel = 0
# Ширина запрещенной зоны
Eg = 0 * q

MIMparams = [Xl, Xr, me, d]
MISparams = [Xc, Xv, me, mh, d, diel, Eg]

# IDK
E = 1 * q
Enorm = 1 * q
Em = 1.1 * q

# Fermi energy
Efl = 1 * q
Efr = 1 * q


# special.erf()

def Gauss():
    pnom = int(input())
    fluct = 0.01
    sigm = fluct * pnom


# подаем определенное напряжение
U = int(input())
T = np.exp((-4) * (np.sqrt(2 * me) * d) / (3 * q * U * h) * (((Xl - E + (m0 / me * Enorm)) ** (3 / 2)) -
                                                             ((Xl - E + m0 / me * Enorm - q * U) ** (3 / 2))))

print((integrate.quad(lambda E: 1, Efl, Efr)))
print(integrate.quad(lambda Enorm: T, 0, (Em - E)))
I = 4 * (np.pi) * q * m0 / (h ** 3) * (integrate.quad(lambda E: 1, Efl, Efr)[0]) * \
    (integrate.quad(lambda Enorm: T, 0, (Em - E))[0])

print(T)
print(I)