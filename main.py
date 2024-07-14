month_code = {"jan": 6, "feb": 2, "mar": 2, "apr": 5, "may": 0, "jun": 3, "jul": 5, "aug": 1, "sep": 4, "oct": 6, "nov": 2, "dec": 4}

leap_month_code = {"jan": 5, "feb": 1, "mar": 2, "apr": 5, "may": 0, "jun": 3, "jul": 5, "aug": 1, "sep": 4, "oct": 6, "nov": 2, "dec": 4}

day_code = {0: "Sun", 7: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}

year = int(input("YEAR:"))
day = int(input("DAY:"))
month = input("MONTH:").lower()

year1 = str(year)[-2:]
year2 = int(year1)//4
year = int(year)
leap = leap_month_code[month]
normal = month_code[month]

if (int(year % 4 == 0 and year % 100 != 0)) or (year % 400 == 0):
    DAY = (int(year1) + int(year2) + day + leap) % 7
    DAY = int(DAY)
    DAY_NAME = day_code[DAY]
    print(DAY_NAME)
else:
    DAY = (int(year1) + int(year2) + day + normal) % 7
    DAY = int(DAY)
    DAY_NAME = day_code[DAY]
    print(DAY_NAME)
