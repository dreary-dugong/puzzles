day = 2
answer = 0
for year in range(1,100+1):
    for month in range(1,12+1):
        if month == 9 or month == 4 or month == 6 or month == 11:
            monthlyDays = 30
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            monthlyDays = 31
        elif month == 2 and year%4 != 0:
            monthlyDays = 28
        elif month == 2 and year%4 == 0:
            monthlyDays = 29
        for date in range(1, monthlyDays+1):
            day += 1
            if day == 8:
                day = 1
            if date == 1 and day == 1:
                answer += 1
print(str(answer))
