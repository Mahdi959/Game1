import pygame
import random

screen = pygame.display.set_mode((480, 640))
shoot = pygame.image.load('shoot1.png')
lala = pygame.image.load('charecter.png')
me = pygame.transform.scale(lala, (400, 240))
shoot1 = pygame.transform.scale(shoot, (120, 180))
bkground = pygame.image.load('background.jpg')
bkground = pygame.transform.scale(bkground, (480, 640))
user_x = 70
user_y = 500

keep_alive = True


def ran():
    return -1 * random.randint(100, 1000)


poss_y = [ran() + 541, ran() + 45, ran() + 90, ran() + 200, ran(), ran()]
poss_x = [ran() + 541, ran() + 45, ran() + 90, ran() + 200, ran(), ran()]


def starting_keepthemrunning(idx):
    if poss_y[idx] > 700:
        poss_y[idx] = ran()  # only this line is for starting_keepthemrunning

    elif poss_x[idx] > 1000:
        poss_x[idx] = ran()

    else:
        poss_y[idx] = poss_y[idx] + 5
        poss_x[idx] = poss_x[idx] + 5



clock = pygame.time.Clock()

while keep_alive:

    starting_keepthemrunning(0)
    starting_keepthemrunning(1)
    starting_keepthemrunning(2)
    starting_keepthemrunning(3)
    starting_keepthemrunning(4)
    starting_keepthemrunning(5)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 285 or keys[pygame.K_d] and user_x < 285:
        user_x = user_x + 5

    elif keys[pygame.K_LEFT] and user_x > -150 or keys[pygame.K_a] and user_x > -150:
        user_x = user_x - 5

    elif keys[pygame.K_UP] and user_y > 0 or keys[pygame.K_w] and user_y > 0:
        user_y = user_y - 5

    elif keys[pygame.K_DOWN] and user_y < 540 or keys[pygame.K_s] and user_y < 540:
        user_y = user_y + 5

    screen.blit(bkground, [0, 0])
    screen.blit(me, [user_x, user_y])
    screen.blit(shoot1, [poss_x[5], poss_y[0]])
    screen.blit(shoot1, [poss_x[4], poss_y[1]])
    screen.blit(shoot1, [poss_x[5], poss_y[2]])
    screen.blit(shoot1, [poss_x[0], poss_y[3]])
    screen.blit(shoot1, [poss_x[3], poss_y[4]])
    screen.blit(shoot1, [poss_x[2], poss_y[5]])
    screen.blit(shoot1, [5, poss_y[0]])
    screen.blit(shoot1, [85, poss_y[4]])
    screen.blit(shoot1, [200, poss_y[3]])
    #if user_x == 5 or user_y == poss_y[0]:

    clock.tick(100)

    pygame.display.update()
