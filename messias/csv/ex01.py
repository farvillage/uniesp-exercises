import csv

with open('ex01.csv', 'r', newline='', encoding='utf-8') as file:
    file_read = csv.reader(file, delimiter=';')

    for line in file_read:
        print(line)

        if line[1] >= '30':
            print(f'{line[0]} have more than 30 years!')