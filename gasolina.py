
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê os dados do arquivo CSV para um DataFrame
df = pd.read_csv('gasolina.csv')

# Define o estilo visual do Seaborn
sns.set_style("whitegrid")

# Cria o gráfico de linha com Seaborn
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
sns.lineplot(x='dia', y='venda', data=df, marker='o')  # Cria o gráfico de linha com marcadores circulares
plt.title('Preço da Gasolina por Dia', fontsize=14)  # Define o título do gráfico
plt.xlabel('Dia', fontsize=12)  # Define o rótulo do eixo x
plt.ylabel('Preço (R$)', fontsize=12)  # Define o rótulo do eixo y

# Ajusta o layout para evitar sobreposição de elementos
plt.tight_layout()

# Salva o gráfico como uma imagem PNG
plt.savefig('gasolina.png')

# Mostra o gráfico na tela
plt.show()
