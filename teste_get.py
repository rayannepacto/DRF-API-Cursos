import requests



headers = {'Authorization': 'Token eb3304bd86c842b8050497a3939a7cb37be5b010'}


url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


resultado = requests.get(url=url_base_cursos, headers=headers)



#Testar endpoint

#assert resultado.status_code == 400



assert resultado.json()['results'][0]['titulo'] == 'Curso de dança'