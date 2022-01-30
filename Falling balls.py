import os, pygame, sys, sqlite3, random

pygame.mixer.pre_init(44100, -16, 1, 512)


pygame.init()

def scren():

    gameplay_background = pygame.transform.scale(load_image('game_bg.jpg'), (width, height))
    screen.blit(gameplay_background, (0, 0))

#Функция отвечающая за проигрывание звука в меню

def menu_sound():

    pygame.mixer.music.load("data/заставка.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

#Функция отвечающая за проигрывание звука во время игры

def play_sound():

    pygame.mixer.music.load("data/play_sound.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

#Функция отвечающая за проигрывание звука при поимке шарика

def poimal_sound():

    pygame.mixer.Sound("data/h.mp3").play()

#Функция отвечающая за вроигрывание звука если шарик не пойман

def fall_sound():

    pygame.mixer.Sound("data/spank.mp3").play()

#Функция отвечающая за вроигрывание звука если вы проиграли

def sorry_sound():

    pygame.mixer.music.load("data/sorry.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)


#Функция отвечающая за отрисовку корзины

def corzina(po):

    if ps[x][y] < 2:
        basket_image = pygame.transform.scale(load_image('basket_l.png'), (70, 70))
    else:
        basket_image = pygame.transform.scale(load_image('basket_r.png'), (70, 70))
    screen.blit(basket_image, MegaPos[po])

def ball(po):

    ball_image = pygame.transform.scale(load_image('ball.png'), (23, 23))
    po = po[0] - 10, po[1] - 10
    screen.blit(ball_image, po)

#Функция отвечающая за создание баззы данных и проверки не создана ли она

def bazacormit():

    data = sqlite3.connect(r'data/records.sqlite')
    cur = data.cursor()
    cur.execute('''
                create table if not exists RECORDS(
                    name text,
                    score integer
                )''')
    cur.execute("""
                INSERT INTO RECORDS(score) VALUES('""" + str(count) + """')
                """)
    data.commit()

#Функция отвечающая за меню рекодов (показ очков и картинки)

def open_records():

    # Создание собственного исключения для
    # исключения ошибки sqlite3.OperationalError

    try:
        data = sqlite3.connect(r'data/records.sqlite')
        cur = data.cursor()
        cur.execute('''
        select score from RECORDS order by score desc
        limit 5
        ''')
        result = cur.fetchall()
        list_rec = []
        for i in result:
            list_rec.append(i[0])

        if len(list_rec) == 0:
            records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
            screen.blit(records_bg, (0, 0))
            player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
            player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
            player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
            player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
            player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
            screen.blit(player_1, (30, 20))
            screen.blit(player_2, (30, 50))
            screen.blit(player_3, (30, 80))
            screen.blit(player_4, (30, 110))
            screen.blit(player_5, (30, 140))

        if len(list_rec) == 1:
            records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
            screen.blit(records_bg, (0, 0))
            player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
            player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
            player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
            player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
            player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
            screen.blit(player_1, (30, 20))
            screen.blit(player_2, (30, 50))
            screen.blit(player_3, (30, 80))
            screen.blit(player_4, (30, 110))
            screen.blit(player_5, (30, 140))

        if len(list_rec) == 2:
            records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
            screen.blit(records_bg, (0, 0))
            player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
            player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
            player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
            player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
            player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
            screen.blit(player_1, (30, 20))
            screen.blit(player_2, (30, 50))
            screen.blit(player_3, (30, 80))
            screen.blit(player_4, (30, 110))
            screen.blit(player_5, (30, 140))

        if len(list_rec) == 3:
            records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
            screen.blit(records_bg, (0, 0))
            player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
            player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
            player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
            player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
            player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
            screen.blit(player_1, (30, 20))
            screen.blit(player_2, (30, 50))
            screen.blit(player_3, (30, 80))
            screen.blit(player_4, (30, 110))
            screen.blit(player_5, (30, 140))

        if len(list_rec) == 4:
            records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
            screen.blit(records_bg, (0, 0))
            player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
            player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
            player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
            player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
            player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
            screen.blit(player_1, (30, 20))
            screen.blit(player_2, (30, 50))
            screen.blit(player_3, (30, 80))
            screen.blit(player_4, (30, 110))
            screen.blit(player_5, (30, 140))

        if len(list_rec) == 5:
            records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
            screen.blit(records_bg, (0, 0))
            player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
            player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
            player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
            player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
            player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
            screen.blit(player_1, (60, 20))
            screen.blit(player_2, (60, 60))
            screen.blit(player_3, (60, 100))
            screen.blit(player_4, (60, 140))
            screen.blit(player_5, (60, 180))
    except sqlite3.OperationalError:
        records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))
        screen.blit(records_bg, (0, 0))
        player_1 = font.render(('Balls master: 0'), True, (255, 255, 255))
        player_2 = font.render(('Boss of the balls: 0'), True, (255, 25, 255))
        player_3 = font.render(('Mr.Average: 0'), True, (255, 255, 25))
        player_4 = font.render(('Starter: 0'), True, (255, 201, 14))
        player_5 = font.render(('Rookie: 0'), True, (255, 0, 0))
        screen.blit(player_1, (30, 20))
        screen.blit(player_2, (30, 60))
        screen.blit(player_3, (30, 100))
        screen.blit(player_4, (30, 140))
        screen.blit(player_5, (30, 180))


def lose():

    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 800, 500), 4)


# Функция отвечающая за загрузку картинки из папки data

