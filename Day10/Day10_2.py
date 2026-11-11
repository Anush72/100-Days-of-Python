# Leap Year Function

def is_leap_year(year):
    """
    :param year:
    :return: return the bool True for Leap Year
    False for not Leap Year
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2024))