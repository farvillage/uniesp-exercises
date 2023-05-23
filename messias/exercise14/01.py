def conta_vogais(string):
    vogais = 'aeiouAEIOU'

    count = 0
    for letra in string:
        if letra in vogais:
            count += 1
        return count

print(conta_vogais("hamilton"))