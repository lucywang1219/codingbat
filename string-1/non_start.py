def non_start(a, b):
    """Given 2 strings, return their concatenation, except omit the first char of each"""
    return a[1:] + b[1:]

print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))