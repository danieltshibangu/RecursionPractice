def getValuesInRange( a, b ):
    if b == a:
        return b
    else:
        return str(getValuesInRange(a, b-1 )) + ", " + str(getValuesInRange( b, b ))

print( getValuesInRange( 1, 10 ) )
