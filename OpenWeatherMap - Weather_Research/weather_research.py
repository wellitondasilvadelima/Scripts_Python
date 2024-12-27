###########################################################################################
# Project Name: weather research
# Author: Welliton Lima
# Version: v1.0
# Creation Date: 01/12/2024
# Last Modified: 26/12/2024
#
# Description:
# Research a city's weather
#
# Features:
# Enter the name of the city
#
# Requirements:
# - Python 3 or higher.
# - Libraries: requests, json.
#
# How to Run:
# 1. Make sure you have Python installed.
# 2. Install the dependencies with `pip install -r requirements.txt`.
# 3. Run the script with.
###########################################################################################

# Import Libs
import os
import requests
import json

#api_key = "Your API KEY"
language = "pt_br" # Brazilian Portuguese set as default

def getWeather(city):
    try:
        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key + '&units=metric&lang='+language)
        weather = json.loads(req.text)
        return weather

    except Exception as e:
        return e

def printar(weather):
    temperature  = weather["main"]["temp"]
    description  = weather["weather"][0]["description"]
    humidity     = weather["main"]["humidity"]
    city_name    = weather["name"]

    print(f"\nClima em {city_name}:")
    print(f"Temperatura: {temperature}°C")
    print(f"Descrição: {description}")
    print(f"Umidade: {humidity}%")

def main():
    sair = False
    while(sair != True):

        city = input('Digite SAIR para encerrar ou insira o nome da cidade: ')

        if(city.upper() == "SAIR"):
            sair = True
        else:
            if(city != ""):
                weather = getWeather(city)

                if(isinstance(weather, dict) and 'main' in weather):
                   printar(weather)

                elif(isinstance(weather, dict) and 'cod' in weather and weather['cod'] == 401):
                    print(weather['message'])
                else:
                    print(weather)
            else:
                print("Inserção inválida")
            input("Pressione ENTER para continuar...")

    print("APLICAÇÃO ENCERRADA")

main()