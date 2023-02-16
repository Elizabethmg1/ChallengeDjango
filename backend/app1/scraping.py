from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json


def converter_json():
    result = scraping()
    result_json = json.dumps(result)
    return result_json

def scraping():
    list_of_dict = []
    url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'
    number_of_pages = get_page_numbers(url) # Get total number of pages from the first page
    number_of_pages = 3
    
    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(get_scraping, url+'?&_paginador_fila_actual='+str(page_num)):
                page_num for page_num in range(1, number_of_pages+1)
        }

        for future in as_completed(futures):
            scraping_items = future.result()
            list_of_dict.extend(scraping_items)

    return list_of_dict
                

def get_scraping(url):
    lista=[]

    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    req=requests.get(url, headers=headers)

    statuscode=req.status_code
    if statuscode == 200:
        soup = BeautifulSoup(req.text,'lxml')

        table = soup.find("table",{"class":"tabla_datos"})
        tbody = table.find("tbody")
        all_tr = tbody.find_all('tr')
        for tr in all_tr:
            all_td = tr.find_all("td")

            numero = int(all_td[0].text)
            nombre = all_td[1].a.text
            tipo = all_td[2].text
            region = all_td[3].text
            tipologia = all_td[4].text
            titular = all_td[5].text
            inversion = all_td[6].text
            fecha = all_td[7].text
            estado = all_td[8].text

            diccionario = {"numero":numero,"nombre":nombre,"tipo":tipo,"region":region,"tipologia":tipologia,"titular":titular,"inversion":inversion,"fecha":fecha,"estado":estado}
            lista.append(diccionario)
    return lista

def get_page_numbers(url):
    number_of_pages=1
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    req=requests.get(url, headers=headers)

    statuscode=req.status_code
    if statuscode == 200:
        soup = BeautifulSoup(req.text,'lxml')
        div_contenido = soup.find("div",{"class":"contenido"})
        split_text = div_contenido.text.split(' ')
        for text in split_text:
            if text.isnumeric() == True:
                number_of_pages = int(text)
                return number_of_pages
    return number_of_pages