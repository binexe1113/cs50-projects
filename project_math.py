import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Definir a função de ajuste
def linear(x, m, b):
    return m * x + b

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 2.8, 3.6, 4.5, 5.1])
sigma_y = np.array([0.1, 0.2, 0.1, 0.2, 0.1])  # Incertezas em y
sigma_x = np.array([0.1, 0.2, 0.1, 0.2, 0.1])  # Incertezas em x (não usados diretamente aqui)

# Ajuste ponderado
popt, pcov = curve_fit(linear, x, y, sigma=sigma_y)
m, b = popt
perr = np.sqrt(np.diag(pcov))

# Plotar os dados e a linha de tendência
plt.errorbar(x, y, yerr=sigma_y, fmt='o', label='Dados')
plt.plot(x, linear(x, *popt), 'r-', label='Ajuste Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

print(f"Coeficiente angular (m): {m:.2f} ± {perr[0]:.2f}")
print(f"Intercepto (b): {b:.2f} ± {perr[1]:.2f}")
