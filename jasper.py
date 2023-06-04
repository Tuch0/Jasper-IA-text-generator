'''
Informacion de uso:
1- El script depende de un fichero con titulos (var= fichero_titulos)
2- El script depende de un fichero con las palabras que deseas utilizar para generar el texto (var= read_words)
3- Le tienes que indicar tu correo de jasper.ai (var = correo)


Botones de el editor de Jasper:
jasper_button = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[4]/div/div[2]/div/div/button')
h1_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[3]')
h2_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[4]')
h3_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[5]')
h4_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[6]')
bold_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[7]')
italic_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[8]')
underline_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[9]')

Modes:
mode_shorter_button = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/button[1]')
mode_medium_button = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/button[2]')
mode_longer_button  = chrome_driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[4]/div/div[1]/div[2]/div[2]/button[3]')

Otros:
page_field = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/div/div[3]/div[1]/p')
'''

# Importar librerias
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup 
from packaging import version
import clipboard as c
from sys import stdout
import pyautogui 
import random
from urllib.request import urlopen
import requests
import json
import re
import time
import os

# Term Colours
def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)


# Nos conectamos con proxy
proxy_username = "aafUIgcHGF"
proxy_password = "FrNlECx9Zw"
proxyList = [
    '185.129.107.160:58542',
    '185.166.174.73:58542',
    '185.197.219.67:58542',
    '185.222.189.51:58542',
    '185.114.205.39:58542',
]

proxy_ip = random.choice(proxyList)
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip
proxy.ssl_proxy = proxy_ip
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_driver = webdriver.Chrome(executable_path="/Users/albertoalonso/Desktop/Trabajo/chromedriver", options=chrome_options, desired_capabilities=capabilities)



# Variables generales
home_jasper_url = 'https://beta.jasper.ai/'
url = str(home_jasper_url)
correo_name = "tuchoalonso3@gmail.com"
wait = WebDriverWait(chrome_driver,50)
soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')


# Iniciamos el navegador
chrome_driver.maximize_window()
chrome_driver.get(home_jasper_url)



# Iniciamos sesion con el proxy
os.system("clear")
yellow()
print('[!] Iniciamos proxy...')
time.sleep(1.3)
pyautogui.typewrite(proxy_username)
pyautogui.press('tab')
pyautogui.typewrite(proxy_password)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('tab')
pyautogui.typewrite(proxy_password)
pyautogui.press('enter')
green()
print('[+] Proxy iniciado con éxito\n')
time.sleep(5)


# Inicio De Sesión (manual)
yellow()
print('[!] Introducciendo correo..')
mail_account_field = chrome_driver.find_element(By.ID, "email")
mail_account_field.send_keys(correo_name)
mail_account_field.send_keys(Keys.ENTER)
yellow()
print('[!] Introduce el código de confirmacion en la web')
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[3]/article/div/div[2]/div[1]/div[1]')))
except:
    red()
    print('[*] La sesion a expirado')
    chrome_driver.close()

green()
print('[+] Inicio de sesión exitoso\n')
time.sleep(2)


# Iniciamos editor Jasper
yellow()
print('[!] Iniciamos el editor de jasper...')
jasper_editor = chrome_driver.get("https://app.jasper.ai/docs/edit/20a8701e-ffdf-4465-8d08-8b8122104e6b?source=next_gen")
url_jasper_editor = chrome_driver.get("https://app.jasper.ai/docs/edit/20a8701e-ffdf-4465-8d08-8b8122104e6b?source=next_gen")
time.sleep(1)
page = chrome_driver.get("https://app.jasper.ai/docs/edit/20a8701e-ffdf-4465-8d08-8b8122104e6b?source=next_gen")
soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/div/div[3]/div[1]/p')))
except:
    chrome_driver.close()
    print("[*] Dont Found Element")

green()
print('[+] Editor iniciado con exito\n')
time.sleep(2)

