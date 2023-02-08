import requests


class TestCurso: 
    headers = {'Authorization': 'Token eb3304bd86c842b8050497a3939a7cb37be5b010'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'


    def test_get_cursos(self):
        curso = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert curso.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}5/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de django",
			"url": "https://www.cursodedjango.com.br"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code ==201
        assert resposta.json()['titulo'] == novo['titulo']


    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso de django rest framework",
			"url": "https://www.cursodedrf.com.br"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=atualizado)

        assert resposta.status_code ==201
        

    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso de django rest framework2",
			"url": "https://www.cursodedrf2.com.br"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']


    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}12/', headers=self.headers)
        
        assert resposta.status_code == 204 and len(resposta.text)== 0