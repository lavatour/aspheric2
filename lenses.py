import math

class Lens():
    def __init__(self, focalPoint, lensHeight, dy, n1, n2):
        self.f_point = focalPoint
        self.lensHeight = lensHeight
        self.dy = dy
        self.n1 = n1
        self.n2 = n2
        self.vertices = [[0, 0]]


