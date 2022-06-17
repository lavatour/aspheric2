import math
from  calculations import LinAlg
class Lens1():

    def __init__(self, focalPoint, lensHeight, numSegments, n1, n2):
        self.fp = focalPoint
        self.lensHeight = lensHeight
        self.n1 = n1
        self.n2 = n2
        self.numSegs = numSegments
        self.segmentAngle = []
        self.dy = self.lensHeight / self.numSegs
        self.lensXY = [[0.0, 0.0]]
        self.lensXYMid = [[0.0, 0.0]]

    # print(f"30 thetaRay, theta1, theta2, segAngle, dx, x =  {thetaRay, self.theta1, self.theta2, self.segmentAngle[i]*180/math.pi, dx, x}")

    def findTheta1_Theta2(self, thetaR, n1, n2):
        """findTheta1_Theta2 documentation
        n1 sin(theta1) = n2 sin(theta(2)
        theta1 = theta2 - thetaR
        theta2 = theta1 + thetaR
        thetaR = theta2 - theta1
        n1 sint(theta1) = n2 sin(theta2)
        n1 sin(theta1) = n2 sin(theta1 + thetaR)
        n1 sin(theta1) = n2 sin(theta1) cos(thetaR) + n2 sin(thetaR) cos(theta1)
        n1 sin(theta1) - n2 sin(theta1) cos(thetaR) = n2 sin(thetaR) cos(theta1)
        sin(theta1) [ n1 - n2 cos(thetaR)] = n2 sin(thetaR) cos(theta1)
        sin(theta1) / cos(theta1) = [ n2 sin(thetaR) ] / [n1 - n2 cos(thetaR)]
        tan(theta1) = [ n2 sin(thetaR) ] / [n1 - n2 cos(thetaR)]
        theta1 = atan[ n2 sin(thetaR) ] / [n1 - n2 cos(thetaR)]
        ****
        n1 sin(theta1) = n2 sin(theta2)
        sin(theta2) = n1 sin(theta1) / n2
        theta2 = asin[ n1 sin(theta1) / n2 ]
        """

        theta1 = math.atan(n2 * math.sin(thetaR)  / (n1 - n2 * math.cos(thetaR)))
        theta2 = math.asin( n1 * math.sin(theta1) / n2 )
        return theta1, theta2


    def Inner(self, position):
        """Calculate lens segment position and angle to focus to point fp
        Build lens segment by segment.
        1. dY = lens height / number of lens segments
        2. y = next point for calculating ray angles
            y = lens[-1][1] + dy/2
        3. xDist = dist from fp to middle of current segment
            middle current segment approx = lens[-1][0] + dy / tan(segmentAngle)
            xDist = fp = (lens[-1][0] + dy/2 / tan(segmentAngle[-1])
        4. final ray angle from to focal point to a point dy/2 directly above the top of last ray segment.
            Called in calculateAngles

            finalRayAngle = atan(atan(y / xDist)
        5. thetaR: change in angle from initialRayAngle to finalRayAngle
        6. Theta1 per double angle equation, n1, n2, thetaR
        7. Theta2 from theta1, n1, n2
        8. segment angle
        9. dX from dY and segment angle
        10. append [lens[-1][0] + dx, lens[-1][1] + dy] to lens
        """

        initialRayAngle = 0.0

        for segNum in range(self.numSegs):

            y = self.lensXY[-1][1] + self.dy / 2
            #print(f"segNum {segNum}    dy {self.dy}    lensXY[-1 {self.lensXY[-1]}    dy/2 {self.dy/2}")
            if len(self.segmentAngle) > 0:
                xDist = self.lensXY[-1][0] + self.dy / math.tan(self.segmentAngle[-1]) - self.fp
            else:
                xDist = (self.lensXY[-1][0] - self.fp)

            finalRayAngle = math.atan(y / xDist)

            thetaR = finalRayAngle - initialRayAngle
            n1, n2 = self.n1, self.n2
            theta1, theta2 = self.findTheta1_Theta2(thetaR, n1, n2)
            self.theta1, self.theta2 = theta1, theta2
            print(f"theta1 = {theta1}   theta2 {theta2}")

            self.segmentAngle.append(initialRayAngle - self.theta1 + math.pi/2)
            #print(f"y = {y}   xDist = {xDist}   theta1 = {self.theta1*180/math.pi}   segmentAngle = {self.segmentAngle[-1]*180/math.pi}")
            # segment angle = initial ray angle - angle of incidence + 90


            dx = self.dy / math.tan(self.segmentAngle[segNum])
            # dx from dy and segment angle

            self.lensXY.append([self.lensXY[-1][0] + dx, self.lensXY[-1][1] + self.dy])
            #print(f"dx = {dx}   finalRayAngle = {finalRayAngle*180/math.pi}")
            #print()
            # print(f"segAngle = {self.segmentAngle[-1]*180/math.pi}")


