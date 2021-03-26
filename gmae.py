import pygame
import random
import datetime

screen = pygame.display.set_mode((480, 640))
shoot = pygame.image.load('shoot1.png')
lala = pygame.image.load('charecter.png')
me = pygame.transform.scale(lala, (400, 240))
shoot1 = pygame.transform.scale(shoot, (120, 180))
user = 70
tuser = 500

keep_alive = True


def mahdi():
    return -1 * random.randint(5, 1000)


pip = [mahdi() + 541, mahdi() + 45, mahdi() + 90, mahdi() + 200, mahdi(), mahdi()]


def ammago(idx):
    if pip[idx] > 700:
        pip[idx] = mahdi()
    else:
        pip[idx] = pip[idx] + 5


d = print('Welcome to Earth')

while keep_alive:
    ammago(0)
    ammago(1)
    ammago(2)
    ammago(3)
    ammago(4)
    ammago(5)
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

    screen.blit(pygame.image.load('background.jpg'), [0, 0])
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

    pygame.display.update()
    clock.tick(60)
