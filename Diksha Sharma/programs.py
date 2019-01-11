a = int(input("enter first number:"))
b = int(input("enter second number:"))

opr= input("Choose any one operation you want to perform (case sensitive):\nAddition \nSubtraction \nMultiplication \nDivision \nYour choice: ")

def add(a,b):
    sum = a+b
    return sum

def sub(a,b):
    sub = a-b
    return sub

def prod(a,b):
    prod= a*b
    return prod

def div(a,b):
    div= a/b
    return div

if opr=="Addition":
    print(add(a,b))
if opr == "Subtraction":
    print(sub(a, b))
if opr == "Multiplication":
    print(prod(a, b))
if opr == "Division":
    print(div(a, b))






