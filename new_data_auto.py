import requests
from zipfile import ZipFile
import os
import pandas as pd
import openpyxl


arquivo = "http://www.telecocare.com.br/mapaerbs/ERBs_Nov22.zip" #nao mexer
nome_arquivo = "ERBs_Nov22.zip" #nao mexer
documento = "Nov22.xlsx" #nao mexer
pasta = "Downloaded" #nao mexer
regiao = "PA"

def download(url: arquivo, dest_folder: pasta):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # criando pasta caso não exista

    nomearquivo = url.split('/')[-1].replace(" ", "_")  
    caminho_arquivo = os.path.join(dest_folder, nomearquivo)

    r = requests.get(url, stream=True)
    if r.ok:
        print("salvando em", os.path.abspath(caminho_arquivo))
        with open(caminho_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
    
    with ZipFile(caminho_arquivo,"r") as zip_object:
        zip_object.extractall(pasta)
    


download("http://www.telecocare.com.br/mapaerbs/ERBs_Nov22.zip", dest_folder=pasta)



torres_df = rf"Downloaded\{documento}"
dados = pd.read_excel(torres_df, names=["Estação","Provedor","Estado","Cidade","Vazio","Logradouro","Longitude","Latitude","Nada","Tecnologia"])

# dados = dados.head()

# print(dados)

estado = regiao
pasta_save_csv = "CSV"
if not os.path.exists(pasta_save_csv):
    os.makedirs(pasta_save_csv)

torres = dados[["Provedor","Estado", "Longitude", "Latitude"]]

torres_estado = torres.loc[dados["Estado"] == estado]

#Exporta o arquivo para o caminho denominado
torres_estado.to_csv(fr"{pasta_save_csv}\lista_de_torres_{estado}.csv", sep=",")
############################################################
