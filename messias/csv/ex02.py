import csv

list = [['avocado'], ['grape'], ['kiwi']]

with open('ex02.csv', 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file, delimiter=';')
    writer.writerows(list)