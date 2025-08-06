#Check whether a character is alphabet or not
char=input("Enter the chartacter: ")
if ((char[0]>="A" and char[0]<="Z") or (char[0]<= "a" and char[0]>= "z")):
    print(char, "is an character")
else:
    print(char, "is not an character")