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
font1 = font.Font(None, 20)
font2 = font.Font(None, 80)
font3 = font.Font(None, 30)


finish = True
run = True
speed_x = 2
speed_y = 3 



while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = True
                ball.rect.x = 300
                ball.rect.y = 300

    if finish:
        window.blit(background, (0,0))
        player_1.update_l()
        player_1.reset()
        player_2.update_r()
        player_2.reset()

        
        ball.reset()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y
        
       

# столкновения c ракеткам
        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1
            speed_y *= -1 
# столкновения cо стеной Х
        if ball.rect.x <-10:
            score2+=1
            ball.rect.x = 300
            ball.rect.y = 300
            speed_x*=-1
        if ball.rect.x>560:
            score1+=1
            ball.rect.x = 300
            ball.rect.y = 300
            speed_x*=-1

# столкновения cо стеной Y
        if ball.rect.y < 0 or ball.rect.y>550:
            speed_y*=-1

     
        
#текст на экране
        text_score1 = font1.render('Счёт черного: ' +str(score1), 1,(255,255,255))
        window.blit(text_score1,(10,10))
        text_score2 = font1.render('Счёт красного: ' +str(score2), 1,(255,255,255))
        window.blit(text_score2,(480,10))
        win1 = font2.render("Black Wins", 1, (180, 0, 0))
        win2 = font2.render("Reds Wins", 1, (180, 0, 0))
        restart = font3.render("Нажмите R чтоб перезапустить игру", 1, (255,255,255))
        
        
#Победа
        if score1>=2:
            window.blit(win1,(150,250))
            #window.blit(restart,(120, 350))
            finish = False

        if score2>=2:
            window.blit(win2,(150,250))
            #window.blit(restart,(120, 350))
            finish = False



    display.update()
    clock.tick(FPS)
