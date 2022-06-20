import math

from lenses import Lens1
from calculations import LinAlg


class Light():
    """Light class for light objects"""
    def __init__(self, rayNumber, lens):
        self.rayNumber = rayNumber
        # print(f"10 rayNumber = {self.rayNumber}")
        # self.source = [-200, 0]
        # print(f"source = {self.source}")
        self.ray = []
        self.angle = [0.0]
        self.lensCoords = [lens.lensXY[self.rayNumber], lens.lensXY[self.rayNumber + 1]]
        self.segmentNumber = []

    """ LIGHT SOURCES """
    def lightSource(self):
        """First Lest Segment"""
        segmentCenter = (self.lensCoords[0][1] + self.lensCoords[1][1]) / 2
        self.ray.append([-200, segmentCenter])
        # self.ray.append([-100, segmentCenter])
        # print(self.ray)


    def rayLensIntersection(self, lens):
        rX1, rY1 = self.ray[-1][0], self.ray[-1][1]
        rX2, rY2 = rX1 + 100 * math.cos(self.angle[-1]), rY1 + 100 * math.sin(self.angle[-1])
        lineR = [[rY1, rY1], [rX2, rY2]]
        # print(f"31 rayAngle {self.angle[-1]*180/math.pi}, rX1 {rX1}, rY1 {rY1}, rX2 {rX2}, rY2 {rY2} ")

        for i in range(1, len(lens.lensXY)):
            lX1, lY1 = lens.lensXY[i-1][0], lens.lensXY[i-1][1]
            lX2, lY2 = lens.lensXY[i][0], lens.lensXY[i][1]
            lineL = [[lX1, lY1],[lX2, lY2]]
            intersectionPoint = LinAlg.line_intersection(lineR, lineL)

            if intersectionPoint[1] >= lY1 and intersectionPoint[1] <= lY2:
                self.ray.append([intersectionPoint[0], intersectionPoint[1]])
                self.segmentNumber.append(i-1) # i-1 because list starts at 0 and i starts at 1
                #print(f"40 ray {self.ray},   point {intersectionPoint},   rayNumber + 1 {self.rayNumber + 1},    i = {i}")



    def refraction(self, lens):
        """rayNumber + 1 = lens Segment number."""
        #print(f"lens.XY = {lens.lensXY}")
        #print(f"self.segmentNumber[-1] = {self.segmentNumber[-1]}")
        #print(f"segnumbers = {self.segmentNumber}")
        #print(f"lens.segmentAngle[self.segmentNumber[-1]] = {lens.segmentAngle[self.segmentNumber[-1]]}")

        normalAngle = lens.segmentAngle[self.segmentNumber[-1]] - math.pi/2
        unitNormalVector = [math.cos(normalAngle), math.sin(normalAngle)]
        rayUnitVector = [math.cos(self.angle[-1]), math.sin(self.angle[-1])]
        dotProd = LinAlg.dotProd(self, unitNormalVector, rayUnitVector)
        # Compute dot product. if angle is obtuse unitNormalVectro wil be multiplied by -1
        if dotProd < 0:
            unitNormalVector = LinAlg.scalarMultiplication(self, -1, unitNormalVector)
        # Use cross product ot find sin(theta)
        crossProd = LinAlg.crossProd(self, unitNormalVector, rayUnitVector)
        angleOfIncidence = math.asin(crossProd)
        # Compute angle of refraction
        angleOfRefraction = lens.n1 * math.asin(math.sin(angleOfIncidence) / lens.n2)
        #light angle = normal angle + angle of refraction
        lightAngle = self.angle[-1] + normalAngle + angleOfRefraction
        self.angle.append(lightAngle)

        #print(f"51 segmentnumber = {self.segmentNumber[-1]},   segment angle = {lens.segmentAngle[self.segmentNumber[-1]] * 180 / math.pi},   normalAngle = {normalAngle*180/math.pi},    normVector = {unitNormalVector},   rayNormVector = {rayUnitVector}")
        #print(f"52 dotProd = {dotProd},   crossProd = {crossProd},   angleOfIncidence = {angleOfIncidence*180/math.pi},  n1 = {lens.n1}, n1 = {lens.n2},   angleOfRefraction = {angleOfRefraction*180/math.pi}   lightAngle = {lightAngle*180/math.pi}")


    def rayExtension(self, dist):
        dx = dist * math.cos(self.angle[-1])
        dy = dist * math.sin(self.angle[-1])
        self.ray.append([self.ray[-1][0] + dx, self.ray[-1][1] + dy])