class Lens2():


    def __init__(self, n1, n2, position):

        self.n1 = n1
        self.n2 = n2
        self.position = position
        self.segmentAngle = []
        self.lensXY = []


    def findfocalPoint(self, light):

        points = []

        for lightBeam in light:
            #print(lightBeam.ray)
            ry = lightBeam.ray
            focalLine = [0,0], [100, 0]
            #print(f"ry = {ry}")
            #print(ry[-2][0])
            rayLine = [ry[-2][0], ry[-2][1]], [ry[-1][0], ry[-1][1]]
            fX, fY = LinAlg.line_intersection(rayLine, focalLine)
            #print((f"x,y = {fX, fY}"))
            points.append(fX)

        #print(f"focalPoints = {points[0], points[-1]}")

        min, fp, max = LinAlg.median(points)
        #print(f"min = {min}   fp = {fp}   max = {max}")
        return fp


    def align1(self, light):

        angles = []
        degrees = []

        for lightbeam in light:
            angles.append(lightbeam.angle[-1])
            degrees.append(lightbeam.angle[-1]*180/math.pi)
        angles.sort()
        degrees.sort()
        minAngle = angles[0] - 0.01
        maxAngle = angles[-1] + 0.01

        #print(f"68 angles = {angles}")
        #print(f"69 degrees = {degrees}")


    def scale(self, scaleFactor, lens1):

        self.scaleFactor = scaleFactor
        #print(f"lens1XY = {lens1.lensXY}")

        for xy in lens1.lensXY:
            x = xy[0]*scaleFactor + lens1.fp * (1 - scaleFactor)
            y = xy[1]*scaleFactor
            self.lensXY.append([x, y])
        #print(f"Lens2xy = {self.lensXY}")


    def align(self, light):

        """Calculate lens segment position and angle to align light"""
        self.rayData = []

        for i in light:
            self.rayNumber = i.rayNumber
            initialRayAngle = i.angle[-1]
            finalRayAngle = 0.0
            thetaR = finalRayAngle - initialRayAngle
            self.theta1, self.theta2 = Lens1.findTheta1_Theta2(self, thetaR, self.n1, self.n2)
            #print(f"n2 = {self.n2}   n1 = {self.n1}")
            print(f"thetaR {thetaR*180/math.pi}   theta1 {self.theta1*180/math.pi}   theta2 {self.theta2*180/math.pi}")
            #self.theta1 = math.atan((-self.n2 * math.sin(thetaR)) / (self.n1 - self.n2 * math.cos(thetaR)))
            #self.theta2 = math.asin(self.n1 * math.sin(self.theta1) / self.n2)
            #print(f"thetaR {thetaR*180/math.pi}   theta1 {self.theta1 * 180 / math.pi}   theta2 {self.theta2 * 180 / math.pi}")

            self.segmentAngle.append(initialRayAngle - self.theta1 + math.pi / 2)
            print(f"segmentAntle = {self.segmentAngle[-1]*180/math.pi}")
            self.segmentAngle.append(initialRayAngle - self.theta1 + math.pi / 2)
            #print(f"segmentAntle = {self.segmentAngle[-1] * 180 / math.pi}")

            x1, y1 = i.ray[-2][0],  i.ray[-1][1]
            x2, y2 = i.ray[-1][0],  i.ray[-1][1]
            rLine = [x1, y1], [x2, y2]
            #print(f"initialRayAngle {initialRayAngle*180/math.pi}   finalRayAngle = {finalRayAngle*180/math.pi}     thetaR = {thetaR*180/math.pi}    n1 = {self.n1}     n2 = {self.n2}")
            #print(f"theta1 = {self.theta1*180/math.pi}    theta2 = {self.theta2*180/math.pi}    segmentAngle = {self.segmentAngle[-1]*180/math.pi}")

            m = math.tan(i.angle[-1])
            m2 = (i.ray[-2][1] - i.ray[-1][1]) / (i.ray[-2][0] - i.ray[-1][0])
            x1 = i.ray[-2][0]
            y1 = i.ray[-2][1]
            fp = (m*x1 - y1) / m
            thetaRay = i.angle[-1]
            self.rayData.append([self.rayNumber, m, m2, x1, y1, fp])
            #print(f"raynum, m, m1, x1, y1, fp {[self.rayNumber, round(m, 3), round(m2, 3), round(x1, 3), round(y1, 3), round(fp, 3)]}")
            #print(f"thetaN = {thetaN * 180 / math.pi}   segAngle = {segmentAngle*180/math.pi} corSegAng = {corSegAng*180/math.pi}")

