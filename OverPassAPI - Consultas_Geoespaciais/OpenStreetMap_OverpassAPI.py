###########################################################################################
# Nome do Projeto: Analisador de Dados OpenStreetMap
# Autor: Welliton Lima
# Versão: v1.0
# Data de Criação: 01/12/2024
# Última Modificação: 26/12/2024
#
# Descrição:
# Esta aplicação utiliza a API Overpass para coletar e processar dados do OpenStreetMap
# (OSM). Permite realizar consultas geoespaciais para extração de informações como:
# estradas, pontos de interesse, edificações e muito mais.
#
# Funcionalidades:
# - Consulta personalizada à API Overpass com sintaxe OQL.
# - Processamento e análise de dados OSM retornados em formato JSON.
# - Visualização de dados em mapas interativos (opcional com biblioteca folium).
#
# Requisitos:
# - Python 3.8 ou superior.
# - Bibliotecas: requests, json, folium (opcional), pandas (opcional).
#
# Como Executar:
# 1. Instale as dependências:
#    pip install requests folium pandas
# 2. Configure a consulta Overpass no arquivo de configuração ou diretamente no código.
# 3. Execute o script
# 
#
# Referências:
# - API Overpass: https://wiki.openstreetmap.org/wiki/Overpass_API
# - Documentação OQL: https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide
#
###########################################################################################

import requests
import json
import os

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="meu_app_geolocalizacao")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

sair = False

while(sair == False):
    endereco = input("Insira um endereço: \n"" Rua, número, Bairro, Cidade, Estado""\n Ex: "" Av. Evergreen Terrace, 742, Suburbio, Springfield, Tacoma do Norte\nPara encerrar insira SAIR\n\n""")

    if(endereco.upper() == 'SAIR'):
        sair = True
    else:
        # Define uma delimitação de busca
        localizacao = geocode(endereco)

        if localizacao:
            lat = round(localizacao.latitude,6)
            lon = round(localizacao.longitude,6)
            around = 1000 # Metros
            
            #print(f"Coordenadas de {endereco}: Latitude: {lat}, Longitude: {lon}")

            # 5. Buscar lugares próximos
            # Definindo a URL da API Overpass
            overpass_url = "https://overpass-api.de/api/interpreter"

            # Definindo a consulta Overpass QL para buscar restaurantes

            overpass_query = f"""
            [out:json];
            (
            node["amenity"="restaurant"](around:{around},{lat}, {lon});
            node["amenity"="cafe"](around:{around},{lat}, {lon});
            node["amenity"="bar"](around:{around},{lat}, {lon});
            node["amenity"="school"](around:{around},{lat}, {lon});
            node["amenity"="fuel"](around:{around},{lat}, {lon});
            node["amenity"="kindergarten"](around:{around},{lat}, {lon});
            node["amenity"="fire_station"](around:{around},{lat}, {lon});
            node["amenity="="clinic"](around:{around},{lat}, {lon}); 
            node["amenity"="pharmacy"](around:{around},{lat}, {lon});
            node["amenity"="hospital"](around:{around},{lat}, {lon});
            node["tourism"="hotel"](around:{around},{lat}, {lon});
            node["shop"="supermarket"](around:{around},{lat}, {lon});
            node["shop"="convenience"](around:{around},{lat}, {lon});
            node["leisure"="fitness_centre"](around:{around},{lat}, {lon});
            
            );
            out body;
            """

            # Fazendo a requisição HTTP
            response = requests.get(overpass_url, params={'data': overpass_query})

            # Verificando se a requisição foi bem-sucedida
            if response.status_code == 200:
                # Processando os dados JSON da resposta
                data = response.json()
                print("\n")
                # Iterando pelos elementos retornados
                for element in data['elements']:
                    name = element['tags'].get('name', 'Sem nome')  # Obtendo o nome do estabelecimento

                    if name == "Sem nome" and 'brand' in element['tags']:
                        name = element['tags']['brand']

                    lat = element['lat']  # Latitude
                    lon = element['lon']  # Longitude

                    # Coletar tipo de estabelecimento
                    tipo = None
                    if 'shop' in element['tags']:
                        tipo = element['tags']['shop']     # Tipo de loja
                    elif 'amenity' in element['tags']:
                        tipo = element['tags']['amenity']  # Tipo de amenidade
                    elif 'tourism' in element['tags']:
                        tipo = element['tags']['tourism']  # Tipo de turismo
                    elif 'leisure' in element['tags']:
                        tipo = element['tags']['leisure']  # Tipo de lazer

                    rua = element['tags'].get('addr:street', '') # Número da rua

                    print(f"Estabelecimento: {name},Tipo:{tipo if tipo else 'Desconhecido'}, Localização: {rua} ({lat}, {lon})") # imprime resposta
                    print("\n")
            else:
                print("Erro na requisição:", response.status_code)

        else:
            print("Endereço não encontrado.")
    input("Pressione ENTER PARA CONTINUAR...")
    os.system('cls')

os.system('cls')        
print("Processo encerrado.")