# Todas las funciones
def def_clean_jasper():

    # Leer archivo de los headers
    page_field = chrome_driver.find_element(By.XPATH, '//*[@id="docEditor"]/div[1]')
    page_field.click()
    time.sleep(1)
    page_field.send_keys(Keys.COMMAND + "a")
    page_field.send_keys(Keys.BACKSPACE)
    content_field = chrome_driver.find_element(By.XPATH, '//*[@id="topic"]')
    content_field.click()
    content_field.send_keys(Keys.COMMAND + "a")
    content_field.send_keys(Keys.BACKSPACE)
    tone_field = chrome_driver.find_element(By.XPATH, '//*[@id="tone"]')
    tone_field.click()
    tone_field.send_keys(Keys.COMMAND + "a")
    tone_field.send_keys(Keys.BACKSPACE)
    keywords_field = chrome_driver.find_element(By.XPATH, '//*[@id="keywordInput"]/div/ul/li/input')
    keywords_field.click()
    for i in range(6):
        keywords_field.send_keys(Keys.BACKSPACE)


def def_tone(tone):

    # Variable to string
    tone = str(tone)

    # Indicamos la variable y el tono
    tone_field = chrome_driver.find_element(By.XPATH, '//*[@id="tone"]')
    tone_field.send_keys(tone)


# Introducimos las keywords
def def_keywords(first,second,third):

    # Variables to string
    first = str(first)
    second = str(second)
    third = str(third)

    # Indicamos el boton y las palabras
    keywords_field = chrome_driver.find_element(By.XPATH, '//*[@id="keywordInput"]/div/ul/li/input')
    keywords_words = [first,second,third]

    # Introducimos las palbras clave
    for words in keywords_words:
        keywords_field.send_keys(words)
        keywords_field.send_keys(Keys.ENTER)


def def_jasper_button():

    # Indicamos el boton
    jasper_button = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/button')
    
    # Probamos si se puede pulstar el boton
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/button')))
        jasper_button.click()
    except:
        time.sleep(20)


def def_mode_output(tone):

    # Variable to string
    tone = str(tone)

    # Inicamos el condicional
    if tone == 'shorter':
        mode_shorter_button = chrome_driver.find_element(By.XPATH, '//*[@id="quillContainer"]/div[3]/div/div[2]/div[2]/button[1]').click()
    if tone == 'medium':
        mode_medium_button = chrome_driver.find_element(By.XPATH, '//*[@id="quillContainer"]/div[3]/div/div[2]/div[2]/button[2]').click()
    if tone == 'longer':
        mode_longer_button  = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[3]/div/div[2]/div[2]/button[3]').click()
    else:
        red()
        print('[!] El tono introducido es incorreto , vuleve a probar con alguno de estos: shorter,medium,longer')
        white()

def read_titulos():
    with open("titulos.txt") as archivo:
        for linea in archivo:
            linea = linea


def def_titulo_post():
    # Encontramos el titulo
    with open("test.txt")as titulo:
        file_title = titulo.readline()
        file_title = str(file_title)
    
    # Activamos el h1
    h1_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[3]')
    h1_button.click()
    time.sleep(1)

    # Copiamos el titulo
    page_field = chrome_driver.find_element(By.XPATH, '//*[@id="docEditor"]/div[1]')
    page_field.click()
    page_field.send_keys(file_title)
    page_field.send_keys("\n")


def def_create_article(title,content):

    # Indicamos el nombre de la api de wordpress
    url_wordpress_api = 'https://locationsnearme.blog'+'/wp-json/customapi/v1/create-post'

    
    # Indicamos la informacion que vamos a tramitar
    data = {
        "title": title,
        "content": content,
    }

    # Indicamos los headrrs
    headers = {
        #'Authorization':'Basic ' + apiKey,
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }
    
    # Creamos la variable que almacena la peticion a wordpress
    requestCreatePost = requests.post(url_wordpress_api, data=json.dumps(data), headers = headers)
    
    # Response, status
    green()
    print("\n")
    print(requestCreatePost.text)
    white()


