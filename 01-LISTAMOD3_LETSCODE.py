#Questão 1-Neste exercício você deve criar um programa
#que abra o arquivo "alunos.csv" e imprima o conteúdo 
#do arquivo linha a linha.Note que esse é o primeiro
#  exercício de uma sequência, então o seu código pode ser
#  reaproveitado nos exercícios seguintes.
#  Dito isso, a recomendação é usar a biblioteca CSV para ler
#  o arquivo mesmo que não seja realmente necessário 
# para esse primeiro item.

import csv
from email import header

with open('alunos.csv','r',encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    #pula cabeçalho
    # header_alunos = next(leitor)
    for linha in leitor:
        print(linha)
