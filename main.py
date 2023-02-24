import pygame as pg
pg.init()
win = pg.display.set_mode((600, 400))
color = (225, 225, 225)
win.fill(color)
pg.display.update()
FPS = 60
WIN_WIDTH = 600
WIN_HEIGH = 400
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

clock = pg.time.Clock()
sc = pg.display.set_mode((WIN_WIDTH, WIN_HEIGH))




class Circle:
    rad = 40
    x = WIN_WIDTH // 2
    y = WIN_HEIGH // 2
    col = (255, 150, 100)

    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col

    def draw(self):
        pg.draw.circle(win, self.col, (self.x, self.y), self.rad)

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


    def jump(self):
        jump_counter = 1
        is_jump = False
        if is_jump is True:
            if jump_counter >= -30:
                self.y -= jump_counter
                jump_counter -= 2
            else:
                jump_counter = 30
                is_jump = False
    FPS = 30
    clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    clock.tick(FPS)












