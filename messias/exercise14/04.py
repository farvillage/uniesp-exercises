def verifica_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % 1 == 0:
            return False
    return True

print(verifica_primo(4))