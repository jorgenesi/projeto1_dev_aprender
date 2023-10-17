"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# cpf = input('Número do CPF: ')
# lista_cpf = []
# #p, b, *_, ap, u = cpf
# p,b,c,e,f,g,h,i,j, *_ = cpf
# n1 = int(p)*10 + int(b)*9 + int(c)*8 + int(e)*7 + int(f)*6 + int(g)*5 + int(h)*4 + int(i)*3 + int(j)*2
# n1 = n1*10
# n1 = n1 % 11
# print(p,b,c,e,f,g,h,i,j)

# if n1 > 9:
#     n1 = 0
# else:
#     n1 = n1
# print('-' * 20)
# print(f'Primeiro Dígito: {n1}')
# print('-' * 20)

# programa do professor
cpf = input('Digite o CPF: ')

cpf = cpf[0:9] # Tira os dois últimos números do cpf

contador_regressivo = 10
resultado_digito_1 = 0

for digito_1 in cpf:
    resultado_digito_1 += int(digito_1)* contador_regressivo # soma um por um a multiplicaçao (d1*mcr)
    contador_regressivo -= 1
print(resultado_digito_1)
digito_1 = (resultado_digito_1 *10) % 11 # resto da divisão -> (rd1*10)/11
print(f'digito_1: {digito_1}')  
digito_1 = digito_1 if digito_1 <= 9 else 0 # d1=di se d1 <= 9 então d1 = 0
print(digito_1)     