nome = 'Jorge Leonardo'
altura = 1.86
peso = 97
imc = 97/altura**2 # IMC = peso/(altura x altura) 
#   -Formatação (imc:.2f)-> duas casas depois da vírgula
Texto = f'{nome} tem {altura} de altura, pesa {peso} kilos e seu IMC é {imc:.2f}'
"f-strings"
print(Texto)

print(str(nome) + ' tem ' + str(altura) + ' de altura, pesa ' +  str(peso) + ' kilos e seu IMC é ' + str(imc))