import requests


headers = {'Authorization': 'Token eb3304bd86c842b8050497a3939a7cb37be5b010'}


url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


resultado_deletado = requests.delete(url=f'{url_base_cursos}11/', headers=headers)


assert resultado_deletado.status_code == 204



assert len(resultado_deletado.text) == 0