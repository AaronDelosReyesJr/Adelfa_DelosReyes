# A. Computational Thinking
## Problem Identification
Finding the area, perimeter, square root of the area, area rounded up, and area rounded down of the circular garden.
## Problem Decomposition
### Input
How to get the radius


### Processing
How to calculate the area

How to calculate the circumference

How to implement the math library

### Output
How to display the result

How to round off the numbers to the nearest 2 decimal places

## Pattern Recognition
The solutions using the math library will be used

Users will input the radius of the circular garden in meters only

## Data Representation
Program displays the area, circumference, squareroot of the area, area rounded up, and area rounded down of the circular garden in meters.

## Algorithm Development
import math

radius = float(input("Enter radius of your circular garden (in meters): "))

area = math.pi * math.pow(radius, 2)

circumference = 2 * math.pi * radius
sr_area = math.sqrt(area)

rd_area = math.floor(area)

ru_area = math.ceil(area)

print(f"The area of your circular garden is {area: .2f} square meters.")

print(f"The circumference of your circular garden is {circumference: .2f} meters.")

print(f"The square root area of your circular garden is {sr_area: .2f} meters.")

print(f"The area of your circular garden rounded down is {rd_area} square meters.")

print(f"The area of your circular garden rounded up is {ru_area} square meters.")