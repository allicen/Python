from datetime import timedelta, date

dateIn = input().split()
yearIn = int(dateIn[0])
monthIn = int(dateIn[1])
daysIn = int(dateIn[2])

date = date(yearIn, monthIn, daysIn)
days = timedelta(days=int(input()))

newDate = date + days
print(newDate.year, newDate.month, newDate.day)
