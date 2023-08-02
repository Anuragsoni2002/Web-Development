"""
 Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement

"""
s1=input("Enter a First String :")
s2=input("Enter a Second String :")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("identical string")
    case (s1,s2) if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {}".format(s2,s1))