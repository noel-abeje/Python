#Noel Abeje
#This code follows instructions from a series of Videos by Tech with Tim (the link is down below)
#https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
import pygame
pygame.init()

window=pygame.display.set_mode((800, 600))
pygame.display.set_caption(('First Game'))

walkright=[pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkleft=[pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock=pygame.time.Clock()

bulletsound=pygame.mixer.Sound('laser.wav')
hitsound=pygame.mixer.Sound('explosion.wav')
music=pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.speed=5
        self.isjump=False
        self.jumpcount=10
        self.left=False
        self.right=False
        self.walkcount=0
        self.standing= True
        self.hitbox=(self.x+17, self.y+11, 29, 52)

    def draw(self, window):
        if self.walkcount+1>=27:
            self.walkcount=0

        if not(self.standing):
            if self.left:
                window.blit(walkleft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            elif self.right:
                window.blit(walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
        else:
            if self.right:
                window.blit(walkright[0],(self.x,self.y))
            else:
                window.blit(walkleft[0],(self.x,self.y))
                
        self.hitbox=(self.x+17, self.y+11, 29, 52)
        #pygame.draw.rect(window,(255,0,0), self.hitbox,2)

    def hit(self):
        self.isjump=False
        self.jumpcount=10
        self.x=700
        self.y=530
        self.walkcount=0
        font1=pygame.font.SysFont('comicsans', 100)
        text=font1.render('-10',1,(255,0,0))
        window.blit(text,(400,300))
        pygame.display.update()
        i=0
        while i<300:
            pygame.time.delay(5)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()


class projectile(object):
    def __init__(self,x,y,radius,color,direction):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.direction=direction
        self.speed=8*direction

    def draw(self, window):
        pygame.draw.circle(window, self.color,(self.x,self.y), self.radius)


class enemy(object):
    walkright = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkleft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x, self.end]
        self.speed=5
        self.walkcount=0
        self.hitbox=(self.x+17, self.y+2, 31, 57)
        self.health=25
        self.alive=True

    def draw(self, window):
        self.move()
        if self.alive:
            if self.walkcount+1>=33:
                self.walkcount=0

            if self.speed>0:
                window.blit(self.walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            else:
                window.blit(self.walkleft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1

            self.hitbox=(self.x+17, self.y+2, 31, 57)
            #pygame.draw.rect(window,(255,0,0), self.hitbox,2)
            pygame.draw.rect(window,(255,0,0), (self.hitbox[0],self.hitbox[1]-20,125,5))
            pygame.draw.rect(window,(0,120,0), (self.hitbox[0],self.hitbox[1]-20,25-(5*(5-self.health)),5))

    def move(self):
        if self.speed>0:
            if self.x+self.speed <self.path[1]:
                self.x+=self.speed
            else:
                self.speed=self.speed *-1
                self.walkcount=0
        else:
            if self.x-self.speed>self.path[0]:
                self.x+=self.speed
            else:
                self.speed=self.speed *-1
                self.walkcount=0

    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.alive=False
        print('pow')
        pass
        
def redraw():
    window.blit(bg, (0,0))
    text=font.render('HITS:'+ str(score),1,(50,0,0))
    window.blit(text,(700,10))
    man.draw(window)
    goblin.draw(window)
    if goblin.alive==False:
        winner=font.render('You Win',1,(123,56,234))
        window.blit(winner,(400,300))
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

font=pygame.font.SysFont('comicsans',30)
man=player(0, 530, 10, 64)
goblin=enemy(0,540,64,64,740)
shot=0
bullets=[]
run= True

while run:
    clock.tick(30)

    if goblin.alive==True:
        if man.hitbox[1]<goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:
            if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]<goblin.hitbox[0]+goblin.hitbox[2]:
                man.hit()
                score-=10

    if shot>0:
        shot+=1
    if shot>3:
        shot=0
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    if goblin.alive==True:
        for bullet in bullets:
            if bullet.y-bullet.radius<goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:
                if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
                    hitsound.play()
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))
                
            if bullet.x<800 and bullet.x>0:
                bullet.x+=bullet.speed
            else:
                bullets.pop(bullets.index(bullet))


    keys= pygame.key.get_pressed()
    if goblin.alive==True:
        if keys[pygame.K_SPACE] and shot==0:
            if man.left:
                direction = -1
            else:
                direction = 1
            if len(bullets) < 10:
                bullets.append(projectile(round(man.x + man.width//2),round(man.y + man.height//2),6,(0,0,0), direction))
                shot=1
    
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.speed
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<=750:
        man.x+=man.speed
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkcount=0
    if not(man.isjump):
        if keys[pygame.K_UP] and man.y<=560:
           man.isjump=True
           man.left=False
           man.right=False
           man.walkcount=0
    else:
        if man.jumpcount>-10:
            neg=1
            if man.jumpcount<=0:
                neg=-1.35
            man.y-=(man.jumpcount**2)*0.5*neg
            man.jumpcount-=1
        else:
            man.isjump=False
            man.jumpcount=10

    redraw()
    
        

pygame.quit()

        
