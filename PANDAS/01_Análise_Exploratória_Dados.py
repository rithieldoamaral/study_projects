## Análise Exploratória
# Importar as bibliotecas
import pandas as pd
import matplot.pyplot as plt
plt.style.use("seaborn")

# Upload do arquivo
from google.colab import files
arq = files.upload()

# Criar nosso DataFrame
df = pd.read_excel("AdventureWorkds.xlsx")

# Visualizar as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape()

# Verificar os tipos de dados
df.dtypes

# Qual foi a Receita Total?
df["Valor Venda".sum()

# Qual o Custo Total por produto?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando uma coluna de custo

# Qual o custo total?
round(df["custo"].sum(), 2)

# Agora que temos a receita e custo e o total, podemos achar o lucro total
# Vamos criar uma coluna de lucro que será Receita - Custo
df["lucro"] = df["Valor Venda"] - df["custo"]
df.head()

# Total lucro
round(df["lucro"].sum(),2)

# Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] - df["Data Envio"] - df["Data Venda"]
df.head()

## Agora, queremos saber a média do tempo de envio para cada Marca, e para isso precisamos transformar a coluna Tempo_envio em númerica
# Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
df.head()

# Verificar o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype

# Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

# Missing Values
#Verificando se temos dados faltantes
df.isnull().sum()

E, se a gente saber o Lucro por Ano e Por Marca?
# Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()
pd.options.display.float_format = '(:20,.2f)'.format

# Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

# Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

# Lucro por ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

# Lucro por ano em números
df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

# Selecionar apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
df2009.head()

# Gráfico de linhas do lucro por mês
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

# Gráfico do lucro por marca
df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');
** legenda eixo x na horizontal

# Gráfico do lucro por classe
df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

# Análise estatística
df["Tempo_envio"].describe()

# Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);

# Histograma
plt.hist(df["Tempo_envio]);

# Tempo mínimo de envio
df["Tempo_envio].min()

# Tempo máximo de envio
df["Tempo_envio"].max()

# Identificar o outlier
df[df["Tempo_envio"] == 20]

# Salvar em um novo csv
df.to_csv("df_vendas_novo.csv", index=False)
