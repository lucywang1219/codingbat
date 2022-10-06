def extra_end(str):
    if len(str) >= 2: 
        return str[-2:]*3

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))
