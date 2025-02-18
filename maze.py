#create a Maze game!
from  pygame import *
 
class GameSprite(sprite.Sprite) :
    def __init__(self,player_name,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_name),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x , self.rect.y))

class player(GameSprite) :
    def update(self) :
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y-= self.speed

        if keys[K_DOWN] and self.rect.y <win_hight - 60:
            self.rect.y+= self.speed

        if keys[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x += self.speed

        if keys[K_LEFT] and self.rect.x >0:
            self.rect.x-= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self) :
        if self.rect.x == win_width - 250:
           self.direction = "right"
        elif self.rect.x == win_width - 80:
            self.direction = 'left'

        if self.direction == 'left' :
            self.rect.x -= self.speed 
        elif self.direction == 'right' :
            self.rect.x += self.speed  

class Wall(sprite.Sprite) :
    def __init__(self,color,wall_x,wall_y,width,height):
        super().__init__()
        self.image=Surface((width,height))
        self.image.fill(color) 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        window.blit(self.image,(self.rect.x , self.rect.y))






win_width , win_hight = 700,500
window = display.set_mode((win_width , win_hight))
display.set_caption("Maze")
clock = time.Clock ()
FBS =60
BACKGROUND = transform.scale(image.load("background.jpg"),(win_width,win_hight))

hero = player("hero.png",5,win_hight - 80,5)
enemy = Enemy('cyborg.png', win_width - 80,280,2)
final = GameSprite("treasure.png",win_width- 120,win_hight - 80,0)


w1=Wall((155,205,50),100,100,450,10)
w2=Wall((155,205,50),100,380,450,10)
w3=Wall((155,205,50),300,100,10,350)

font.init()
font_1 = font.SysFont("Times", 70)
win = font_1.render("YOU WON!",True , (255,215,0))
lose = font_1.render("YOU LOSE!",True , (255,50,0))


mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()


finish= False
run = True 
while run :

    for e in event.get() :
        if e.type == QUIT :
            run = False



    if not finish :
        window.blit(BACKGROUND , (0,0))
        hero.update()
        enemy.update()

        hero.reset()
        enemy.reset()
        final.reset()
        w1.draw()
        w2.draw()
        w3.draw()
        if sprite.collide_rect(hero, final) :
            finish= True 
            window.blit(win,(200,300))
        
        if (sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero,w1) or sprite.collide_rect(hero, w2)) :

            finish = True 
            window.blit(lose,(200,300))
        

    display.update()
    clock.tick(FBS) 