###########################################################################################
# Project Name:Search movie information
# Author: Welliton Lima
# Version: v2.0
# Creation Date: 01/12/2024
# Last Modified: 26/12/2024
#
# Description:
# Using the title of a film, research some information about it.
#
# Features:
# Enter the name of a movie
#
# Requirements:
# - Python 3 or higher.
# - Libraries: requests, json.
#
# How to Run:
# 1. Make sure you have Python installed.
# 2. Install the dependencies with `pip install -r requirements.txt`.
# 3. Run the script with `python searchmovie.py`. #
###########################################################################################


import requests
import json
import os

APIKEY = "YOUR API KEY"

############################################################

def req(titule):
    try:
        #requisicao = requests.get("http://www.omdbapi.com/?t="+titulo+"&type=movie")
        response_request = requests.get("http://www.omdbapi.com/?&t=" + titule + "&type=movie&apikey=" + APIKEY)
        dictionary = json.loads(response_request.text)
        return dictionary

    except Exception as e:
        dictionary = {'Response': 'False', 'Error': e}
        return dictionary

def move_print(Movie):
    print("Título: "    ,Movie['Title']     )
    print("Ano: "       ,Movie['Year']      )
    print("Lançamento: ",Movie['Released']  )
    print("Duração: "   ,Movie['Runtime']   )
    print("Genero: "    ,Movie['Genre']     )
    print("Diretor: "   ,Movie['Director'] )
    print("Atores: "    ,Movie['Actors']    )
    print("Poster: "    ,Movie['Poster']    )
    print("Nota Imdb: " ,Movie['imdbRating'])

exit = False

while not exit:
    os.system('cls')
    op = input("Digite SAIR para encerrar\nInsira o nome de um filme: ")
    print("\n")
    if(op.upper() == "SAIR"):
        exit = True
        #print("Encerrando...")
    else:
        if(op.upper() != ""):
            Movie = req(op)
            
            if (Movie['Response'] == "False"):
                print(Movie['Error'])
            else:
                move_print(Movie)

    input("\nPressione Enter para continuar...\n\n")
    os.system("cls")

print("\n\n\nAplicação Encerrada...")