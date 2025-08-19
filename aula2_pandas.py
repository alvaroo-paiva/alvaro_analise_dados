import pandas as pd
df = pd.read_csv("C:\\Users\\Álvaro Paiva\\Documents\\analiseDados\\dados\\imoveis_brasil.csv")
df.shape
df.columns
df.head(5)
df.tail(5)
df.sample(5)
df.info()
#Verificar os tipos de Imoveis
df["Tipo_Imovel"].unique()
#Imoveis com valor maiores que 1M
filtro = df["Valor_Imovel"] > 1000000
df_1m = df.loc[filtro]
#Selecionar cidade, bairro e valor e gravar no df2
colunas_selecionadas = ["Cidade","Bairro","Tipo_Imovel"]
df2 = df[colunas_selecionadas]
#Ordenar os valores dos imoveis mais caros
df.sort_values(["Valor_Imovel"], ascending=False)
#valor medio dos Imoveis
 valor_medio_geral = df["Valor_Imovel"].mean()
#Valor medio dos imoveis de Curitiba
filtro = df["Cidade"] == "Curitiba"
valor_medio = df.loc[filtro,("Valor_Imovel")].mean()
#Numero de imóveis com Valor acima do valor medio
filtro = df["Valor_Imovel"] >valor_medio_geral
df_maior = df.loc[filtro]
len(df_maior)
#Numero de imoveis com valor abaixo do valor medio
filtro = df["Valor_Imovel"] < valor_medio_geral
df_menor = df.loc[filtro]
len(df_menor)
