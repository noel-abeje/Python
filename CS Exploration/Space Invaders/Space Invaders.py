#Noel Abeje
#Some this code was done by following instructions from a series of videos by free code camp (link is below)
#https://www.youtube.com/watch?v=FfWpgLFMI7w
import pygame
import random
import math
from pygame import mixer
#Initialize pygame
pygame.init()
#Create a window
window=pygame.display.set_mode((800,600))
#To get a title
pygame.display.set_caption(('Practice'))
#To get a background image
background=pygame.image.load('space.png')
#To add background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
#To make an icon
#Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
icon=pygame.image.load('super-mario.png')
pygame.display.set_icon(icon)
#To add an image
#Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
playerImg=pygame.image.load('space-invaders.png')
#define x and y so that they can be changed
px=370
py=480
speed=4
#To add an interactive enemy
enemyImg=[]
ex=[]
ey=[]
speed2=[]
enemyAmount=10
for i in range(enemyAmount):
    enemyImg.append(pygame.image.load('ufo.png'))
    #define x and y so that they can be changed
    ex.append(random.randint(0,736))
    ey.append(random.randint(50,150))
    speed2.append(4)
#To add a bullet
bulletImg=pygame.image.load('bullet.png')
#define x and y so that they can be changed
bx=random.randint(0,800)
by=480
speed3=7
bstate='ready'
#function to make it easier
def player(x,y):
    window.blit(playerImg, (x,y))
def enemy(x,y,i):
    window.blit(enemyImg[i], (x,y))
def fire(x,y):
    global bstate
    bstate="fire"
    window.blit(bulletImg, (x+22,y+10))

#To find collision
def collision(x1, y1, x2, y2):
    distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if distance<30:
        return True
    else:
        return False

#Score
score=0
font= pygame.font.Font('freesansbold.ttf',32)
tx=600
ty=10
def scores(x,y):
    scoring=font.render('Score:'+str(score),True,(255,255,255))
    window.blit(scoring, (x,y))

#Game Over
over= pygame.font.Font('freesansbold.ttf',64)
def game_over():
    done=over.render('GAME OVER',True,(255,255,255))
    window.blit(done, (200,250))


#Loop to keep the game running
run=True
while run:
    #To get a background
    window.fill((0,0,0))
    #background image
    window.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #if keys are pressed
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        px-=speed
    if keys[pygame.K_RIGHT]:
        px+=speed
    if keys[pygame.K_UP]:
        py-=speed
    if keys[pygame.K_DOWN]:
        py+=speed
    if keys[pygame.K_SPACE]:
        if bstate is 'ready':
            bullet_sound=mixer.Sound('laser.wav')
            bullet_sound.play()
            bx=px
            fire(bx,by)
    #To constrain the player
    if px<=0:
        px=0
    if px>=736:
        px=736
    if py<=400:
        py=400
    if py>=536:
        py=536

    #To move the enemies
    for i in range(enemyAmount):
        #Game Over
        if ey[i]>440:
            for j in range(enemyAmount):
                ey[j]=2000
            game_over()
        ex[i]+=speed2[i]
        #To constrain the image
        if ex[i]<=0:
            speed2[i]=4
            ey[i]+=30
        if ex[i]>736:
            speed2[i]=-4
            ey[i]+=30
        #Collision
        coll=collision(ex[i],ey[i],bx,by)
        if coll==True:
            co_sound=mixer.Sound('explosion.wav')
            co_sound.play()
            by=py
            bstate="ready"
            score+=1
            ex[i]=10
            ey[i]=10
        enemy(ex[i],ey[i],i)
    #Bullet movement
    if by<=0:
        by=py
        bstate="ready"
    if bstate is 'fire':
        fire(bx,by)
        by-=speed3

    player(px,py)
    scores(tx,ty)
    pygame.display.update()

    

pygame.quit()
