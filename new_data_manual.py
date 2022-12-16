import pandas as pd
import openpyxl

torres_df = r"E:\Tratamentos dados torres\Nov22 teste.xlsx"
# torres_df = torres_df.append({"Estação","Provedor"})
dados = pd.read_excel(torres_df, names=["Estação","Provedor","Estado","Cidade","Vazio","Logradouro","Longitude","Latitude","Nada","Tecnologia"])


dados = dados.head()

print(dados)
################################################
estado = "PA"
caminho_save_csv = "E:\Tratamentos dados torres"

torres = dados[["Provedor","Estado", "Longitude", "Latitude"]]

torres_estado = torres.loc[dados["Estado"] == estado]

#####
# torres_por_estado = torres["Estado"].value_counts()
# dados_df = dados[[]]
#####

#Exporta o arquivo para o caminho denominado
torres_estado.to_csv(fr"{caminho_save_csv}\lista_de_torres_{estado}.csv", sep=",")
############################################################
