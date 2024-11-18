# circle_03.py

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--radius', help='radius in cm', required=True, type=int)
# parser.add_argument('--area', help='Area in pixels', required=False, type=int)

args = parser.parse_args()
radius = args.radius

# Calculate area and circumference
import math
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius


# Print results
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
