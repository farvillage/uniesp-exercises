def selecao_Ordem(vetor, ordem):
    n = len(vetor)
    if ordem == 0:
        for i in range(n - 1):
            for j in range(0, n - i - 1):  
                if vetor[j] > vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    else: 
        for i in range(n - 1):
            for j in range(0, n - i - 1):  
                if vetor[j] < vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

vetor = [2,4,6,8,0,1,3,5,7,9]
selecao_Ordem(vetor,0)
print(vetor)
selecao_Ordem(vetor,1)
print(vetor)