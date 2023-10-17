# Exemplo de uso dos sets
import os
letras = set()

while True:
    letra = input('Digite nome de uma flôr: ')
    letras.add(letra.lower()) #adicionar letra em lower(minúscula)

    if 'rosa' in letras:
        os.system('cls') # limpa a tela
        print('PARABÉNS é', letra)
        
        break
    
    print()
    print('Outra flôr: ',letras)
    
# while True:
#     letra = input('Digite uma letra até acertar a palavra: ')
#     letras.add(letra.lower()) #adicionar letra em lower(minúscula)

    # if 'l' in letras:
    #     print('PARABÉNS')
    #     break

    #print(letras)