def encontrar_Max(vetor):
    maximo = vetor[0]

    for elemento in vetor:
        maximo = elemento
        return maximo
    
def encontrar_Min(vetor):
    minimo = vetor[0]

    for elemento in vetor:
        minimo = elemento
        return minimo
    
def encontrar_Max_Min(vetor):
    maximo = vetor[0]
    minimo = vetor[0]

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento
    return [maximo, minimo]

vetor = [7,5,3,9]
print(encontrar_Max(vetor))
print(encontrar_Min(vetor))
resp=encontrar_Max_Min(vetor)
print(resp[0], resp[1])