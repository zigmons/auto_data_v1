import requests
from zipfile import ZipFile
import os
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
import csv
import string
from bs4 import NavigableString



arquivo = r"C:\Users\RafaelSousa\db_torres\auto_data_v1\auto_torres_bd_ugm\HIGHLINE.kmz" #nao mexer
nome_arquivo = "ERBs_Nov22.zip" #nao mexer
documento = "Nov22.xlsx" #nao mexer
pasta = "Dados" #nao mexer
regiao = "SP"


def download(url: arquivo, dest_folder: pasta):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # criando pasta caso não exista

    nomearquivo = url.split('/')[-1].replace(" ", "_")  
    caminho_arquivo = os.path.join(dest_folder, nomearquivo)

    
    with ZipFile(caminho_arquivo,"r") as zip_object:
        zip_object.extractall(pasta)
    

download(r"C:\Users\RafaelSousa\db_torres\auto_data_v1\auto_torres_bd_ugm\HIGHLINE.kmz", dest_folder=pasta)


infile = r'C:\Users\RafaelSousa\db_torres\auto_data_v1\auto_torres_bd_ugm\Dados\doc.kml'
outfile = 'my_file.csv'

# coordenadas =[]
# latitude =[]
# longitude =[]

# with open(infile, encoding="utf-8") as f:
#     s = BeautifulSoup(f, 'xml')

# for coords in s.find_all('coordinates'):
#     coordenadas.append(coords.string)


# # lattitude
#     latitude.append(coordenadas)
    
#     # print(latitude)
 


# with open(outfile, 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Latitude', 'Longitude'])
#     csv_writer.writerow([latitude])







def process_coordinate_string(str):
    """
    Take the coordinate string from the KML file, and break it up into [Lat,Lon,Lat,Lon...] for a CSV row
    """
    space_splits = str.split(" ")
    ret = []
    # There was a space in between <coordinates>" "-80.123...... hence the [1:]
    for split in space_splits[1:]:
        comma_split = split.split(',')
        ret.append(comma_split[1])    # lat
        ret.append(comma_split[0])    # lng
    return ret

def main():
    """
    Open the KML. Read the KML. Open a CSV file. Process a coordinate string to be a CSV row.
    """
    with open(infile, encoding="utf-8") as f:
        s = BeautifulSoup(f, 'xml')
        with open(outfile, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            for coords in s.find_all('coordinates'):
                writer.writerow(process_coordinate_string(coords.string))

# if __name__ == "__main__":
    main()











    # for coords in s.find_all('coordinates'):
    #     # Take coordinate string from KML and break it up into [Lat,Lon,Lat,Lon...] to get CSV row
    #     space_splits = coords.split(" ")
    #     row = []
        
    #     for split in space_splits[1:]:
    #         # Note: because of the space between <coordinates>" "-80.123, we slice [1:]
    #         comma_split = split.split(',')

    #         # lattitude
    #         row.append(comma_split[1])
            
    #         # longitude
    #         row.append(comma_split[0])
        
    #     writer.writerow(row)











# def main():
#     """
#     Open the KML. Read the KML. Make 3 lists for Name, Coordinates and Description of the placemarks. Save the data to a CSV
#     """
#     name_counter = 0
#     names_list = []
#     coords_counter = 0
#     coords_list = []
#     desc_counter = 0
#     desc_list = []
    
#     with open('input_file.kml', 'r') as f:
#         s = BeautifulSoup(f, 'xml')

#         for names in s.find_all('name'):                #google earth nomenclature. Should read the KML file to see the relevant names we require
#             names_list.append(names.string)
#         names_list = names_list[2:]       #only keep names of placemarks
#         name_counter = len(names_list)

#         for coords in s.find_all('coordinates'):
#             coords_list.append(coords.string)
#             coords_list = [string.replace(',9','') for string in coords_list] #here i am manually removing the altitude from coords. Not the best way
#         coords_counter = len(coords_list)

#         for descriptions in s.find_all('description'):
#             desc_list.append(descriptions.string)
#         desc_counter = len(desc_list)

#     print(f'name counter = {name_counter}')         #just for testing, all counters should be equal
#     print(f'coords counter = {coords_counter}')
#     print(f'descriptions counter = {desc_counter}')

#     with open('output2.csv', 'w') as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow(['Name', 'Coordinates', 'Description'])
#         for counter in range(0, name_counter):
#             csv_writer.writerow(
#                 [names_list[counter], coords_list[counter], desc_list[counter]])


# if __name__ == "__main__":
#     main()