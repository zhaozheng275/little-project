import pygame
import sys
import random

zom_nun = 99  # 僵尸数量
sun_num = 150  # 初始阳光
x = 1020
y = 700
che_speed = [0, 0, 0, 0, 0, 0]
che_pos = [180, 180, 180, 180, 180, 180]
with open('dll.txt', 'r') as file:
    temporary = file.read()
times = int(temporary)
plant_list = [[0] * 6 for i in range(11)]
plant_hp = [[0] * 6 for g in range(11)]
price = [0, 50, 100, 200, 400, 500]  # 植物价格
lin = [0, 180, 280, 380, 480, 580, 700]  # 位置列表
row = [0, 250, 330, 410, 490, 580, 660, 740, 810, 890, 970, 1020]  # 位置列表
p = 0
p_list = [[0] * 6 for a in range(10)]
zom_list = [1 for b in range(zom_nun + 10)]
zom_hp_list = [0 for f in range(zom_nun + 10)]
pos_list = [0 for c in range(zom_nun + 10)]
lin_list = [0 for d in range(zom_nun + 10)]
pygame.font.init()
pygame.init()
font = pygame.font.SysFont('kaiti', 100)
pygame.display.set_caption("赵政制作版植物大战僵尸")
stymie = 5
h = 700
w = 1020
pygame.mixer.music.load("images/music.mp3")
pygame.mixer.music.play()
back = pygame.image.load("images/background1.jpg")
card_shoot = pygame.image.load("images/card/Peashooter.gif")
card_flower = pygame.image.load("images/card/TwinSunflower.gif")
card_shoots = pygame.image.load("images/card/PotatoMine.gif")
card_wall = pygame.image.load("images/card/WallNut.gif")
card_tnt = pygame.image.load("images/card/Gralic.gif")
che = pygame.image.load("images/LawnMower.gif")
dan = pygame.image.load("images/PB10.gif")
win = pygame.image.load("images/ZombiesWon.png")
wins = pygame.image.load("images/Logo.jpg")
zoms = [[],
        [pygame.image.load("images/zom1/zom1.png"), pygame.image.load("images/zom1/zom2.png"),
         pygame.image.load("images/zom1/zom3.png"), pygame.image.load("images/zom1/zom4.png"),
         pygame.image.load("images/zom1/zom5.png"), pygame.image.load("images/zom1/zom6.png"),
         pygame.image.load("images/zom1/zom7.png"), pygame.image.load("images/zom1/zom8.png"),
         pygame.image.load("images/zom1/zom9.png"), ],
        [pygame.image.load("images/zom2/zom1.png"), pygame.image.load("images/zom2/zom2.png"),
         pygame.image.load("images/zom2/zom3.png"), pygame.image.load("images/zom2/zom4.png"),
         pygame.image.load("images/zom2/zom5.png"), pygame.image.load("images/zom2/zom6.png"),
         pygame.image.load("images/zom2/zom7.png"), pygame.image.load("images/zom2/zom8.png"),
         pygame.image.load("images/zom2/zom9.png"), ],
        [pygame.image.load("images/zom3/zom1.png"), pygame.image.load("images/zom3/zom2.png"),
         pygame.image.load("images/zom3/zom3.png"), pygame.image.load("images/zom3/zom4.png"),
         pygame.image.load("images/zom3/zom5.png"), pygame.image.load("images/zom3/zom6.png"),
         pygame.image.load("images/zom3/zom7.png"), pygame.image.load("images/zom3/zom8.png"),
         pygame.image.load("images/zom3/zom9.png"), ],
        [pygame.image.load("images/zom4/zom1.png"), pygame.image.load("images/zom4/zom2.png"),
         pygame.image.load("images/zom4/zom3.png"), pygame.image.load("images/zom4/zom4.png"),
         pygame.image.load("images/zom4/zom5.png"), pygame.image.load("images/zom4/zom6.png"),
         pygame.image.load("images/zom4/zom7.png"), pygame.image.load("images/zom4/zom8.png"),
         pygame.image.load("images/zom4/zom9.png"), ]]
for i in range(1, 5):
    for j in range(9):
        zoms[i][j] = pygame.transform.scale(zoms[i][j], (78, 140))
plant = [0, pygame.image.load("images/TwinSunflower.gif"), pygame.image.load("images/Peashooter.gif"),
         pygame.image.load("images/Repeater.giF"), pygame.image.load("images/GatlingPea.gif"),
         pygame.image.load("images/PotatoMine.gif")]
zom_action = 0
zom_actions = 0
for i in range(zom_nun + 10):
    zom_list[i] = random.randint(1, 4)
    pos_list[i] = 1200 +70*i # 僵尸位置
    lin_list[i] = random.randint(1, 5)
    zom_hp_list[i] = zom_list[i] * 500 + 300 * i  # 僵尸血量
