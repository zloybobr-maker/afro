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
            lost += 3
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

class UFO5(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > heiht:
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())


class UFO4(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > heiht:
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())

class UFO3(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > heiht:  
            self.rect.y = randint(-100, -50)
            self.rect.x = randint(0, width - self.image.get_width())

mixer.init()
mixer.music.load('8.mp3')
mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')


player = Player('3.png', 300, 360, 7, 150, 170)
#player = sprite.Group
monsters = sprite.Group()
for i in range(1):
    ufo = UFO('1.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
    monsters.add(ufo)

monsters1 = sprite.Group()
for i in range(1):
    ufo1 = UFO1('chuvak.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
    monsters1.add(ufo1)


monsters2 = sprite.Group()
for i in range(1):
    ufo2 = UFO2('a.png', randint(0, 650), randint(-100, -50), 2, 45, 65)
    monsters2.add(ufo2)


monsters3 = sprite.Group()
for i in range(1):
    ufo3 = UFO3('6.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
    monsters3.add(ufo3)

monsters4 = sprite.Group()
for i in range(1):
    ufo4 = UFO4('42.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
    monsters4.add(ufo4)

monsters5 = sprite.Group()
for i in range(1):
    ufo5 = UFO5('10.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
    monsters5.add(ufo5)



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
        speed_text = font2.render('скорость игрока:' + str(player.speed), True, (255, 255, 255))
        window.blit(score_text, (10, 20))
        window.blit(lost_text, (10, 50))
        window.blit(speed_text, (10, 80)) 
                
        collides = sprite.spritecollide(player, monsters, True)
        for c in collides:
            score += 1
            ufo = UFO('1.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
            monsters.add(ufo)

        if sprite.spritecollide(player, monsters, False) or lost >= 10:
            finish = True
            window.blit(lose_text, (200, 200))
        if score > 40:
            finish = True
            window.blit(win_text, (200, 200))
        #if player.speed >= 1:
            #window.blit(player.speed, (10, 80)) 

        if score > 10:

            monsters1.update()
            monsters1.draw(window) 

    
        collides = sprite.spritecollide(player, monsters1, True)
        for c in collides:
            score -= 2
            ufo1 = UFO1('chuvak.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
            monsters1.add(ufo1)


        if score > 7:

            monsters2.update()
            monsters2.draw(window) 



        collides = sprite.spritecollide(player, monsters2, True)
        for c in collides:
            score += 3
            ufo2 = UFO2('a.png', randint(0, 650), randint(-100, -50), 2, 45, 65)
            monsters2.add(ufo2)


        if score > 15:

            monsters3.update()
            monsters3.draw(window) 

    
        collides = sprite.spritecollide(player, monsters3, True)
        for c in collides:
            score -= 5
            ufo3 = UFO3('6.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
            monsters3.add(ufo3)

        if score > 20:

            monsters4.update()
            monsters4.draw(window) 

    
        collides = sprite.spritecollide(player, monsters4, True)
        for c in collides:
            player.speed -= 1
            ufo4 = UFO4('42.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
            monsters4.add(ufo4)
        
        if score >= 19:

            monsters5.update()
            monsters5.draw(window) 

    
        collides = sprite.spritecollide(player, monsters5, True)
        for c in collides:
            player.speed += 1
            ufo5 = UFO5('10.png', randint(0, 650), randint(-100, -50), 2, 55, 85)
            monsters5.add(ufo5)

            
                       



        

    display.update()
    clock.tick(FPS)
