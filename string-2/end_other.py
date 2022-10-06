def end_other(a, b):
    """Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences """
    a = a.lower()
    b = b.lower()
    if len(a) < len(b): 
        return a == b[-len(a):]
    elif len(b) < len(a): 
        return b == a[-len(b):]

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
