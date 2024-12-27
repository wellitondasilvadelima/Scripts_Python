###########################################################################################
# Project Name:Search movie list
# Author: Welliton Lima
# Version: v2.0
# Creation Date: 01/12/2024
# Last Modified: 26/12/2024
#
# Description:
# Using a movie title, search a list of movies
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

def request_API(titule): # makes a request to get the number of movies in the list
    n_page = 0
    try:
        req = requests.get("http://www.omdbapi.com/?&s=" + titule + "&type=movie&apikey=" + APIKEY)
        dictionary = json.loads(req.text)

    except Exception as e:
        print(e)
        return n_page

    if (dictionary['Response'] == "True"):
        total_results = dictionary['totalResults']
        n_page = round((int(total_results) / 10))  # Divide by 10 as this is the number of films displayed per page

    else:
        print(dictionary['Error'])

    return n_page

def movieList(titule, n_page): # function to make a request for each page found in the previous function

    movies = []

    for i in range(1, int(n_page), 1):
        try:
            req = requests.get("http://www.omdbapi.com/?&s=" + titule + "&page="+ str(i) +"&type=movie&apikey=" + APIKEY)
            dictionary = json.loads(req.text)
            movies.append(dictionary['Search'])

        except Exception as e:
            print("\n\nErro na requisição da página: ",i,"| AVISO: ",str(e))

    return movies


def movie_print(movie_list, pages): # print movie list
    print("\n")
    for i in range(0,int(pages)-1, 1):
        for movie in  movie_list[int(i)]:
            print("Título: "    ,movie['Title']     )
            print("Ano: "       ,movie['Year']      )
            print("Poster: "    ,movie['Poster']    )
            print("\n")

exit = False

while not exit:
    os.system('cls')
    op = input("Digite SAIR para encerrar\nInsira o nome de um filme: ")

    if(op.upper() == "SAIR"):
        exit = True
    else:
        if(op.upper() != ""):
            pages = request_API(op)
            if(pages != 0 ):
                list = movieList(op,pages)
                movie_print(list,pages)

        else:
            print("ENTRADA INVÀLDA")

    input("\nPressione Enter para continuar...\n\n")
    os.system("cls")

print("\n\n\nAplicação Encerrada...")