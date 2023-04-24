#list:
matriz3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#printing each list:
print(matriz3x3[0])
print(matriz3x3[1])
print(matriz3x3[2])

#printing one item in the list:
print(matriz3x3[0][1])

##################################

#5x5 list:
matriz5x5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

#printing 5x5 list:
for list in matriz5x5:
    for item in list:
        if (item % 2) == 0:
            print(f'This number is EVEN {item}')
        elif item == 5:
            print(f'This is number five - {item}')
        elif (item % 2) != 0:
            print(f'This number isnt five neither odd {item}')