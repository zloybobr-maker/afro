from pygame import *
from random import *


width = 700
heiht = 500
lost = 0
   # score = 0
    #lost = 0

window =display.set_mode((width, heiht))
display.set_caption('👶🏿')
backgrounnd = transform.scale(image.load('2.webp'), (width, heiht))


score = 0
lost = 0

clock = time.Clock()
FPS = 70


font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 32)
win_text = font1.render('You win!', True, (0, 0, 5))
lose_text = font1.render('You lose!', True, (0, 0, 5))





finish = False
game = True




class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, width, height):
        super().__init__()

        self.image = transform.scale(image.load(filename), (width, height))
        self.speed = speed 

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player (GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < width - self.image.get_width():
            self.rect.x += self.speed

class UFO1(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > heiht:
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())

class UFO2(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > heiht:
            lost += 1
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())



class UFO(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > heiht:
            lost += 1
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())


player = Player('3.png', 300, 360, 7, 150, 170)
#player = sprite.Group
monsters = sprite.Group()
for i in range(1):
    ufo = UFO('1.png', randint(0, 650), randint(-100, -50), 1, 55, 85)
    monsters.add(ufo)

monsters1 = sprite.Group()
for i in range(1):
    ufo1 = UFO1('chuvak.png', randint(0, 650), randint(-100, -50), 1, 55, 85)
    monsters1.add(ufo1)


monsters2 = sprite.Group()
for i in range(1):
    ufo2 = UFO2('a.png', randint(0, 650), randint(-100, -50), 1, 85, 105)
    monsters2.add(ufo2)





finish = False
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(backgrounnd,(0, 0)) 
        player.reset()
        player.update()
        monsters.update()
        monsters.draw(window) 
        


        score_text = font2.render('Счет:' + str(score), True, (255, 255, 255))
        lost_text = font2.render('Пропущено:' + str(lost), True, (255, 255, 255))
        window.blit(score_text, (10, 20))
        window.blit(lost_text, (10, 50))   
                
        collides = sprite.spritecollide(player, monsters, True)
        for c in collides:
            score += 1
            ufo = UFO('1.png', randint(0, 650), randint(-100, -50), 3, 55, 85)
            monsters.add(ufo)

        if sprite.spritecollide(player, monsters, False) or lost > 5:
            finish = True
            window.blit(lose_text, (200, 200))
        if score > 30:
            finish = True
            window.blit(win_text, (200, 200))

        if score > 5:

            monsters1.update()
            monsters1.draw(window) 

    
        collides = sprite.spritecollide(player, monsters1, True)
        for c in collides:
            score -= 1
            ufo1 = UFO1('chuvak.png', randint(0, 650), randint(-100, -50), 3, 55, 85)
            monsters1.add(ufo1)


        if score > 10:

            monsters2.update()
            monsters2.draw(window) 



        collides = sprite.spritecollide(player, monsters2, True)
        for c in collides:
            score += 3
            ufo2 = UFO2('a.png', randint(0, 650), randint(-100, -50), 3, 85, 105)
            monsters2.add(ufo2)


            



        

    display.update()
    clock.tick(FPS)
