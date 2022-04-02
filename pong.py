from random import randint
import pygame as pg

screenWidth = 600
screenHeight = 400

class Player(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pg.draw.rect(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 300:
            self.rect.y = 300

class Ball(pg.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pg.image.load('img.png')
        self.image = pg.transform.scale(self.image, (width,height))

        self.velocity = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

pg.init()
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("PongGame")

player1 = Player((255,255,255), 10, 100)
player1.rect.x = 20
player1.rect.y = 200

player2 = Player((255,255,255), 10, 100)
player2.rect.x = 580
player2.rect.y = 200

ballWidth = 100
ballHeight = 150
ball = Ball(ballWidth, ballHeight)
ball.rect.x = 300
ball.rect.y = 200

sprites = pg.sprite.Group()

sprites.add(player1)
sprites.add(player2)
sprites.add(ball)

Run = True
clock = pg.time.Clock()
while Run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player1.moveUp(5)
    if keys[pg.K_s]:
        player1.moveDown(5)
    if keys[pg.K_UP]:
        player2.moveUp(5)
    if keys[pg.K_DOWN]:
        player2.moveDown(5)

    sprites.update()

    if ball.rect.x >= screenWidth - ballWidth:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x < 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= screenHeight - ballHeight:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pg.sprite.collide_mask(ball, player1) or pg.sprite.collide_mask(ball, player2):
        ball.bounce()

    screen.fill((0,0,0))
    sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)

pg.quit()
