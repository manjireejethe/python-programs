def year1():
    leap_year=0
    leap_year=int(input("Please enter the year: "))

    if leap_year :
        check_leap_year(leap_year)
    else:
        print("Please enter the valid year....")

def check_leap_year(leap_year):
    if (leap_year % 4) == 0:
        if (leap_year % 100) == 0:
            if (leap_year % 400) == 0:
                print(leap_year,"is a leap year")
            else:
                print(leap_year,"not a leap year")
        else:
            print(leap_year,"is a leap year")
    else:
        print(leap_year,"not a leap year")

year1()
