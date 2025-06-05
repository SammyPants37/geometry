# website for pygame: https://repl.it/languages/pygame
# importing the codes settings and sprite classes
from settings import *
from sprites import *

# setting up the pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Geometry')
clock = pygame.time.Clock()


# this is a function that changes the mouse position if it gets close enough to a point
def keepThere(mouse, point, pos):
    changed = False
    po = (pos[0], pos[1])
    touch = pygame.sprite.spritecollide(mouse, point, False) #, False)
    point.update()
    for t in touch:
        po = t.center
        t.grow()
        changed = True
    return po, changed

# this makes text sprites and a sprite to track where the mouse is
t1 = HelpText()
allSprites.add(t1)
t2 = HelpText()
t2.clear()
allSprites.add(t2)
mouseSprite = MouseSprite((50, 50))

while running:
    # process input
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            # exit the program
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                draw = 2
                # start drawing circles
            if event.key == pygame.K_p:
                draw = 1
                # start drawing points
            if event.key == pygame.K_l:
                draw = 3
                # start drawing lines
            if event.key == pygame.K_x:
                pygame.sprite.Group.empty(allSprites)
                allSprites.add(t1)
                allSprites.add(t2)
                # clear all sprites and add back the text
        if event.type == pygame.MOUSEBUTTONUP:
            p1, change1 = keepThere(mouseSprite, points, event.pos)
            p2, change = keepThere(mouseSprite, points, event.pos)
            if draw == 2:  # this checks if your drawing circles
                if not thingProcess:
                    # this checks to see if your not already drawing a circle. if
                    # not then it draws the center of the circle and what
                    # the circle would look like if you clicked again
                    thingProcess = True
                    c = CircleSprite(p1, p2)
                    allSprites.add(c)
                else:
                    thingProcess = False
                    # tell program to stop updating what the circle looks like
            elif draw == 3:  # this checks if your drawing lines
                if not thingProcess:
                    # this checks to see if your not already drawing a line. if
                    # not then it draws one end of the line and what
                    # the line would look like if you clicked again
                    thingProcess = True
                    line = Line(p1)
                    allSprites.add(line)
                else:
                    thingProcess = False
                    # tell program to stop updating what the circle looks like
                    if not change:
                        # this checks if it needs to draw a point or if you are
                        # connecting the end of the line to a existing point
                        p = Point(p2)
                        allSprites.add(p)
            elif draw == 1 and not change:
                # this checks that you're drawing points and then draws it
                p = Point(p1)
                allSprites.add(p)
        if event.type == pygame.MOUSEMOTION:
            mouseSprite.move(event.pos)
            # update the position of the mouse
            p2, change = keepThere(mouseSprite, points, event.pos)
            # update the second point
            if thingProcess and draw == 2:
                # if you are drawing a circle then it updates what the circle
                # looks like
                c.change(p2)
            elif thingProcess and draw == 3:
                # if you are drawing a line then it updates what the line
                # looks like
                line.change(p2)
    # update the text
    if draw == 1:
        t2.point()
    elif draw == 2:
        t2.circle(thingProcess)
    elif draw == 3:
        t2.line(thingProcess)
    # render
    # draws over every thing, redraws everything, puts everything on screen
    # then waits until it has been 1/30th of a second
    screen.fill(WHITE)
    allSprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

# quit
pygame.quit()
sys.exit()
