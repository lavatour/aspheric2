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

    # print(f"30 thetaRay, theta1, theta2, segAngle, dx, x =  {thetaRay, self.theta1, self.theta2, self.segmentAngle[i]*180/math.pi, dx, x}")

    def Inner(self):
        """Calculate lens segment position and angle to focus to point fp
        Build lens segment by segment.
        1. dY = lens height / number of lens segments
        2. y = next point for calculating ray angles
            y = lens[-1][1] + dy
        3. xDist = distance from fp to top of last ray segment
            xDist = (lens[-1][0] + dy / tan(segmentAngle[-1]) - fp
        4. final ray angle from to focal point to a point dy directly above the top of last ray segment.
            finalRayAngle = math.atan2(xDist, y)
            ***Check that angle is correct: negative.***
        5. thetaR: change in angle from initialRayAngle to finalRayAngle
            Called in calculateAngles
            thetaR = finalRayAngle - initialRayAngle
        6. Theta1 per double angle equation, n1, n2, thetaR
            Called in calculateAngles
            self.theta1 = math.atan((-self.n2 * math.sin(thetaR)) / (self.n1 - self.n2 * math.cos(thetaR)))
        7. Theta2 from theta1, n1, n2
            called in calculateAngles
            self.theta2 = math.asin(self.n1 * math.sin(self.theta1) / self.n2)
        8. segment angle
            called in calculateAngles
            self.segmentAngle.append(math.pi / 2 - self.theta1 + initialRayAngle)
        9. dX from dY and segment angle
        10. append [lens[-1][0] + dx, lens[-1][1] + dy] to lens
            The entire segment will focus short of the focal point.
        """
        segmentAngle = []
        initialRayAngle = 0.0

        for i in range(self.numSegs):
            y = self.lensXY[-1][1] + self.dy
            # y coordinate of lens segments. This is the top of the segment.
            # This makes the lens focus short of the desired focal pt.

            xDist = self.fp - self.lensXY[-1][0]
            # distance from point on lens to focal point
            finalRayAngle = math.atan(y / xDist)
            # angle of ray from point on lens to desired focal point

            thetaR = finalRayAngle - initialRayAngle
            # The change in ray direction = theta2 - theta1

            self.theta1 = math.atan((-self.n2 * math.sin(thetaR)) / (self.n1 - self.n2 * math.cos(thetaR)))
            # theta 1 from angle in derived formula given change in angle from 0 to thetaR
            # theta 1 = angle of incidence

            self.theta2 = math.asin(self.n1 * math.sin(self.theta1) / self.n2)
            # angle of refraction using snells law

            self.segmentAngle.append(math.pi / 2 - self.theta1 + initialRayAngle)
            # segment angle = 90 - angle of incidence + initial ray angle

            dx = self.dy / math.tan(self.segmentAngle[i])
            # dx from dy and segment angle
            x = self.lensXY[-1][0] + dx
            self.lensXY.append([x, y])
            #print(f"finalRayAngle = {finalRayAngle*180/math.pi}")
            # print(f"segAngle = {self.segmentAngle[-1]*180/math.pi}")

    def Middle(self):
        """Calculate lens segment position and angle to focus to point fp
        Build lens segment by segment.
        1. dY = lens height / number of lens segments
        2. y = next point for calculating ray angles
            y = lens[-1][1] + dy/2
        3. xDist = dist from fp to middle of current segment
            middle current segment approx = lens[-1][0] + dy / tan(segmentAngle)
            xDist = fp = (lens[-1][0] + dy/2 / tan(segmentAngle[-1])
        4. final ray angle from to focal point to a point dy directly above the top of last ray segment.
            Called in calculateAngles

            finalRayAngle = atan(
        5. thetaR: change in angle from initialRayAngle to finalRayAngle
        6. Theta1 per double angle equation, n1, n2, thetaR
        7. Theta2 from theta1, n1, n2
        8. segment angle
        9. dX from dY and segment angle
        10. append [lens[-1][0] + dx, lens[-1][1] + dy] to lens
            The entire segment will focus short of the focal point.
        """

        segmentAngle = []
        initialRayAngle = 0.0
        self.lensXYMiddle = [[0.0, 0.0]]

        for i in range(self.numSegs):
            y = self.lensXYMiddle[-1][1]
            # y coordinate of lens segments

            xDist = self.fp - self.lensXYMiddle[-1][0]
            # distance from bottom of lens segment to intended focal point

            finalRayAngle = math.atan(-(y + self.dy/2) / xDist)  # -dy/2 to set angle at center of lens segment

            #print(f"65 xDist {xDist}   y + dy/2 {y + self.dy/2}")
            #print(f"75 y {y}   lensXYMiddle {self.lensXYMiddle}    xDist {xDist}   finalRayAngle = {finalRayAngle * 180 / math.pi}")
            #TODO rewrite code to use atan2
            thetaR = finalRayAngle - initialRayAngle
            theta1 = math.atan((-self.n2 * math.sin(thetaR)) / (self.n1 - self.n2 * math.cos(thetaR)))
            theta2 = math.asin(self.n1 * math.sin(theta1) / self.n2)
            #print(f"initialRayAngle {initialRayAngle*180/math.pi}   finalRayAngle {finalRayAngle*180/math.pi}   thetaR {thetaR*180/math.pi}   theta1 {theta1*180/math.pi}   theta2 {theta2*180/math.pi}")
            segmentAngle.append(math.pi / 2 + theta1 + initialRayAngle)
            #print(f"segmentAngle = {segmentAngle[-1]*180/math.pi}")
            dx = self.dy / math.tan(segmentAngle[i])
            x = self.lensXYMiddle[-1][0] + dx
            y = self.lensXYMiddle[-1][1] + self.dy
            self.lensXYMiddle.append([x, y])

            #print(f"segmentAngle {segmentAngle}   dx {dx}")
