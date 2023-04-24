#R1:
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a>b:
    print("a is higher!")

#R2:
a = int(input("Enter your age: "))
if a>=18:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")

#R3:
n = int(input("Enter your fullname: "))
a = int(input("Enter your age: "))
if a>=18:
    print("You can drive this car.")
else:
    print("You cannot drive this car.")

#R4:
g1 = int(float("Enter your grade: "))
g2 = int(float("Enter your grade: "))
g3 = int(float("Enter your grade: "))
g4 = int(float("Enter your grade: "))
if g1+g2+g3+g4>=28:
    print("You are approved!")
else:
    print("You failed.")

#R5:
n = int(input("Enter a number: "))
if (n%2) == 0:
    print("This number is even.")
else:
    print("This number is odd.")

#R6:
w = int(float("Enter your salary: "))
if w>1.500:
    print("You're gonna receive the 10% raise.")
elif w<1.500:
    print("You're gonna receive the 15% raise.")

#R7:
p = int(str("Enter palindrome: "))
