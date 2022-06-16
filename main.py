""" This will approimate lens shappe for aspheric lens to focus at a single point."""

from lenses import Lens1
from lenses import Lens2
from light import Light
from display import Display

#numberLightRays = 100
lens1Front = 0
focalPoint = 720
lensHeight = 180
numSegments = 50
n1 = 1.0
n2 = 1.495

light = []
lens1 = Lens1(focalPoint, lensHeight, numSegments, n1, n2)


n1 = 1.5
n2 = 1.0
lens2Position = 5000 #DOES NOTHING
lens2 = Lens2(n1, n2, lens2Position)
scaleFactor = 0.2

lens1.Inner("Middle")


""" Set number light sources"""
numberLightRays = len(lens1.lensXY) -1
#print(numberLightRays)


# Light list for light objects


""" Create instance of light """
for rayNumber in range(numberLightRays):
    light.append(Light(rayNumber, lens1))


""" ADD LIGHT SOURCE POINTS """
for lightBeam in light:
    lightBeam.lightSource()

for lightBeam in light:
    lightBeam.rayLensIntersection(lens1)

for lightBeam in light:
    lightBeam.refraction(lens1)

for lightBeam in light:
    lightBeam.rayExtension(100)

#Find focal point to calculate second lens
lens2.findfocalPoint(light)

lens2.align1(light)

#lens2.scale(scaleFactor, lens1)
#lens2.align(light)

for lightBeam in light:
    lightBeam.rayLensIntersection(lens2)
    lightBeam.rayLensIntersection(lens2)
    pass


for lightBeam in light:
    #lightBeam.refraction(lens2)
    pass

for lightBeam in light:
    lightBeam.rayExtension(700)
    pass


#******************************************8
toScreen = Display()

#drawLens
toScreen.draw_Lens1(lens1.lensXY, "RED")
#toScreen.draw_Lens1(lens1.lensXYMid, "BLUE")
#toScreen.draw_Lens1(lens1.lensXYOuter, "BLACK")
toScreen.draw_Lens1(lens2.lensXY, "RED")

for lightBeam in light:
    toScreen.draw_Source(lightBeam.ray)

for lightBeam in light:
    toScreen.draw_Rays(lightBeam.ray)

print(lens1.fp)

toScreen.draw_FocalPoint(lens1.fp)
toScreen.display_to_screen()

