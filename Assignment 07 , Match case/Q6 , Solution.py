"""
Write a python program to check whether a given string is a multiword string or single
word string using match case statement

"""
s1=input("Enter A String :")
# s1.strip() me suru ke space ko hatane kaam karta hai ,suruy ke space count nhi hota hai , agar count hoga to multiword ho jayega.
s2=s1.strip()
print(s2)
match s2:
    case s2 if ' ' in s2:
        print("Multiword String")
    case s2 if ' ' not in s2:
        print("Singleword string")