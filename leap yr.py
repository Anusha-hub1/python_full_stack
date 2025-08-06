#Check whether a number is leap year or not
year = int(input("Enter the year: "))
if (year%400)==0 or (year%100)==0:
    if (year%4)==0:
     print("Given year is Leap year")
else:
     print("Given year is not a Leap year")