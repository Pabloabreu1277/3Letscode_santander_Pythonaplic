import csv

with open('brasil_covid.csv','r',encoding ='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    header = next(leitor)
    for linha in leitor:
        
        if float(linha[2]) > 1: 
            print(linha)


with open('brasil_covid.csv','r',encoding ='utf-8') as arquivo:
    linhas = arquivo.read()
    linhas = linhas.split("\n")
    for linha in linhas:
        linha = linha.split(',')
        print(linha)
with open('users.csv','w', encoding = 'utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['nome','sobrenome', 'email','genero'])
    escritor.writerow(['Pablo','Abreu', 'pato@gmai.com','masculino'])




