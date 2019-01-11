# number = int(input("Enter a positive number"))
number = 7
if number % 2 != 0:
    print("Weird")
else:
    if number >= 2 and number <= 5:
        print("Not weird")
    elif number >= 6 and number <= 20:
        print("Weird")
    else:
        print("Not Weird")
