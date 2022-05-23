import math

from lenses import Lens
from calculations import LinAlg

class Light():
    """Light class for light objects"""
    def __init__(self, rayNumber, lens):
        self.rayNumber = rayNumber
        self.sourceX = -500
        self.sourceY = 0
        self.ray = []
        self.angle = []
        self.lensCoords = lens.lensXY

    """ LIGHT SOURCES """
    def lightSource(self):
        """Source Points"""
        #print(f"self.lensCoords[self.rayNumber][1] = {self.lensCoords[self.rayNumber][1]}")
        self.sourceY = (self.lensCoords[self.rayNumber][1] + self.lensCoords[self.rayNumber + 1][1]) / 2
        #print(self.sourceY)

