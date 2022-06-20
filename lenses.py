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
            #print(f"theta1 = {theta1}   theta2 {theta2}")

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


    def __init__(self, n1, n2, focalPoint, scaleFactor):

        self.n1 = n1
        self.n2 = n2
        self.fp = focalPoint
        self.scaleFactor = scaleFactor
        #self.position = position
        self.segmentAngle = []
        self.lensXY = []


    def findRayMidline(self, light):
        """
        I. Find midline between adjacent rays
            A. ray[i] and ray[i+1] intersection: midRX1, midY1
            B. midRay Angle, average angles ray[i] & ray[i+1]
            C. midRay point 2, midRX2 = midRX1 + cos(midRAngle)...
            D. define midRayLine"""
        for i in range(len(light) - 1):
            print(light[i].ray[-1])

    def scale(self, lens1):

        scaleFactor = self.scaleFactor
        #print(f"lens1XY = {lens1.lensXY}")

        for xy in lens1.lensXY:
            x = xy[0]*scaleFactor + lens1.fp * (1 - scaleFactor)
            y = xy[1]*scaleFactor
            self.lensXY.append([x, y])
        #print(f"Lens2xy = {self.lensXY}")


    def align(self, light):
        """Calculate lens segment position and angle to align light
                1. lENSxy[0][0] scaleFactor
                2. for i in range (len(rays)):
                    A. ThetaR = finalAngle - InitialAngle
                    B. theta1, theta2
                    C. middleAngle: imaginary ray between real rays.
                    D. middleRayLine
                        i. midpointLens1Segment
                3 for j in range(len(middleRayLine)):
                    E. calculate segmentAngle
                3. for i in range (len(segmentAngle)):
                    A. segmentLine = [[x1, y1], [x2,y2]
                    B. segLine middleRay intersection

                    d. calculate lensSegment and ray intersection
                        i. rayLine
                        ii. segmentLine
                    """
        # 1. lENSxy[0][0] scaleFactor
        self.lensXY.append([self.fp - self.scaleFactor*self.fp, 0])
        middleRayLine = []
        # 2. for i in range (len(rays)):

        for i in range(len(light)):
            # A. ThetaR = finalAngle - InitialAngle
            initialRayAngle, finalRayAngle = light[i].angle[-1], 0.0
            thetaR = finalRayAngle - initialRayAngle
            # B. Calculate theta1, theta2
            self.theta1, self.theta2 = Lens1.findTheta1_Theta2(self, thetaR, self.n1, self.n2)
            # C Calculate middle Angle: imaginary ray between real rays.
            if i < len(light) - 1:
                middleAngle = ( light[i].angle[-1] + light[i+1].angle[-1] ) / 2
            else:
                middleAngle = 2 * light[i].angle[-1] - light[i-1].angle[-1]
            # D.Calculate middleRayLine

            middleRayLine.append( [[self.fp, 0.0], [self.fp+100*math.cos(middleAngle), 0.0 + 100*math.sin(middleAngle)]] )
            #print(f"middleRay = {middleAngle*180/math.pi}  lightAngle {light[i].angle[1]*180/math.pi}")

            # E. calculate segmentAngle
            self.segmentAngle.append(initialRayAngle - self.theta1 + math.pi / 2)
        #print(f"middleRayLine {middleRayLine}  \n {len(middleRayLine)}")

        numsegs = len(self.segmentAngle)

        for i in range(len(self.segmentAngle)):
            # A. segmentLine
            segX = self.lensXY[i][0] + math.cos(self.segmentAngle[i])
            segY = self.lensXY[i][1] + math.sin(self.segmentAngle[i])
            segmentLine = [self.lensXY[i], [segX, segY]]
            # B. segLine middleRay intersection
            lX, lY = LinAlg.line_intersection(segmentLine, middleRayLine[i])
            #print(f"segLine = {segmentLine}, \nmiddleLine = {middleRayLine[i]}")
            #print(f"lx, ly = {lX, lY}")
            #****print(light[i].ray[-1])
            self.lensXY.append([lX, lY])
            #print(light[i].ray[-1])
            #print()

