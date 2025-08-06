# Check whether a character is uppercase or lowercase alphabet
char = input("Enetr the Character: ")
if (char >="A" and char <="Z"):
    print(char, "is an uppercase alphabet")
elif (char >= "a" and char <= "z"):
    print(char, "is an lowercase alphabet")
elif(char >="0" and char <="9"):
    print(char, "is an digit num")
else:
    print(char, "is an spaecial symbol")