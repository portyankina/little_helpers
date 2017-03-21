from numpy import sin, cos, tan, arcsin, arccos, arctan, sqrt, pi

'''calculate length of arc from coordinates of end points'''
def arc_length(lat1, lon1, lat2, lon2):
    '''works for east longitudes and south latitdes (with +)'''
    phi1 = pi + lat1 
    phi2 = pi + lat2 
    
    AB = sin(phi1) * sin(phi2) + cos(-lon1 + lon2) * cos(phi1) * cos(phi2)
    arc = arccos(AB)
    return arc

'''spherical excess of the triangle'''
def spherical_excess(a, b, c):
    A = arccos( ( cos(a) - cos(b)*cos(c) ) / sin(b) / sin(c))
    B = arccos( ( cos(b) - cos(c)*cos(a) ) / sin(c) / sin(a))
    C = arccos( ( cos(c) - cos(a)*cos(b) ) / sin(a) / sin(b))    
    E = A + B + C - pi    
    return(E)

R_Mars = 3376.20000 # in km
Surf_Mars = R_Mars**2 # in km^2

'''calculate area of a spherical triangle'''
def triangle_area(a, b, c):
    E = spherical_excess(a,b,c)
    Area = Surf_Mars * E
    return Area