from math import pi
def circle_area(r) :

    if type(r) != int and type(r) !=  float:
        raise TypeError("r has to be a number.")
    elif r<0:
        raise ValueError( "r has to be greater than 0." )
    else:
        return pi*(r**2

        
def endless_loop(n):
    i=0
    s=1
    while i<10:
        s=s*n
    return s
