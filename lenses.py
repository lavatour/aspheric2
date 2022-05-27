import math
from  calculations import LinAlg


class Lens():
    def __init__(self, focalPoint, lensHeight, numSegments, n1, n2):
        self.fp = focalPoint
        self.lensHeight = lensHeight
        self.n1 = n1
        self.n2 = n2
        self.numSegs = numSegments
        self.segmentAngle = []
        self.dy = self.lensHeight / self.numSegs
        self.lensXY = [[0.0, 0.0]]


    def segments(self):
        tempXY = [[0, 0]]
        for i in range(self.numSegs):
            y = self.lensXY[-1][1] + self.dy
            xDist = self.fp - self.lensXY[-1][0]
            thetaRay = math.atan(y / xDist)
            self.theta1 = math.atan((-self.n2 * math.sin(thetaRay)) / (1 - self.n2 * math.cos(thetaRay)))
            self.theta2 = math.asin(math.sin(self.theta1) / self.n2)
            self.segmentAngle.append(math.pi / 2 - self.theta1)
            dx = self.dy / math.tan(self.segmentAngle[i])
            x = self.lensXY[-1][0] + dx
            self.lensXY.append([x, y])

            #print(f"30 thetaRay, theta1, theta2, segAngle, dx, x =  {thetaRay, self.theta1, self.theta2, self.segmentAngle[i]*180/math.pi, dx, x}")




