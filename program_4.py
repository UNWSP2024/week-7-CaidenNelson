#programmer = Caiden
#date = 10.18.24

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input)
# and will return (as output) the distance between those points in space.
# The 3-dimensional coordinates must be stored as tuples.

import math

def input_checker(user_input):
    while True:
        try:
            coords = input(user_input)
            coordinate = tuple(float(x) for x in coords.strip("()").split(","))
            if len(coordinate) != 3:
                raise ValueError('There are only three coordinates on a three dimensional plane')
            return coordinate
        except ValueError:
            print('Your input is incorrect, type your coordinates like this: x,y,z')
def difference_from_points(coordinate_1,coordinate_2):
    return math.sqrt((coordinate_2[0] - coordinate_2[0])**2 +(coordinate_2[1] - coordinate_1[1])**2 +(coordinate_2[2] - coordinate_1[2])**2)



def main():


    coordinate_1=input_checker('What is your first set of coordinates? Type your answer like this, x,y,x ')



    coordinate_2 = input_checker('What is your second set of coordinates? Type your answer like this, x,y,z ')



    distance = difference_from_points(coordinate_1,coordinate_2)
    print(distance)


main()

# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