#        print(f"lensOuter {self.lensXYOuter} \nlenOuter = {len(self.lensXYOuter)} {self.lensXYOuter[0], self.lensXYOuter[-1]}")
#        print(f"lensInner {self.lensXY} \nlen(lensInner) {len(self.lensXY)}")
#        print(f"lensMiddle {self.lensXYMiddle} \nlen(lensMiddle) {len(self.lensXYMiddle)}")

















    def Outer(self):

        segmentAngle = []
        initialRayAngle = 0.0
        self.lensXYOuter = [[0.0, 0.0]]

        for i in range(self.numSegs):
            xDist = self.fp - self.lensXYOuter[-1][0]
            finalRayAngle = math.atan(self.lensXYOuter[-1][1] / xDist)
            thetaR = finalRayAngle - initialRayAngle
            theta1 = math.atan((-self.n2 * math.sin(thetaR)) / (self.n1 - self.n2 * math.cos(thetaR)))
            theta2 = math.asin(self.n1 * math.sin(theta1) / self.n2)
            segmentAngle.append(math.pi / 2 - theta1 + initialRayAngle)
            dx = self.dy / math.tan(segmentAngle[i])
            x = self.lensXYOuter[-1][0] + dx
            y = self.lensXYOuter[-1][1] + self.dy
            self.lensXYOuter.append([x, y])
            #print(f"52 xDist {xDist}   finalRayAngle {finalRayAngle*180/math.pi}   thetaR {thetaR*180/math.pi}")
            #print(f"theta1 {theta1*180/math.pi}   theta2 {theta2*180/math.pi}   segmentAngle {segmentAngle[i]*180/math.pi}")
            #print(f"dx = {dx}   lensXYOuter[-1][1] {self.lensXYOuter[-1][1]}")
        #print(f"segAngle {segmentAngle}")



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
        fp = LinAlg.median(points)
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
            self.theta1 = math.atan((-self.n2 * math.sin(thetaR)) / (self.n1 - self.n2 * math.cos(thetaR)))
            self.theta2 = math.asin(self.n1 * math.sin(self.theta1) / self.n2)
            self.segmentAngle.append(math.pi / 2 + self.theta1 + initialRayAngle)
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




