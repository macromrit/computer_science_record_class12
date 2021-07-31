import math

def vol_cube(a:float=0.0)->str and float:
    ans = math.pow(a, 3)
    return F'Volume of the cube as per the given measurement is {ans:.3f}'

def vol_sphere(r:float=0.0)->str and float:
    ans = (4/3)*math.pi*(math.pow(r, 3))
    return F'Volume of the cube as per the given measurement is {ans:.3f}'
