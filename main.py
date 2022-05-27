""" This will approimate lens shappe for aspheric lens to focus at a single point."""

from lenses import Lens
from light import Light
from display import Display

lens1Front = 0
focalPoint = 720
lensHeight = 180
numSegments = 100
n1 = 1.0
n2 = 1.5


lens1 = Lens(focalPoint, lensHeight, numSegments, n1, n2)

lens1.segments()


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

for lightBeam in light:
    lightBeam.rayLensIntersection(lens1)

for lightBeam in light:
    lightBeam.refraction(lens1)

#Extend rays for viewing
for lightBeam in light:
    lightBeam.rayExtension(2000)


#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(lens1.lensXY)

for lightBeam in light:
    toScreen.draw_Source(lightBeam.ray)

for lightBeam in light:
    toScreen.draw_Rays(lightBeam.ray)


toScreen.display_to_screen()

