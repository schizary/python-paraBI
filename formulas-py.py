import pandas as pd

# O Power BI envia a tabela atual para a variável 'dataset'
df = dataset.copy()

# Cálculos
media = df["Valor"].mean()
mediana = df["Valor"].median()
moda = df["Valor"].mode()[0]   # pega a primeira moda
desvio = df["Valor"].std()

# Retorna uma tabela resumo
resultado = pd.DataFrame({
    "Média": [media],
    "Mediana": [mediana],
    "Moda": [moda],
    "Desvio Padrão": [desvio]
})

resultado


# Se você quiser que cada linha da tabela de vendas mostre os mesmos valores estatísticos:

import pandas as pd

df = dataset.copy()

df["Média"] = df["Valor"].mean()
df["Mediana"] = df["Valor"].median()
df["Moda"] = df["Valor"].mode()[0]
df["Desvio Padrão"] = df["Valor"].std()

df


#---- se os dados forem CSV -------

import pandas as pd

# Lendo o CSV
df = pd.read_csv(r"C:\Users\SeuUsuario\Documents\vendas.csv")

# Cálculos estatísticos
media = df["Valor"].mean()
mediana = df["Valor"].median()
moda = df["Valor"].mode()[0]
desvio = df["Valor"].std()

# Retorna resumo
resultado = pd.DataFrame({
    "Média": [media],
    "Mediana": [mediana],
    "Moda": [moda],
    "Desvio Padrão": [desvio]
})

resultado




# LISTA AS COLUNAS 

import pandas as pd

df = dataset.copy()

print(df.columns.tolist())  # lista os nomes das colunas exatamente como o Python recebeu
df.head()



# EXEMPLO COM COLUNAS 


import pandas as pd

df = dataset.copy()

media_qtd = df["Qtd. Vendida"].mean()
mediana_qtd = df["Qtd. Vendida"].median()
moda_qtd = df["Qtd. Vendida"].mode()[0]
desvio_qtd = df["Qtd. Vendida"].std()

resultado = pd.DataFrame({
    "Média Qtd. Vendida": [media_qtd],
    "Mediana Qtd. Vendida": [mediana_qtd],
    "Moda Qtd. Vendida": [moda_qtd],
    "Desvio Padrão Qtd. Vendida": [desvio_qtd]
})

resultado
