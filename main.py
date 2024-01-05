

year = int(input("What year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:

        if year % 400 == 0:
            print(f"This year {year} is a leap year")
        else:
            print(f"This year {year} is not a leap year")
    else:
        print(f"This year {year} is a leap year")
else:
    print(f"So, this year {year} is not a leap year")