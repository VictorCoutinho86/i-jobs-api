from bs4 import BeautifulSoup
import requests
from flask import jsonify
from difflib import SequenceMatcher

url_base = 'https://www.chances.com.br'
busca = '/chances/oportunidades/'


def get_jobs(palavra):
    req = requests.get(url_base + busca + palavra)
    soup = BeautifulSoup(req.text, 'html.parser')
    vagas = soup.find_all('section', class_='oportunidade')
    oportunidades = []

    for vaga in vagas:
        print(palavra + ' ' + vaga.find('h1').get_text() + ' = ' + str(similar(palavra, vaga.find('h1').get_text())*10))
        if similar(palavra, vaga.find('h1').get_text().strip(' ')) * 10 > 5:
            oportunidades.append({'titulo': vaga.find('h1').get_text(), 'localidade': vaga.find('localidade').get_text(),
                              'url': url_base + vaga.find('a', class_='btn-default').get('href')})

    print(oportunidades.__len__())
    return jsonify(oportunidades)


def similar(palavra_chave, oportunidade):
    return SequenceMatcher(None, palavra_chave, oportunidade).ratio()
