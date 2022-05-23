""" This will approimate lens shappe for aspheric lens to focus at a single point."""

from lenses import Lens
from light import Light
from display import Display

focalPoint = 1000
lensHeight = 100
numSegments = 300
n1 = 1.0
n2 = 1.5



lens1 = Lens(focalPoint, lensHeight, numSegments, n1, n2)
lens1.coordinates()
#print(f"lens1 = {lens1.lensXY}")

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












#x = approximate(0, 300, 19234, 0.0000001)


