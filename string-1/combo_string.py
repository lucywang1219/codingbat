def combo_string(a, b):
    """
    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
    """
    if len(a) < len(b): 
        return a + b + a 
    else: 
        return b + a + b 

print(combo_string('Hello', 'hi')) 
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))
