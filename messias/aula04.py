'''R1:'''
N1 = int(input("Enter your grade: "))
if N1 > 10:
    print("You didn´t pass to Q3")

'''R2:'''
N1 = int(input("Tell me your grade 1: "))
N2 = int(input("Now, tell me your grade 2: "))
print((N1+N2)/2)

'''R2.1:'''
if ((N1+N2)/2) >= 7:
    print("Poooole!")
else:
    print("Out of Q1")

'''R3:'''
N1 = int(input("Enter number 1: "))
N2 = int(input("Enter number 2: "))
if N2 > N1:
    print(N2)

'''CORREÇÃO R1:'''
if N1 > 10:
    print(f"Higher than 10 - {N1}")
elif N1 == 10:
    print(f"{N1} is equal 10")
else N1 < 10:
    print(f"Bellow than 10 - {N1}")

'''CORREÇÃO R2:'''