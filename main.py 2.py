import pygame as pg
import sys

FPS = 60
WIN_WIDTH = 600
WIN_HEIGH = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pg.time.Clock()
sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGH))

r = 50
x = WIN_WIDTH // 2
y = WIN_HEIGH // 2

sc.fill(WHITE)
class Circle:
    def __init__(self, x, y, r, RED):
        self.x = x
        self.y = y
        self.r = r
        self.RED = RED

    def draw(self):
        pg.draw.circle(sc, RED, (x, y), r)

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] == 1:
            self.y -= 1
        if keys[pg.K_DOWN] == 1:
            self.y += 1
        if keys[pg.K_LEFT] == 1:
            self.x -= 1
        if keys[pg.K_RIGHT] == 1:
            self.x += 1

circle = Circle(x, y, r, RED)
circle.draw()
circle.move_by_keys()
print(circle.move_by_keys)
pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)


