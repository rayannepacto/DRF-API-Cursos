import requests

#GET


avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

#print(avaliacoes.json())

#Acessando count

#print(avaliacoes.json()['count'])

#print(avaliacoes.json()['next'])

#print(avaliacoes.json()['results'])

#print(avaliacoes.json()['results'][-1]['nome'])


#avaliacoes_unica = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/3/')
#print(avaliacoes_unica.json())


#GET CURSO

headers = {'Authorization': 'Token eb3304bd86c842b8050497a3939a7cb37be5b010'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)


#print(cursos.json())


