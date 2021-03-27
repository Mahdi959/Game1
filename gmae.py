import pygame
import random
screen = pygame.display.set_mode((480, 640))
shoot = pygame.image.load('shoot1.png')
lala = pygame.image.load('charecter.png')
me = pygame.transform.scale(lala, (400, 240))
shoot1 = pygame.transform.scale(shoot, (120, 180))
bkground = pygame.image.load('background.jpg')
bkground = pygame.transform.scale(bkground,(480,640))
user = 70
tuser = 500

keep_alive = True


def ran():
    return -1 * random.randint(5, 1000)


pip = [ran() + 541, ran() + 45, ran() + 90, ran() + 200, ran(), ran()]


def starting(idx):
    if pip[idx] > 700:
        pip[idx] = ran()
    else:
        pip[idx] = pip[idx] + 5

clock = pygame.time.Clock()
while keep_alive:
    starting(0)
    starting(1)
    starting(2)
    starting(3)
    starting(4)
    starting(5)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user < 285:
        user = user + 20
    elif keys[pygame.K_LEFT] and user > -150:
        user = user - 20
    elif keys[pygame.K_UP] and tuser > 0:
        tuser = tuser - 20
    elif keys[pygame.K_DOWN] and tuser < 540:
        tuser = tuser + 20

    screen.blit(bkground, [0, 0])
    screen.blit(me, [user, tuser])
    screen.blit(shoot1, [pip[5], pip[0]])
    screen.blit(shoot1, [pip[4], pip[1]])
    screen.blit(shoot1, [pip[5], pip[2]])
    screen.blit(shoot1, [pip[0], pip[3]])
    screen.blit(shoot1, [pip[3], pip[4]])
    screen.blit(shoot1, [pip[2], pip[5]])
    screen.blit(shoot1, [5, pip[0]])
    screen.blit(shoot1, [85, pip[4]])
    screen.blit(shoot1, [200, pip[3]])
    clock.tick(60)
    pygame.display.update()
    clock.tick(60)
