arquivo = open('dom_casmurro_cap_1.txt.txt', 'r',encoding ='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()
print('#'*100)

arquivo = open('dom_casmurro_cap_1.txt.txt', 'r',encoding ='utf-8')
linha = arquivo.readline()
while linha !='':
    print(linha,end='')
    linha = arquivo.readline()
arquivo.close()
print('#'*100)

arquivo = open('dom_casmurro_cap_1.txt.txt', 'r',encoding ='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()
print('#'*100)

with open('dom_casmurro_cap_1.txt.txt', 'r',encoding ='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)
print('#'*100)

with open('arquivo_teste.txt','w',encoding ='utf-8') as arquivo:
    arquivo.write('essa é uma linha que eu escrevi usando python\n')
    arquivo.write('escrevi mais uma linha so pra exemplificar')
print('#'*100)

with open('arquivo_teste.txt','r',encoding ='utf-8') as arquivo:
    print(arquivo.read(), end='')


with open('arquivo_teste.txt','a',encoding ='utf-8') as arquivo:
    arquivo.write('essa é mais uma linha que eu escrevi usando python\n')

