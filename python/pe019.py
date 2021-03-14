year, month = 1901, 0
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 2 # Jan 1 1901 was a Tuesday
count = 0

while year <= 2000:
    while month < 12:
        if day == 0:
            count += 1
        day += days_in_month[month]
        day %= 7
        month += 1
    month = 0
    year += 1
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            days_in_month[1] = 29
    else:
        days_in_month[1] = 28

print count
