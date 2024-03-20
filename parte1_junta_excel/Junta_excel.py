import os
import pandas as pd

#Criação de um dataframe para funcionar como "acumulador"
df = pd.DataFrame()

#Iteração para achar os arquivos do diretório atual
for arquivo in os.listdir():

    #se o arquivo for excel (xlsx)
    if ".xlsx" in arquivo:
        df_temporario = pd.read_excel(arquivo)
        df = pd.concat([df, df_temporario], axis=0)


df.to_excel("Arquivo_concatenado.xlsx", index=False)