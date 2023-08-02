# Write a python script to display the number of days in a given month number.
"""n=int(input("Enter a Month Number :"))
match n:
    case 1:
        print("January - 31 Days")
    case 2:
        print("February - 28 Days")
    case 3:
        print("March - 31 Days")
    case 4:
        print("April - 30 Days")
    case 5:
        print("May - 31 Days")
    case 6:
        print("June - 30 Days")
    case 7:
        print("July - 30 Days")
    case 8:
        print("August - 31 Days")
    case 9:
        print("September - 30 Days")
    case 10:
        print("October - 31 Days")
    case 11:
        print("November - 30 Days")
    case 12:
        print("December - 31 Days")
    case _:
        print("Incorrect! Month Number")
print()"""


m=int(input("Enter a Month Number :"))
match m:
    case m if m in (1,3,5,7,8,10,12):
        print("31 days")
    case m if m in (4,6,9,11):
        print("30 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Invalid Month Number")