def xyz_there(str):
    """Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.)."""
    if 'xyz' in str: 
        if '.xyz' in str: 
            return False
        else: 
            return True 
    

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))