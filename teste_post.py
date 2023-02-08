import requests



headers = {'Authorization': 'Token eb3304bd86c842b8050497a3939a7cb37be5b010'}


url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'




novo_curso = {
    "titulo" : "Curso de Dama",
    "url" : "https://www.cursodedama.com.br"
}


resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == 201 

assert resultado.json()['titulo'] == novo_curso['titulo']
