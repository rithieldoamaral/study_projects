# Importar Bibliotecas
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Importar Base de Dados
doenca = pd.read_csv('dados_com_doencas.csv')

# Criar Subconjunto/treino e Teste
X = doenca.drop(columns=['Doença'])
y = doenca['Doença']
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.05)

# Criar Modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_treino, y_treino)

# Nomear as características
nomes_caracteristicas = X.columns

# Fazer previsões
previsao = modelo.predict(X_teste)

#Medir e Melhorar
Medir=accuracy_score(y_teste,previsao)
Medir

# Fazer previsão para uma nova instância
nova_instancia = [[22, 1]]
previsao2 = modelo.predict(nova_instancia)

print("Previsão para a nova instância:", previsao2)
