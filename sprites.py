# importing the codes settings
from settings import *


# define a sprite to keep track of where the mouse is
class MouseSprite(pygame.sprite.Sprite):
    def __init__(self, spot):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3, 3))
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = spot
        self.center = self.rect.center

    def move(self, spot):
        self.rect.center = spot


# defining a sprite that tells user how to draw shapes
class HelpText(pygame.sprite.Sprite):
    def __init__(self):
        # initialising the sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = basicFont.render('p: point  c: circle  l: line  x: clear', True, BLACK, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 5)

    def clear(self):
        # this clears the area
        self.image = basicFont.render(' ', True, BLACK, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 25)

    def circle(self, thingProcess):
        # this draws instructions on how to make circles
        if not thingProcess:
            self.image = basicFont.render('click to make the center of a circle', True, BLACK, WHITE)
        else:
            self.image = basicFont.render('click to make the outside of the circle', True, BLACK, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 25)

    def point(self):
        # this draws instructions for making a point
        self.image = basicFont.render('click to make a point', True, BLACK, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 25)

    def line(self, thingProcess):
        # this draws instructions for making a line
        if not thingProcess:
            self.image = basicFont.render('click to make one end of the line', True, BLACK, WHITE)
        else:
            self.image = basicFont.render('click to make the other end of the line', True, BLACK, WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 25)


# defining a line sprite
class Line(pygame.sprite.Sprite):
    def __init__(self, p1):
        # initialising the sprite
        global allSprites
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.p = p1
        p = Point(p1)
        allSprites.add(p)

    def change(self, p2):
        # updating what the line looks like
        self.image.fill(GREEN)
        pygame.draw.line(self.image, BLACK, self.p, p2, 2)


# defining a point sprite
class Point(pygame.sprite.Sprite):
    def __init__(self, p1):
        # initialising the sprite
        pygame.sprite.Sprite.__init__(self)
        global points
        self.image = pygame.Surface((14, 14))
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
        self.radius = 2
        pygame.draw.circle(self.image, BLUE, (7, 7), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (p1[0], p1[1])
        self.center = self.rect.center
        points.add(self)

    def grow(self):
        # this grows the point when the mouse is on it
        self.image.fill(GREEN)
        self.radius = 5
        pygame.draw.circle(self.image, RED, (7, 7), self.radius)

    def update(self):
        # this shrinks the sprite when the mouse is not on it
        self.image.fill(GREEN)
        self.radius = 2
        pygame.draw.circle(self.image, BLUE, (7, 7), self.radius)


# defining a circle sprite
class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, p1, p2):
        # initialising the sprite
        global allSprites
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)

        radius = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        if radius < 3:
            radius = 4
        pygame.draw.circle(self.image, BLACK, p1, int(radius), 2)
        self.center = p1

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        p = Point(p1)
        allSprites.add(p)

    def change(self, p2):
        # this updates what the circle looks like
        self.image.fill(GREEN)
        p1 = self.center
        radius = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        if radius < 3:
            radius = 4
        pygame.draw.circle(self.image, BLACK, self.center, int(radius), 2)
