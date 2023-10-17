import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios

# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)
print(*produtos, sep='\n')
print()
#print(*novos_produtos, sep='\n')

# Aumente os preços dos produtos a seguir em 10%
def ordenar(lista): # Função 'ordenar' parâmetro(Lista)
    for item in lista: # para item na lista...
        print(item) # exibir item
    print()

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)} # round('dado', 2) -> 2 casa depos da vírgula
    #if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
    
novos_produtos1 = ordenar(novos_produtos)
# Ordene os produtos por nome decrescente (do maior para menor)
novos_produtos1 = sorted(novos_produtos, key=lambda item: item['nome']) # ordem crescente
print(f"1= ", *novos_produtos1, sep='\n')
print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
novos_produtos2 = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True) # ordem crescente
print("2= ", *novos_produtos2, sep='\n')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


