# Name: Da-un Jung
# SBUID: 115337987

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   return 5/9*(fahrenheit-32)

def what_to_wear(celsius):
    if celsius<-10:
        print ("puffy jacket")
    elif -10<celsius and celsius<=0:
        print ("scarf")         
    elif 0< celsius and celsius <=10:
        print ("sweater")
    elif 10< celsius and celsius <=20:
        print ("light jacket")
    else:
        print ("T-shirt")

    
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return ((x1*y2+x2*y3+x3*y1)-(x1*y3+x2*y1+x3*y2))/2
    

def euclidean_distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return ((x1-x2)**2+(y1-y2)**2)**0.5+((x2-x3)**2+(y2-y3)**2)**0.5+((x1-x3)**2+(y1-y3)**2)**0.5
    

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


import math
def deg2rad(deg):
    return deg*math.pi/180

import math
# s is length_side
# n is number_sides

def apothem(number_sides, length_side):
    deg2rad=math.pi/number_sides
    tantan=math.tan(deg2rad)
    apothem=length_side/(2*tantan)
    return apothem


import math

def apothem(number_sides, length_side):
    deg2rad=math.pi/number_sides
    tantan=math.tan(deg2rad)
    apothem=length_side/(2*tantan)
    return apothem
def polygon_area(number_sides, length_side):
    apothem_length=apothem(number_sides, length_side)
    return (number_sides*length_side*apothem_length)/2
   


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
def fahrenheit2celsius(fahrenheit): 
   return 5/9*(fahrenheit-32)
fahrenheit = 40
print()

what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

