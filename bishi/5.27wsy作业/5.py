def isLeapYear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# 测试
test_years = [1600, 2000, 1900, 2004, 2019]
results = {year: isLeapYear(year) for year in test_years}
print(results)
