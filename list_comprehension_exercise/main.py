import copy
from pprint import pprint

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**item, 'preco': round(item['preco']*1.1,2)} 
    for item in copy.deepcopy(produtos)
]

produtos_orientados_por_nome = sorted(copy.deepcopy(produtos),key=lambda item: item.get('nome'))
produtos_orientados_por_preco = sorted(copy.deepcopy(produtos),key=lambda item: item.get('preco'))

pprint(produtos)
print()
pprint(novos_produtos)
print()
pprint(produtos_orientados_por_nome)
print()
pprint(produtos_orientados_por_preco)