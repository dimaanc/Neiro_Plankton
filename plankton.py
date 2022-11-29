import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sigma1 = 0.25
sigma2 = 0.003
eps1 = 0.025
eps2 = 0.025
eps3 = 0.2
C0 = 80
C1 = 40
C = 140
ksi=1
x = np.linspace(-140, 0, 100)
t = np.linspace(0, 1, 100)
fig = plt.subplots()

E = lambda x: sigma1 * (np.tanh(eps1 * x + C1) + 1)
S = lambda x: sigma2 * ((np.tahn*(eps2 * x + C1) + 1
S = lambda t: np.cos(2*np.pi*t) + 1
G = lambda x: ksi * np.cosh * eps3(x+C0)
plt.plot(x, G(x))
plt.plot(t, S(t))
plt.plot(x, E(x))
plt.plot(x, S(x))
plt.show()


