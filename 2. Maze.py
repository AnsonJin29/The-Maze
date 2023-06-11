#To do the same for the green block(the timing upadte)
import pygame
import time
pygame.init()
timebob=0
timebobby=0
laptime=10000000000000
laptime2=10000000000000
screen=pygame.display.set_mode((1300,900))
done=False
font=pygame.font.Font('Macondo.ttf',70)
Title=font.render('The Maze Challenge',True,(255,255,255))
fontres=pygame.font.Font('Macondo.ttf',40)
x=35
y=40
a=95
b=40
countbobby=1
countbob=1
clock=pygame.time.Clock()
snapbob1=time.time()
snapbobby1=time.time()
snapbob1b=time.time()
snapbobby1b=time.time()
while done==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    screen.fill((0, 0, 0))
    if pressed[pygame.K_w]:
        y-=1
    if pressed[pygame.K_s]:
        y+=1
    if pressed[pygame.K_a]:
        x-=1
    if pressed[pygame.K_d]:
        x+=1
    bobby=pygame.draw.rect(screen,(0,30,255),pygame.Rect(x,y,50,50))
    if pressed[pygame.K_UP]:
        b -= 1
    if pressed[pygame.K_DOWN]:
        b += 1
    if pressed[pygame.K_LEFT]:
        a -= 1
    if pressed[pygame.K_RIGHT]:
        a += 1
    bob = pygame.draw.rect(screen, (128, 255, 0), pygame.Rect(a, b, 50, 50))
    left = pygame.draw.rect(screen, (200, 150, 0), pygame.Rect(0, 0, 30, 1000))
    right = pygame.draw.rect(screen, (200, 150, 0), pygame.Rect(1270, 0, 30, 1000))
    top = pygame.draw.rect(screen, (200, 150, 0), pygame.Rect(0, 0, 1300, 30))
    bottom = pygame.draw.rect(screen, (200, 150, 0), pygame.Rect(0, 870, 1300, 30))
    if bobby.colliderect(top): y+=5
    if bobby.colliderect(bottom): y-=5
    if bobby.colliderect(left): x+=5
    if bobby.colliderect(right): x-=5
    if bob.colliderect(top): b+=5
    if bob.colliderect(bottom): b-=5
    if bob.colliderect(left): a+=5
    if bob.colliderect(right): a-=5
    wall1 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(150, 30, 30, 730))
    wall2 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(320, 120, 30, 750))
    wall3 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(490, 30, 30, 730))
    wall4 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(600, 120, 30, 750))
    wall5 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(700, 30, 30, 730))
    wall6 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(820, 100, 370, 30))
    wall7 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(920, 200, 350, 30))
    wall8 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(820, 300, 370, 30))
    wall9 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(920, 400, 350, 30))
    wall10 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(820, 500, 370, 30))
    wall11 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(920, 600, 350, 30))
    wall12 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(820, 700, 370, 30))
    wall13 = pygame.draw.rect(screen, (255, 125, 0), pygame.Rect(820, 100, 30, 770))
    fin = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(900, 750, 50, 100))
    fontresbob = font.render(str(timebob), True, (128, 255, 0))
    fontresbobby = font.render(str(timebobby), True, (0, 30, 255))
    screen.blit(fontresbob, (200, 600))
    screen.blit(Title, (100, 100))
    screen.blit(fontresbobby, (500, 600))
    if bobby.colliderect(wall1) or bobby.colliderect(wall2) or bobby.colliderect(wall3) or bobby.colliderect(wall4) or bobby.colliderect(wall5) or bobby.colliderect(wall6) or bobby.colliderect(wall7) or bobby.colliderect(wall8) or bobby.colliderect(wall9) or bobby.colliderect(wall10) or bobby.colliderect(wall11) or bobby.colliderect(wall12) or bobby.colliderect(wall13) or bobby.colliderect(fin):
        if pressed[pygame.K_w]: y+=6
        if pressed[pygame.K_a]: x+=6
        if pressed[pygame.K_d]: x-=6
        if pressed[pygame.K_s]: y-=6
    if bob.colliderect(wall1) or bob.colliderect(wall2) or bob.colliderect(wall3) or bob.colliderect(wall4) or bob.colliderect(wall5) or bob.colliderect(wall6) or bob.colliderect(wall7) or bob.colliderect(wall8) or bob.colliderect(wall9) or bob.colliderect(wall10) or bob.colliderect(wall11) or bob.colliderect(wall12) or bob.colliderect(wall13) or bobby.colliderect(fin):
        if pressed[pygame.K_UP]: b+=6
        if pressed[pygame.K_LEFT]: a+=6
        if pressed[pygame.K_RIGHT]: a-=6
        if pressed[pygame.K_DOWN]: b-=6
    if  bob.colliderect(fin):
        snapbobend = time.time()
        timingbob = snapbobend - snapbob1
        snapbob1 = time.time()
        if timingbob <= laptime2:
            timebob = str(round(timingbob, 2))
            laptime2 = timingbob
            filebob=open('../../PyGame Projects/Laptime_Bob.txt', 'w')
            filebob.write(str(laptime2))
        a = 95
        b = 40
        x = 35
        y = 40
        fontresbob=0
    if  bobby.colliderect(fin):
        snapbobbyend=time.time()
        timingbobby = snapbobbyend - snapbobby1
        snapbobby1 = time.time()
        if timingbobby<=laptime:
            timebobby=str(round(timingbobby,2))
            laptime=timingbobby
        x = 35
        y = 40
        a = 95
        b = 40
    clock.tick(1000)
    pygame.display.flip()