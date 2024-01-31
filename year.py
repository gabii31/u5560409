def is_leap_year(year):
    year = int(year)
    if year %400 == 0:
        return True
    elif year %4 == 0 and year %100 != 0 :
        return True
    else:
        return False
    
print(is_leap_year(2020))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2019))