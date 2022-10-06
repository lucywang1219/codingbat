
def left2(str):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
    """
    if len(str) > 2: 
        left_2 = str[:2] 
        rest = str[2:]
        return rest + left_2
    else: 
        return str

print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))