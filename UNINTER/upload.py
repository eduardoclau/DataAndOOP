import matplotlib.pyplot as plt
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('STORES.csv')

# Renomear as colunas
df = df.rename(columns={
    'Items_Available': 'Itens',
    'Daily_Customer_Count': 'Visitantes',
    'Store_Sales': 'Vendas'
})

# Calcular os valores estatísticos
min_items = df['Itens'].min()
max_items = df['Itens'].max()
mean_items = df['Itens'].mean()
std_items = df['Itens'].std()

min_visitantes = df['Visitantes'].min()
max_visitantes = df['Visitantes'].max()
mean_visitantes = df['Visitantes'].mean()
std_visitantes = df['Visitantes'].std()

min_vendas = df['Vendas'].min()
max_vendas = df['Vendas'].max()
mean_vendas = df['Vendas'].mean()
std_vendas = df['Vendas'].std()

# Criar os gráficos
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.scatter(df.index, df['Itens'], color='blue')
plt.xlabel('Loja')
plt.ylabel('Itens')
plt.title('Itens Disponíveis')

plt.subplot(1, 3, 2)
plt.scatter(df.index, df['Visitantes'], color='red')
plt.xlabel('Loja')
plt.ylabel('Visitantes')
plt.title('Contagem Diária de Clientes')

plt.subplot(1, 3, 3)
plt.scatter(df.index, df['Vendas'], color='green')
plt.xlabel('Loja')
plt.ylabel('Vendas')
plt.title('Histórico de Vendas')

plt.tight_layout()

# Exibir os valores estatísticos
print('Valores Estatísticos:')
print('Itens: mínimo =', min_items, 'máximo =', max_items,
      'médio =', mean_items, 'desvio padrão =', std_items)
print('Visitantes: mínimo =', min_visitantes, 'máximo =', max_visitantes,
      'médio =', mean_visitantes, 'desvio padrão =', std_visitantes)
print('Vendas: mínimo =', min_vendas, 'máximo =', max_vendas,
      'médio =', mean_vendas, 'desvio padrão =', std_vendas)

# Exibir os gráficos
plt.show()
