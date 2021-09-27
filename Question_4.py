# Write a program to find distance between two locations when their latitude and longitudes are given.
import math
from math import sin, cos, sqrt, atan2, radians

# lat1 = 53.32
# log1 = 12.14
# log2 = 55.64
# lat2 = 45.65
R = 6373.0


def distance(lat1, log1, lat2, log2):
    dlon = log2 - log1
    dlat = lat2 - lat1
    a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


lat1 = float(input("Enter the first location Latitude"))
log1 = float(input("Enter the first location Longitude"))
lat2 = float(input("Enter the second location Latitude"))
log2 = float(input("Enter the second location Longitude"))
print("First Coordinates", lat1, ",", lat2)
print("Second Coordinates", lat2, ",", log2)
lat1 = radians(lat1)  # converting into radian
log1 = radians(log1)
lat2 = radians(lat2)
log2 = radians(log2)

dis = distance(lat1, log1, lat2, log2)
print("Distance between both the coordinates is :- ", dis)
