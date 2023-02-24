import pygame
import pygame as pg
import sys

FPS = 60
WIN_WIDTH = 600
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SPEED = 5

clock = pg.time.Clock()
sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

r = 50
x = WIN_WIDTH // 2
y = WIN_HEIGHT // 2

sc.fill(WHITE)


class Circle:
    def __init__(self, x, y, r, RED, speed):
        self.x = x
        self.y = y
        self.r = r
        self.RED = RED
        self.speed = speed

    def draw(self):
        pg.draw.circle(sc, self.RED, (self.x, self.y), self.r)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.y -= self.speed
        elif self.y < 200:
            self.y += self.speed


circle = Circle(x, y, r, RED, SPEED)

while True:
    clock.tick(FPS)
    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    sc.fill(WHITE)
    circle.draw()
    circle.move_by_keys()
    circle.jump()
    pg.time.delay(10)
    pg.display.update()