screen = pygame.display.set_mode([w, h])
screen.fill((20, 100, 100))
back_rect = back.get_rect().move(0, 100)
pygame.display.flip()


while True:
    pygame.time.Clock().tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y <= lin[1]:
                p = 0
            if sun_num - price[p] >= 0:
                sun_num = sun_num - price[p]
                if y <= lin[1]:
                    sun_num = sun_num + price[p]
                    if row[1] <= x < row[2]:
                        p = 1
                    elif row[2] <= x < row[3]:
                        p = 2
                    elif row[3] <= x < row[4]:
                        p = 3
                    elif row[4] <= x < row[5]:
                        p = 4
                    elif row[5] <= x < row[6]:
                        p = 5
                for i in range(1, 10):
                    for j in range(1, 6):
                        if lin[j] <= y < lin[j + 1]:
                            if row[i] <= x < row[i + 1]:
                                if p != 0:
                                    p_list[i][j] = p
                                    plant_list[i][j] = p
                                    plant_hp[i][j] = 200
                                    p = 0
    time = pygame.time.get_ticks()
    if time / 1000 > stymie:
        sun_num = sun_num + 25
        for i in range(1, 6):
            for j in range(1, 10):
                if plant_list[j][i] == 1:
                    sun_num = sun_num + 25
        stymie = stymie + 3
    screen = pygame.display.set_mode([w, h])
    screen.fill((20, 100, 100))
    back_rect = back.get_rect().move(0, 100)
    screen.blit(back, back_rect)
    screen.blit(card_flower, (row[1], lin[0]))
    screen.blit(card_shoot, (row[2], lin[0]))
    screen.blit(card_shoots, (row[3], lin[0]))
    screen.blit(card_wall, (row[4], lin[0]))
    screen.blit(card_tnt, (row[5], lin[0]))
    for j in range(zom_nun):
        if pos_list[j] <= che_pos[lin_list[j]] + 50 and pos_list[j] <= 1020 and che_pos[lin_list[j]] <= 1100:
            che_speed[lin_list[j]] = 5
            zom_nun = zom_nun - 1
            del zom_hp_list[j]
            del zom_list[j]
            del pos_list[j]
            del lin_list[j]
    for i in range(1, 6):
        for j in range(1, 10):
            if plant_list[j][i] != 0:
                if p_list[j][i] != 0:
                    screen.blit(plant[p_list[j][i]], (row[j], lin[i]))
    for i in range(1, 6):
        che_pos[i] += che_speed[i]
        screen.blit(che, (che_pos[i], lin[i]))
    text = font.render(str(sun_num), True, (0, 0, 255), (0, 0, 0))
    texts = font.render(str(zom_nun), True, (0, 0, 255), (0, 0, 0))
    screen.blit(texts, (800, 0))
    screen.blit(text, (0, 0))
    for i in range(1, 6):
        for j in range(1, 10):
            if plant_hp[j][i] <= 0:
                plant_list[j][i] = 0
            if plant_list[j][i] == 2:
                for a in range(zom_nun):
                    if lin_list[a] == i:
                        if pos_list[a] <= 1020:
                            zom_hp_list[a] = zom_hp_list[a] - 5 * times
                            break
            if plant_list[j][i] == 3:
                for a in range(zom_nun):
                    if lin_list[a] == i:
                        if pos_list[a] <= 1020:
                            zom_hp_list[a] = zom_hp_list[a] - 10 * times
                            break
            if plant_list[j][i] == 4:
                for a in range(zom_nun):
                    if lin_list[a] == i:
                        if pos_list[a] <= 1020:
                            zom_hp_list[a] = zom_hp_list[a] - 20 * times
                            break
    for i in range(zom_nun):
        if zom_hp_list[i] <= 0:
            del zom_hp_list[i]
            del zom_list[i]
            del pos_list[i]
            del lin_list[i]
            zom_nun = zom_nun - 1
        pos_list[i] = pos_list[i] - 1
        for j in range(1, 11):
            if row[10 - j] <= pos_list[i] <= row[11 - j] and plant_list[11 - j][lin_list[i]] != 0:
                if plant_list[11 - j][lin_list[i]] == 5:
                    plant_list[11 - j][lin_list[i]] = 0
                    del zom_hp_list[i]
                    del zom_list[i]
                    del pos_list[i]
                    del lin_list[i]
                    zom_nun = zom_nun - 1
                else:
                    plant_hp[11 - j][lin_list[i]] -= 1
                    pos_list[i] = pos_list[i] + 1
        screen.blit(zoms[zom_list[i]][int(zom_action / 10)], (pos_list[i], lin[lin_list[i]] - 50))
        if pos_list[i] < -10:
            screen.blit(win, (300, 150))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
    zom_action = zom_action + 1
    if zom_action == 90:
        zom_action = 0
    if zom_nun <= 0:
        screen.blit(wins, (50, 50))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
    pygame.display.update()
