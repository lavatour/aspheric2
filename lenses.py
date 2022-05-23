import math



class Lens():
    def __init__(self, focalPoint, lensHeight, numSegments, n1, n2):
        self.f_point = focalPoint
        self.lensHeight = lensHeight
        self.n1 = n1
        self.n2 = n2
        self.numSegs = numSegments
        self.dy = self.lensHeight / self.numSegs
        self.lensXY = [[0.0, 0.0]]

    def coordinates(self):
        """ Set y Coordinates """
        for i in range(1, self.numSegs +1):
            self.lensXY.append([0, self.lensXY[0][1] + i*self.dy])





