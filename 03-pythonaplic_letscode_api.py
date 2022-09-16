import requests
url = 'https://api.exchangerate-api.com/v6/latest'
#verificação do acesso a api
req = requests.get(url)
print(req.status_code)

dados = req.json()
print(dados)
valor_reais = float(input("Informe o valor em reais a ser convertido:\n"))
cotacao = dados['rates']['BRL']
print(f"R$ {valor_reais} em dolar valem US${valor_reais / cotacao:.2f}")
