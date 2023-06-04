# Librerias
from dataclasses import replace
from distutils.command.clean import clean
from webbrowser import get
import html2text
import requests
from bs4 import BeautifulSoup 
import re
import os


# Funciones
def buscador_titulares():
    # Variables Globales
    url = 'https://nearme.blog/bravo-supermarkets-near-me/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    salto_de_linea = "\n"

    # Find Box
    box = soup.find('div', class_='entry-content')

    # Buscamos los h2
    for heading in box.find_all('h2'):
        # Sacamos el texto
        headers = heading.text

        # Copiamos el texto
        with open("titulares",'a')as f:
            f.write(headers + "\n")

    # Buscamos los h3
    for heading in box.find_all('h3'):
        # Sacamos el texto
        headers = heading.text

        # Copiamos el texto
        with open("titulos.txt",'a')as f:
            f.write(headers + "\n")

buscador_titulares()