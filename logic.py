import datetime

Year = int(input("Please enter year of birth:"))
Month = int(input("Please enter the number of the month you were born.For exmaple 3 = March: "))
Day = int(input("Please enter the day you were born:"))

DOB = datetime.datetime(Year,Month,Day)
Age = (datetime.datetime.now() - DOB)
print("You are " + str(Age.days) + " days old")
convertdays = int (Age.days)
AgeYears = convertdays/365
print("you are " + str(AgeYears) +" years old")

if AgeYears <=18:
    print("minor")
elif AgeYears >=18 and AgeYears <=36:
    print("Youth")
else:
    print("elder")