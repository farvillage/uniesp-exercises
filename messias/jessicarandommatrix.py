import random

n = int(input('Enter a dimension n in the matrix: '))
m = int(input('Enter a dimension in the matrix: '))
matrix = []

for i in range(n):
    line = []
    for j in range(m):
        line.append(random.randint(0, 10))
    matrix.apppend(line)
print(matrix)

#WHAT THE HECK JESSICA