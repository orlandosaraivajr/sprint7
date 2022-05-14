import requests
import json

# https://covid19-brazil-api-docs.vercel.app/

url = 'https://covid19-brazil-api.now.sh/api/report/v1'
r = requests.get(url)
casos_covid = r.json()
content = json.loads(r.content)


url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp'
r = requests.get(url)
dados_SP = r.json()


url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/20211020'
r = requests.get(url)
