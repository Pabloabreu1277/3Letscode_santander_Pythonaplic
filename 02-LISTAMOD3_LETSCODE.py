#2 - Para o segundo exercício, você deve criar um programa
#  que realize uma cópia do arquivo "alunos.csv". 
# Essa cópia deve ser um arquivo chamado "alunos_copia.csv".
#Novamente, aqui você também não precisa utilizar a
# biblioteca CSV mas se usar, seu código pode ser
# reutilizado na próxima questão sem muitas modificações.

import csv

with open('alunos.csv','r',encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    with open('alunos_copia.csv','w',encoding='utf-8',newline='') as arquivo_copia:
        escrever = csv.writer(arquivo_copia)
        for linha in leitor:
            escrever.writerow(linha)
    with open('alunos_copia.csv','r',encoding='utf-8') as arquivo_copia:
        leitornovo = csv.reader(arquivo_copia)
        for linhanova in leitornovo:
            print(linhanova)
