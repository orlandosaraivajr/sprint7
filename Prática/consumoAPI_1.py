import requests
import xmltodict

cep = '13506095'

url = 'http://viacep.com.br/ws/' + cep + '/json/'
r = requests.get(url)
endereco_json = r.json()

url = 'http://viacep.com.br/ws/' + cep + '/xml/'
r = requests.get(url)
endereco_xmldata = xmltodict.parse(r.content)


url = 'http://viacep.com.br/ws/' + cep + '/piped/'
r = requests.get(url)

endereco_piped = r.content
