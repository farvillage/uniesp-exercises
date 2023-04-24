#R1:
pessoa = {
    'primeiro_nome': 'Ygor',
    'segundo_nome': 'Carvalho',
    'idade': '19',
    'cidade': 'João Pessoa'
}

print(f'Primeiro Nome: {pessoa["primeiro_nome"]}')
print(f'Segundo Nome: {pessoa["segundo_nome"]}')

#R2:
num_fav = {
    'Ygor': '44',
    'Yann': '22',
    'Jerson': '24',
    'Bebeto': '17',
    'Rondi': '66'
}

for nome in num_fav.keys():
    print(f'{nome} -> {num_fav[nome]}')
    print(nome)
    print(num_fav[nome])
    print('-----------------------')
