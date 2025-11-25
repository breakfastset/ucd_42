def is_leap_year(year):
    """Return True if year is a leap year."""
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

    # return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    print("2000 is leap year? ", is_leap_year(2000))
    print("2100 is leap year? ", is_leap_year(2100))
    print("2001 is leap year? ", is_leap_year(2001))
    print("2004 is leap year? ", is_leap_year(2004))

main()