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
with open('users.csv','w', encoding = 'utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['nome','sobrenome', 'email','genero'])
    escritor.writerow(['Pablo','Abreu', 'pato@gmai.com','masculino'])


#exemplo de cadastro

header = ['nome', 'sobrenome']
dados = []
opt = input('Escolha uma opção :\n1 - Cadastrar\n0 - Sair\n')
while opt !='0':
    nome = input('Qual seu nome?')
    sobrenome = input('Qual seu sobre nome?')
    dados.append([nome, sobrenome])
    opt = input('Escolha uma opção :\n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer. writerow(header)
    writer.writerow(dados)
with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

