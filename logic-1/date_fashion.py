def date_fashion(you, date):
    """The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no)."""
    if you <= 2 or date <= 2: 
        return 0 
    elif you >= 8 or date >= 8: 
        return 2 
    else: 
        return 1

print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))