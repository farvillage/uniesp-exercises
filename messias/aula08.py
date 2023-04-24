#List:

name = "Ygor"
names = ['Ygor', 'Yann', 'Fábio', 'Yanis']

#print lists:
print('names')
#print data:
print(type('names'))
#list  size:
print(len(names))
#print list's itens:
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Insert:

fruits = ['pear', 'apple', 'grape', 'kiwi']
fruits[1] = 'avocado'
print(fruits)
fruits.insert(2, 'strawberry')
print(fruits)
fruits.insert(5, 'chicken') #chicken isn't a fruit
print(fruits)
del fruits[5]
print(fruits)

del fruits[fruits.index('watermelon')]
print(fruits)
fruits.remove('kiwi')
print(fruits)
fruits.insert(10, 'plum')
print(fruits)
pop_fruit = fruits.pop(fruits.index('plum'))
print(f'Pop Fruta - {pop_fruit}')
print(fruits)

#"Lists of list":
lists_list = [
    [1, 2, 4, 44, 55],
    [16, 22, 23, 11, 10],
    [31, 27, 77, 24, 63]
]

lists_dictionary = {
    'furtas' = ['PEACHES', 'grape', 'strawberry'],
    'cars' = ['W11', 'FW14b', 'W12']
}

print(lists_dictionary['cars'][2])

print(lists_list[44][77][1])

