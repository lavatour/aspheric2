import math

from lenses import Lens
from calculations import LinAlg

class Light():
    """Light class for light objects"""
    def __init__(self, rayNumber, lens):
        self.rayNumber = rayNumber
        #print(f"10 rayNumber = {self.rayNumber}")
        #self.source = [-200, 0]
        #print(f"source = {self.source}")
        self.ray = []
        self.angle = []
        self.lensCoords = [lens.lensXY[self.rayNumber], lens.lensXY[self.rayNumber + 1]]
        #print(f"lensCoords = {self.lensCoords}")
        #self.source = []

    """ LIGHT SOURCES """
    def lightSource(self):
        """First Lest Segment"""
        segmentCenter = (self.lensCoords[0][1] + self.lensCoords[1][1]) / 2
        self.ray.append([-200, segmentCenter])
        #self.ray.append([-100, segmentCenter])
        #print(self.ray)