def def_post_generator():

    # Limpiamos jasper
    blue()
    print('[!] REQUISITOS CUMPLIDOS , INICIANDO PROGRAMA...')
    time.sleep(3)

    def_clean_jasper()
    white()
    print('[+] 1- Jasper restaurado')
    time.sleep(3)

    # Añadimos titulo
    def_titulo_post()
    print('[+] 2- Titulo añadido')
    time.sleep(1)
    def_jasper_button()
    time.sleep(7)
    
    # Iniciamos beautifulSoup
    soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')
    editor = soup.select_one('div', class_='ql-editor')

    # Buscamos la data
    h1 = editor.find('h1').get_text()

    # Variable to string
    h1 = str(h1)


    # Almacenamos la data en un archivo
    title = h1
    with open(title + '.html', 'a') as file:
        file.write('<h1>' + title + '</h1>' + '\n')
        for element in editor.find_all('p'):
            jasper_text = element.get_text()
            jasper_text = str(jasper_text)
            file.write('<p>' + jasper_text + '</p>' + '\n')

    print('[+] 3- Texto Generado')
    time.sleep(1)

    # Introducimos Tono
    def_tone('witty')
    print('[+] 4- Tono de voz añadido')
    time.sleep(1)

    # Introducimos Keywords
    def_keywords('Store','Near Me','Food')
    print('[+] 5- Palabras claves añadidas')
    time.sleep(1)

    # Introducimos la longitud de el output
    chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[3]/div/div[3]/div[2]/button[3]').click()
    print('[+] 6- Longitud de texto establecida')
    time.sleep(1)

    # Indicamos las variables a tratar
    page_field = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/div/div[3]/div[1]/p')
    content_field = chrome_driver.find_element(By.XPATH, '//*[@id="quillContainer"]/div[3]/form/input')

    # Añadimos contentido a generar
    content_field.click()
    content_field_add = "Speak me about "
    titulos = read_titulos()

    # Introducimos los titulos
    with open("test.txt") as file:
        for line in file:

            # Borramos datos de contenido
            row = str(line)
            content = chrome_driver.find_element(By.XPATH, '//*[@id="quillContainer"]/div[3]/form/input')
            content.click()
            content.send_keys(Keys.COMMAND + "a")
            content.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            content.send_keys(content_field_add + row)
            time.sleep(1)

            # Imprimimos el titulo (apartado)
            page_field = chrome_driver.find_element(By.XPATH, '//*[@id="docEditor"]/div[1]')
            page_field.click()
            page_field.send_keys(Keys.COMMAND + 'a')
            page_field.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            h2_button = chrome_driver.find_element(By.XPATH, '//*[@id="toolbar"]/button[4]')
            h2_button.click()
            page_field.send_keys(row)
            time.sleep(1)
            page_field.send_keys("\n")
            time.sleep(1)

            # Introducimos textos
            page_field = chrome_driver.find_element(By.XPATH, '//*[@id="docEditor"]/div[1]')
            page_field.click()
            page_field.send_keys(Keys.COMMAND + Keys.ARROW_DOWN)
            def_jasper_button()
            time.sleep(10)

            # Buscamos la data
            soup = BeautifulSoup(chrome_driver.page_source, 'html.parser')
            editor = soup.select_one('div', class_='ql-editor')
            title = h1 
            h2 = editor.find('h2').get_text()

            # Variable to string
            h2 = str(h2)

            # Añadimos la data a un archivo
            with open(title + '.html', 'a') as file:
                file.write('<h2>' + h2 + '</h2>' + '\n')
                for element in editor.find_all('p'):
                    text = element.get_text()
                    text = str(text)
                    file.write('<p>' + text + '</p>')
                    file.write("\n")


            # Ponemos tiempo de espera
            time.sleep(5)

    '''
    # Subimos el Post
    title = title
    title = str(title)
    with open(title + '.html', 'r') as file:
        content = file.read()
        def_create_article(title,content)
    '''


# Iniciamos main
def_post_generator()