def load_image(name, colorkey=None):

    fullname = os.path.join(r'data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
    return image

# Функция отвечающая за закрытие приложения
def terminate():

    pygame.quit()
    sys.exit()

#Создание игрового окна(название, размеры)

pygame.display.set_caption('Falling balls')
size = width, height = 800, 500
screen = pygame.display.set_mode(size)


katit = False
Lose = False
Menu = True
records = False
settings = False

x = 0
y = 0
ps = [
    [0, 2],
    [1, 3]
]


MegaPos = [
    (250, height * 0.32, 70, 70),
    (250, height * 0.67, 70, 70),
    (480, height * 0.32, 70, 70),
    (480, height * 0.67, 70, 70)
]


starts = [
    (0, height * 0.137),
    (0, height * 0.5),
    (width, height * 0.137),
    (width, height * 0.5)
]


lcount = 0

running = True
fps = 120
g = []


z = 0
p = 0

clock = pygame.time.Clock()


count = 0
LoseCount = 0
speed = 100

scren()

corzina(ps[x][y])
k = 80
g = []
MaX = 4

xleft = 2
yTop = 0.7
xright = -2
yBot = 0.6

menu_sound()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if x == 1:
                    x = 0
            if event.key == pygame.K_DOWN:
                if x == 0:
                    x = 1
            if event.key == pygame.K_LEFT:
                if y == 1:
                    y = 0
            if event.key == pygame.K_RIGHT:
                if y == 0:
                    y = 1
    # Флаг отвечающий за проигрыш
    if Lose == True:

        screen.fill((0, 0, 0))
        lose_picture = pygame.transform.scale(load_image('lose_picture.jpg'), (width, height))
        screen.blit(lose_picture, (0, 0))

        # Установка шрифта

        font = pygame.font.Font(None, 50)
        font1 = pygame.font.Font(None, 25)

        # Настройка отображения текста

        text = font.render(("Your score: " + str(count)), True, (45, 110, 240))
        text1 = font1.render(('нажмите Esc'), True, (100, 10, 100))
        text_x = width * 0.36
        text_y = height * 0.6
        text1_x = width * 0.8
        text1_y = height * 0.9
        screen.blit(text, (text_x, text_y))
        screen.blit(text1, (text1_x, text1_y))

        k = 80
        g = []

        # Создание условия для выхода из
        # окна проигрыша

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bazacormit()
                    Menu = True
                    Lose = False
                    count = 0
                    menu_sound()

    # Флаг отвечающий за сам процесс игры

    if katit == True:

        scren()
        corzina(ps[x][y])
        k += 1
        if k % speed == 0:
            u = random.randint(0, MaX)
            if u == 0:
                start = starts[0]
                g.append([start, xleft, yTop, u])

            elif u == 1:
                start = starts[1]
                g.append([start, xleft, yBot, u])

            elif u == 2:
                start = starts[2]
                g.append([start, xright, yTop, u])

            else:
                start = starts[3]
                g.append([start, xright, yBot, u])

        for i in g:

            ball(i[0])
            i[0] = i[0][0] + i[1], i[0][1] + i[2]
            if width * 0.26 < i[0][0] < width * 0.74:
                if i[3] == 0:
                    i[1] -= 0.01
                elif i[3] == 1 and i[1] > 0:
                    i[1] -= 0.03
                elif i[3] == 2:
                    i[1] += 0.01
                elif i[3] == 3 and i[1] < 0:
                    i[1] += 0.03
                i[2] += 0.03


            # Условие проверки пойман ли шарик
            # Если выполняется то:

            if MegaPos[ps[x][y]][1] + 25 <= i[0][1] <= MegaPos[ps[x][y]][1] + 35 and\
                    MegaPos[ps[x][y]][0] <= i[0][0] <= MegaPos[ps[x][y]][0] + 70:
                g.remove(i)
                poimal_sound()
                count += 1
                if speed > 30:
                    speed -= 1
                    fps *= 1.01

            # Условие проверки пойман ли шарик
            # Если выполняется то:

            if i[0][1] > height:
                g.remove(i)
                fall_sound()
                LoseCount += 1
                if LoseCount >= 5:
                    katit = False
                    Lose = True
                    sorry_sound()
                    LoseCount = 0

    # Флаг отвечающий за меню рекодов

    if records == True:

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        open_records()
        records_bg = pygame.transform.scale(load_image('records.jpg'), (width, height))

        # Условие для выхода из таблицы рекордов


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    records = False
                    Menu = True
            pygame.display.flip()

    # Флаг отвечающий за главное меню

    if Menu == True:

        fon = pygame.transform.scale(load_image('foon.jpg'), (width, height))

        screen.blit(fon, (0, 0))

        # Проверка нажатия Лкм в определённой зоне экрана
        # чтобы открыть то или иное коно

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Проверка для кнопки запуска игры.

                if height * 0.25 < event.pos[1] <= height * 0.365 and \
                        width * 0.365 < event.pos[0] < width * 0.635:
                    katit = True
                    Menu = False
                    play_sound()

                # Проверка для кнопки запуска меню рекордов

                if height * 0.38 < event.pos[1] <= height * 0.49 and \
                        width * 0.365 < event.pos[0] < width * 0.635:
                    Menu = False
                    records = True

                # Проверка для кнопки запуска меню настроек

                if height * 0.5 < event.pos[1] <= height * 0.61 and \
                        width * 0.365 < event.pos[0] < width * 0.635:
                    settings = True
                    Menu = False

                # Проверка для кнопки выхода из игры

                if height * 0.63 < event.pos[1] <= height * 0.73 and \
                        width * 0.365 < event.pos[0] < width * 0.635:
                    terminate()
        pygame.display.flip()

    # Флаг отвечающий за окно настроек

    if settings == True:

        fon = pygame.transform.scale(load_image('settings.jpg'), (width, height))
        screen.blit(fon, (0, 0))

        # Проверка нажатия кнопки Esc для выхода из этого меню

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings = False
                    Menu = True
            pygame.display.flip()

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()