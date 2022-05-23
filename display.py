import pygame

class Display():
    """Set colors, screeh size, display object, OFFSET_X, OFFSET_Y, to center displayed objects.
    Display caption, fill color
    """

    def __init__(self):
        pygame.init()

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.width = 1620
        self.height = 900
        self.size = (self.width, self.height)
        self.display = pygame.display.set_mode(self.size)
        self.OFFSET_X =  int(self.width/2 - 500)
        self.OFFSET_Y = int(self.height/2)
        pygame.display.set_caption("Lens")
        self.display.fill(self.WHITE)

    def draw_Lens1(self, surface):
        for point in surface:
            x = point[0]
            y = point[1]
            pygame.draw.circle(self.display, self.RED,(x + self.OFFSET_X,-y + self.OFFSET_Y),1,1)


    def draw_Source(self, source):
        x = source[0]  + self.OFFSET_X
        y = -source[1] + self.OFFSET_Y  # SET NEGATIVE TO MAKE SOURCE ON UPPER HALF IN IMAGE
        pygame.draw.circle(self.display, self.RED,( x, y), 2, 2)    #

    def draw_Rays(self, ray):
        """display rays"""
        for p in range(len(ray)-1):
            #print(f"ray = {ray}")
            x1, y1 = ray[p][0], -ray[p][1]
            x2, y2 = ray[p+1][0], -ray[p+1][1]

            pygame.draw.line(self.display, self.RED, [x1 + self.OFFSET_X, y1 + self.OFFSET_Y], [x2 + self.OFFSET_X, y2 + self.OFFSET_Y])


    def display_to_screen(self):
        """This is needed to display everything to the screen"""
        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():  # this gets any event on the screen
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
        quit()