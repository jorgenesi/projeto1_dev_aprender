"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248970)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
'''Cálculo do primeiro dígito do CPF'''

cpf = input('Digite o CPF: ')
nove_digitos = cpf[0:9] # Tira os dois últimos números do cpf

contador_regressivo = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1)* contador_regressivo # soma um por um a multiplicaçao (d1*mcr)
    contador_regressivo -= 1
print(resultado_digito_1)
digito_1 = (resultado_digito_1 *10) % 11 # resto da divisão -> (rd1*10)/11
print(f'digito_1: {digito_1}')  
digito_1 = digito_1 if digito_1 <= 9 else 0 # d1=di se d1 <= 9 então d1 = 0
print(f'Primeiro dígito: {digito_1}') 

'''Cálculo do segundo dígito do CPF'''

nove_digitos_2 = cpf[:10]
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_2 in nove_digitos_2:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'segundo dígito: {digito_2}')

'''Validação do CPF'''
novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
print(f"Novo cpf: {novo_cpf}")

if cpf == novo_cpf:
    print('-' * 30)
    print(f'CPF validado!')
    print('-' * 30)
    
else:
    print('-' * 30)
    print(f'CPF digitado é inválido!')
    print('-' * 30)
    
    