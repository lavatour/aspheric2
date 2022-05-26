""" This will approimate lens shappe for aspheric lens to focus at a single point."""

from lenses import Lens
from light import Light
from display import Display

lens1Front = 0
focalPoint = 1000
lensHeight = 300
numSegments = 10
n1 = 1.0
n2 = 1.5


lens1 = Lens(focalPoint, lensHeight, numSegments, n1, n2)

print(f"lens1 = {lens1.lensXY}")

lens1.segmentAngle()


""" Set number light sources"""
numberLightRays = len(lens1.lensXY) -1
#print(numberLightRays)


# Light list for light objects
light = []

""" Create instance of light """
for i in range(numberLightRays):
    light.append(Light(i, lens1))


""" ADD LIGHT SOURCE POINTS """
for lightBeam in light:
    lightBeam.lightSource()

for i in range(numSegments):
    pass
    #lens1.segmentAngle(lens1.lensXY[i])

#"""
#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(lens1.lensXY)

for lightBeam in light:
    toScreen.draw_Source(lightBeam.ray)

for lightBeam in light:
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()


#"""

def approximate(min, max, goal, precision):
    def increment(min, max, goal):
        """ Define a function. Enter min max and goal.
        call function at # call function here
        Incrementally approach a desired solution. """
        x = min
        dx = (max - min) / 10
        for i in range(0, 11):
            # call function here
            if function(x + dx) < goal:
                x = x + dx
            elif function(x + dx) > goal:
                min = x
                max = x + dx
                break
            elif function(x + dx) == goal:
                min = x + dx
                max = min
        return (min, max)
    while (max - min) > precision:
        (min, max) = increment(min, max, goal)
    print(f"x = {(min + max) / 2}")
    return (min + max) / 2

def function(x):
    r = x**2
    return r


approximate(0, 30, 400, 0.00000001)