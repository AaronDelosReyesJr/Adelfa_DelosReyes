#AARON G DELOS REYES JR
#8 ADELFA
#COMP SCI LONG TEST PART 2
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