def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        return True
    return leap
