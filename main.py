import pandas as pd
import matplotlib.pyplot as plt

# Dados dos eventos de vacinação
data = {
    'Bairro': ['Gleba E', 'Jardim Limoeiro', 'Lama Preta', 'Piaçaveira'],
    'Data': ['2024-05-19', '2024-06-09', '2024-07-07', '2024-07-21'],
    'Vacinas Aplicadas': [250, 190, 230, 200],
    'Vermifugações Aplicadas': [29, 50, 80, 40]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Visualização dos dados
print(df)

# Cálculo do total de vacinas e vermifugações aplicadas
df['Total Aplicações'] = df['Vacinas Aplicadas'] + df['Vermifugações Aplicadas']
total_aplicacoes = df['Total Aplicações'].sum()

# Média de vacinas e vermifugações por bairro
media_aplicacoes = df[['Vacinas Aplicadas', 'Vermifugações Aplicadas']].mean()

# Proporção em relação à população total de Camaçari-BA
populacao_total = 319394
proporcao = (total_aplicacoes / populacao_total) * 100

# resultados
print(f"Total de aplicações: {total_aplicacoes}")
print(f"Média de vacinas por bairro: {media_aplicacoes['Vacinas Aplicadas']:.2f}")
print(f"Média de vermifugações por bairro: {media_aplicacoes['Vermifugações Aplicadas']:.2f}")
print(f"Proporção de pets atendidos em relação à população total: {proporcao:.2f}%")


# Gráfico de barras para distribuição de vacinas e vermifugações
df.plot(x='Bairro', y=['Vacinas Aplicadas', 'Vermifugações Aplicadas'], kind='bar', figsize=(10, 6))
plt.title('Distribuição de Vacinas e Vermifugações por Bairro')
plt.xlabel('Bairro')
plt.ylabel('Número de Aplicações')
plt.show()

# Gráfico de pizza para proporção de aplicações por bairro
df.set_index('Bairro')['Total Aplicações'].plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
plt.title('Proporção de Aplicações por Bairro')
plt.ylabel('')
plt.show()