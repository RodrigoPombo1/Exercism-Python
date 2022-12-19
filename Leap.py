def leap_year(year):
    if (not year % 4 and year % 100) or not year % 400:
        return True
    return False
