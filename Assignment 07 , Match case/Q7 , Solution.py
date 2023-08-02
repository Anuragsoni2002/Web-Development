# Write a python program to check whether a given number is positive, negative or zero using match case statement
n=int(input("Enter a Number :"))
match n:
    case 0:
        print("Zero")
    case n if n>0:
        print("Positive")
    case _:
        print("Negative")
