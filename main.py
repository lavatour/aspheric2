""" This will approimate lens shappe for aspheric lens to focus at a single point."""

from lenses import Lens1
from lenses import Lens2
from lenses import completeLens
from light import Light
from display import Display

#numberLightRays = 00
lens1Front = 0
focalPoint = 900
lensHeight = 200
numSegments = 500
n1 = 1.0
n2 = 1.495

light = []
lens1 = Lens1(focalPoint, lensHeight, numSegments, n1, n2)
finishLens = completeLens()

n1 = 1.495
n2 = 1.0
scaleFactor = 0.1
lens2 = Lens2(n1, n2, focalPoint, scaleFactor)


lens1.Inner("Middle")
lens1XY = finishLens.lowerHalf(lens1.lensXY)
#print(lens1XY)



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
    lightBeam.rayLens1Intersection(lens1)

for lightBeam in light:
    lightBeam.refraction(lens1)

print()
for lightBeam in light:
    lightBeam.rayExtension(5)
    #print(f"M52 lightBeam.angle {lightBeam.angle}")

print()

#Find focal point to calculate second lens
lens2.findRayMidline(light)

lens2.formLens(light)

lens2XY = finishLens.lowerHalf(lens2.lensXY)
#print(lens2XY)

corners = []
corners = finishLens.lensCorners(lens1XY, lens2XY)
#print(f"corners {corners}")



for lightBeam in light:
    lightBeam.rayLens2Intersection(lens2)
    pass



for lightBeam in light:
    lightBeam.refraction(lens2)
    #print(f"M73 lightBeam.angle {lightBeam.angle}")
    pass

#print(f"type(light): {type(light)}")
#print(f"light: {light[0].ray}")

for lightBeam in light:
    #lightBeam.rayExtension(100)
    pass


#******************************************8
toScreen = Display()



#drawLens
#toScreen.draw_Lens(lens1.lensXY, "RED")
toScreen.drawLensLines(lens1.lensXY)

#toScreen.draw_Lens(lens2.lensXY, "RED")
toScreen.drawLensLines(lens2.lensXY)

for lightBeam in light:
    #toScreen.draw_Source(lightBeam.ray)
    pass

for lightBeam in light:
    #toScreen.draw_Rays(lightBeam.ray)
    pass


for line in lens2.midRayLine:
    #toScreen.draw_Rays(line)
    #print(line)
    pass

# ************** COPY
toScreen.drawLensLines(lens1XY)
toScreen.drawLensLines(lens2XY)
toScreen.drawLensLines(corners[0])
toScreen.drawLensLines(corners[1])
toScreen.drawLensLines(corners[2])
toScreen.drawLensLines(corners[3])

#toScreen.draw_FocalPoint(lens1.fp)
toScreen.display_to_screen()


