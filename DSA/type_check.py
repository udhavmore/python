def only_ints(a, b):
    # if isinstance(a,int) and isinstance(b, int):
    #     return True
    # else:
    #     return False
    
    return type(a) == int and type(b) == int

print(only_ints(True,2))
