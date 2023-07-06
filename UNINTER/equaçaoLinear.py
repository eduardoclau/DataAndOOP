import matplotlib.pyplot as plt
import numpy as np

# Três primeiros números do RU

num1 = 3
num2 = 9
num3 = 7

# Substituir zeros por 5

if num1 == 0:
    num1 = 5
if num2 == 0:
    num2 = 5
if num3 == 0:
    num3 = 5

# Criar vetor aleatório de tamanho 10 para os valores de x

x = np.random.rand(10)

# Calcular os valores de y para cada x

y = num1 * x + num2 * x - num3

# Plotar os pontos no gráfico

plt.scatter(x, y, c='red', label='Equação Linear')

# Configurar os eixos e a legenda do gráfico

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

# Exibir o gráfico

plt.show()
