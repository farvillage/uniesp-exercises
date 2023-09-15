vetor = [9,7,5,3,1,2,4,6,8,0]
n = len(vetor)

for i in range(n - 1):
    for j in range(0, n - i - 1):  
        if vetor[j] > vetor[j + 1]:
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
            
print(vetor)