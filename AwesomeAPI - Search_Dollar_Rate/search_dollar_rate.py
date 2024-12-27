###########################################################################################
# Project Name: Search for the dollar rate
# Author: Welliton Lima
# Version: v1.0
# Creation Date: 01/12/2024
# Last Modified: 26/12/2024
#
# Description:
# Search for the dollar rate of the currency entered
#
# Features:
# Enter the currency code of the currency
#
# Requirements:
# - Python 3 or higher.
# - Libraries: requests, json,datetime,time.
#
# How to Run:
# 1. Make sure you have Python installed.
# 2. Install the dependencies with `pip install -r requirements.txt`.
# 3. Run the script with.
###########################################################################################

# Import Libs
import datetime
import json
import os
import requests
import time

USD = "USD" # EUA currency

def getRate(search): # Dollar rate request function for Awesome API
    try:
        URL = "https://economia.awesomeapi.com.br/json/last/"+ USD +"-"+ search      # Awesome API URL string
        response_request = requests.get(URL)                                         # Makes the request
        response = json.loads(response_request.text)                                 # Turn the request into a dictionare
        return response

    except Exception as e:                                                           # Return Error
        return e

def main(): # Main function

    exit = False           # Application exit control

    while(exit == False):

        search = input("Informe o código da moeda: ")

        if(search.upper == "SAIR"):
            exit = True
        else:
            rate = getRate(search) 
            os.system('cls')

            currency_search = USD+search

            if(isinstance(rate, dict) and currency_search in rate): # isinstance checks if the return of the function is a dictionary | Checks if the tag is of the sought conversion
                print("Cotação do dolar para a moeda "+search+" : ",round(float(rate[currency_search]['ask']),3))

            elif(isinstance(rate, dict) and 'status' in rate and rate['status'] == 404): # Check status 
                print(rate['message'])
            else:
                print(rate)

            print("Hora: ", datetime.datetime.now(),"\n")
            input("Pressione ENTER para continuar... ")
            os.system('cls')
        
main()