# Some straightforward vector maths for lists.
import math

def getDistance( p1, p2 ):
    return math.sqrt( sum([(a-b)**2 for (a,b) in zip(p1,p2)]) )

def getVector( p1, p2 ):
    return [b-a for (a,b) in zip(p1,p2)]

def getMagnitude( v ):
    return math.sqrt(sum([a**2 for a in v]))

def normalize( v ):
    m = getMagnitude( v )
    return [0 for a in v] if m == 0 else [a/m for a in v]


