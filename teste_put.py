import requests


headers = {'Authorization': 'Token eb3304bd86c842b8050497a3939a7cb37be5b010'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'



curso_atualizado = {
    "titulo": "Curso de xadrez",
	"url": "https://www.cursodexadrez.com.br"
}


resultado = requests.put(url=f'{url_base_cursos}10/', headers=headers, data=curso_atualizado)



assert resultado.status_code == 200


assert resultado.json()['titulo'] == curso_atualizado['titulo']



curso = requests.get(url=f'{url_base_cursos}10/', headers=headers)
print(curso.json())