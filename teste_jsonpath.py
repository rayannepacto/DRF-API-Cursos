import requests
import jsonpath



avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')


#print(jsonpath.jsonpath(avaliacoes.json(),'results'))

#print(jsonpath.jsonpath(avaliacoes.json(),'results[1]'))

#print(jsonpath.jsonpath(avaliacoes.json(),'results[1].nome'))

#print(jsonpath.jsonpath(avaliacoes.json(),'results[1].comentario'))




#Todas as avaliacoes de quem avaliou


notas = jsonpath.jsonpath(avaliacoes.json(),'results[*].avaliacao')
print(notas)