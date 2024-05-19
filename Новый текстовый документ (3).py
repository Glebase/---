from pygame import *
font.init()
game=True
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>=5:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_s] and self.rect.y<650:
            self.rect.y = self.rect.y + self.speed
window = display.set_mode((700,500))
display.set_caption('пинг-понг')
background = transform.scale(image.load("hockey.jpg"),(700, 500))
window.blit(background,(0,0))

player_left = Player('player.png',50,200,5,50,100)
player_right = Player('player2.png',600,200,5,50,100)
ball = GameSprite('9209.png',200,200,5,50,50)
font1 = font.Font(None, 70)
won1 = font1.render('Player 1 won!', True, (255,0,0))
won2 = font1.render('Player 2 won!',True, (255,0,0))

clock = time.Clock()
fps = 60
while game == True:
    player_left.reset()
    player_right.reset()
    ball.reset()















    display.update()
    clock.tick(fps)
