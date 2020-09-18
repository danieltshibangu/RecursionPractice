def multiply( x, y ):
    # set base case
    if y == 1:
        return x
    else:
        return multiply( x, y-1) + multiply( x, 1 )

print( multiply(7, 5) )
