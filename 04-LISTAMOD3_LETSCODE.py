"""
Questão 4
Você conhece Star Wars? Se trata, obviamente, da famosa saga espacial criada por George Lucas em 1977 e que deu origem a símbolos do cinema e da cultura pop como o imponente vilão Darth Vader ou o simpático robô R2-D2. A ideia desse exercício é justamente extrair informações do personagem Darth Vader através de uma API de Star Wars chamada SWAPI.

Utilize a URL "https://swapi.dev/api/people/4/" para fazer a requisição dos dados de Darth Vader e extraia as informações "name" (nome), "height" (altura), "mass" (massa) e "birthyear" (ano de nascimento e imprima cada dado em uma linha.

Dica: caso não se lembre de como fazer isso, assista novamente a aula sobre API porque o exemplo da aula pode te ajudar.


"""
import csv
import requests as r
URL = "https://swapi.dev/api/people/4/"
#verificação do acesso a api
#apareceu 200 acesso executado com sucesso
req = r.get(URL)
print(req.status_code)

#Extração de dados
dados = req.json()
#print(dados)
inf_vader =['name','height','mass','birth_year']

for valor in inf_vader:
    
    with open('Vader.csv','w',encoding ='utf-8',newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(inf_vader)
        for linha in inf_vader:
            escrever.writerow(dados[linha])

    

    print(dados[valor])   


