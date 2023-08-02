# Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division.
"""print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Reminder")


x=int(input("Enter First Number :"))
y=int(input("Enter Second Number :"))
opr=input("Enter The operator(+,-,*,/,%)")
match opr:
    case '+':
        print("Addition",x+y)
    case '-':
        print("Subtraction",x-y)
    case '*':
        print("Multiplication",x*y)
    case '/':
        print("Division",x/y)
    case '%':
        print("Reminder",x%y)
    case _:
        print("Invalid Operator , Exit")
print()"""

n1=int(input("Enter First Number :"))
n2=int(input("Enter Second Number :"))
print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Reminder")

choise=int(input("Enter Your Menu Choice Number :"))
match choise:
    case 1:
        print("Addtion is:",n1+n2)
    case 2:
        print("Subtraction is:",n1-n2)
    case 3:
        print("Multiplication is:",n1*n2)
    case 4:
        print("Division is:",n1/n2)
    case 5:
        print("Reminder is:",n1%n2)
    case _:
        print("Sorry ! Not in menu list")














