import pandas as pd
import random

# Lista de doenças fictícias
doencas_crianca = ['Resfriado', 'Gripe', 'Alergia']
doencas_adulto = ['Hipertensão', 'Diabetes', 'Enxaqueca']
doencas_idoso = ['Hipertensão', 'Diabetes', 'Câncer']

# Criar dados fictícios
dados = {'Idade': [random.randint(1, 5) for _ in range(200)] +  # Crianças (1-5 anos)
                  [random.randint(6, 17) for _ in range(300)] +  # Adolescentes (6-17 anos)
                  [random.randint(18, 64) for _ in range(300)] +  # Adultos (18-64 anos)
                  [random.randint(65, 100) for _ in range(200)],  # Idosos (65+ anos)
         'Gênero': [random.choice([1, 2]) for _ in range(1000)],
         'Doença': []}

# Preencher a coluna de doenças com base na idade
for idade in dados['Idade']:
    if 1 <= idade <= 5:
        dados['Doença'].append(random.choice(doencas_crianca))
    elif 6 <= idade <= 17:
        dados['Doença'].append(random.choice(doencas_adulto))
    elif 18 <= idade <= 64:
        dados['Doença'].append(random.choice(doencas_adulto))
    else:
        dados['Doença'].append(random.choice(doencas_idoso))

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar DataFrame como CSV
df.to_csv('dados_com_doencas.csv', index=False)
