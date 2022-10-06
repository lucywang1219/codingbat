def in1to10(n, outside_mode):
    """Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10."""
    if 1 <= n <= 10 and outside_mode == False: 
        return True 
    elif n <= 1 or n >= 10: 
        if outside_mode == True: 
            return True 
        else: 
            return False 
    else: 
        return False 

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))