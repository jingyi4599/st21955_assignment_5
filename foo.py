def is_divisible_by_k(x, k): # parameter 'x' is not the same as those in line 12 to 14 as is just a name
    '''
    Checks whether x is divisible by k.
    '''
    return x%k == 0 # logical expression (==) for calculation will be a boolean result

'''
Store all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''
integers = [] # can use 'integers = list()' to create new list
for x in range(1,1001): # ':' refer to indexing eg a list, use ', for range and range will only consider integers no need worry about doubles
    if is_divisible_by_k(x, 2) or is_divisible_by_k(x, 5) or  is_divisible_by_k(x, 7): # python does not recognise symbols
    # only append if is divisible by k aka '== True' booolean
        integers.append(x)
    
'''
Sum all the integers that are multiples of 2 or 5 or 7 
that are lower or equal to 1000 (excluding doubles)
'''
print(sum(integers))  # output is 328927

