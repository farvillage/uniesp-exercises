''' Criando um identificador de variável chamado nome atribuindo uma String ao identificador.'''

#Dados:
name = "Ygor Carvalho"
print(name)

name = input("Please, state your name: ")
print(f'Hello, {name}')

age = input("State your age: ")
print(f'Age {age} | type {type(age)}')

#Exemplo de soma:
print(5 + 3)

#Exemplo de subtração:
print(5 - 3)

#Exemplo de multiplicação:
print(5 * 3)

#Exemplo de divisão:
print(5 / 3)

#Exemplo esquisito:
resultado = (789 + 456 ) - 36985 / 88 * 456 + 78 ** 5
print(resultado)

a = 10
b = 10

if a == b:
    print('Pooooole!')
