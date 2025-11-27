#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer


win_width = 600
win_height = 600
score1 = 0
score2 = 0 #сколько монстров подбито
clock = time.Clock()
FPS = 60

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('fon2.jpg'), (win_width, win_height))

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.set_volume(0.2) #- сбавить звук
#mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 50:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 50:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 50:
            self.rect.y += self.speed



player_1 = Player('p.png', 50, 250, 30, 150, 10)
player_2 = Player('p2.png', 550, 250, 20, 100, 10)
ball = GameSprite("dp.png", 300, 300, 50, 50, 15)



#cоздание шрифта
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 80)
finish = True
run = True


while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
        
    if finish:
        window.blit(background, (0,0))
        player_1.update_l()
        player_1.reset()
        player_2.update_r()
        player_2.reset()

        
        ball.reset()
        
        """

# столкновения
        collide = sprite.groupcollide(monsters, bullets, True, True)
        for c in collide:
            score+=1
            monster = Enemy("ufo.png", randint(0, 610), 0, 80,50, randint(1,5))
            monsters.add(monster)
#текст на экране
        text_lose = font1.render('Пропущено: ' +str(lost), 1,(255,255,255))
        window.blit(text_lose,(10,40))
        text = font1.render('Счёт: ' +str(score), 1,(255,255,255))
        window.blit(text,(10,10))
        win = font2.render('WIN', 1,(255,255,255))
        lose = font2.render('Lose', 0,(255,255,255))
#Победа
        if score>=10:
            window.blit(win,(250,250))
            finish = False



#Поражение
        if sprite.spritecollide(ship, monsters, False) or lost >22:
            window.blit(lose,(250,250))
            finish = False
        if sprite.collide_rect(ship, ast):
            window.blit(lose,(250,250))
            finish = False
"""
    display.update()
    clock.tick(FPS)
