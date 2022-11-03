import pygame
import sys
from random import randint
from PIL import Image


WIDTH = 840
HEIGHT = 650

# Задаем цвета
BLACK = (0, 0, 0)
BLUE = (0,0,255)
RED = (255,0,0)

# Создаем игру и окно
pygame.init() #
pygame.mixer.init() #
display = pygame.display.set_mode((WIDTH, HEIGHT)) # переменная под наш дисплей (ширина/высота)
pygame.display.set_caption("My Game") # название окна
clock = pygame.time.Clock() # как часто будет обновлятся цикл(fps)

# Музыка
pygame.mixer.music.load("фон.mp3") # только для mp3
pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.load("C:/Users/user/Desktop/Game/проиграл.mp3")
# pygame.mixer.music.set_volume()  Громкость
# pygame.mixer.music.play()  чтобы проиграть музыку (-1(без конца)) (1(1 раз))
# pygame.mixer.music.pause() поставить музыку на паузу
# pygame.mixer.music.unpause() выйти из  паузы
# pygame.mixer.music.stop() остановить музыку
game_over_sound = pygame.mixer.Sound("проиграл.wav") # если хотим  музыку в переменной только для wav
pygame.mixer.Sound.set_volume(game_over_sound, 0.1) # Громкость конкретного звука 
# pygame.time.delay(мл/с) временная задержка / не музыки
# pygame.mixer.Sound.play чтобы проиграть музыку
# pygame.mixer.Sound.set_volume(название, значение) # Громкость конкретного звука

# Персонаж
usr_widrh = 45 # ШИРИНА 
usr_height = 80 # ДЛИНА
usr_x = WIDTH / 2 - 80 # ЕГО х ПОЗИЦИЯ
usr_y = HEIGHT - usr_height - 100 # ЕГО y ПОЗИЦИЯ

player_img = [pygame.image.load("car_player0.png"),pygame.image.load("car_player1.png"),pygame.image.load("car_player2.png")]
choise = randint(0,2)

def draw_player():
    display.blit(player_img[choise],(usr_x,usr_y)) # Игрок

# Проверяем, касается ли персонаж границ экрана
def check_if_borders():
    global usr_x, usr_y 
    if usr_x > WIDTH - 190: 
        usr_x -= 4
    if usr_x < 145 :
        usr_x += 4
    if usr_y < 1 :
        usr_y += 4
    if usr_y > 560 :
        usr_y -= 4

# Функия ходьбы 
def left():
    global usr_x
    usr_x -= 4
def right():
    global usr_x
    usr_x += 4
def up():
    global usr_y
    usr_y -= 4
def down():
    global usr_y
    usr_y += 4

# создаем машину
car_img=[pygame.image.load("car0.png"),pygame.image.load("car1.png"),pygame.image.load("car2.png")] 

# Класс машин
class Object:
    def __init__(self,x,y,width,height,image,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed

    def move(self):
        if self.y <= HEIGHT:
            display.blit(self.image,(self.x,self.y))
            #pygame.draw.rect(display,RED,(self.x,self.y,self.width,self.height))
            self.y += self.speed
            return True
        else:
            self.y = -HEIGHT + 300 + randint(230,278)
            return False
    def return_self(self,x,y,image):
        self.x = x
        self.y = y
        #self.width = width
        #self.height = height
        self.image = image 
        display.blit(self.image,(self.x,self.y))

# Функия за нас будет создавать массив машин (образы наших машин)
def create_car_arr(array):
    
    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-100,0),    45,80,img,randint(5,8))) # (х позиция,y позиция ,ширина машины,высота машины,скорость)
    
    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-500,-400), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-700,-600), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-900,-800), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-1100,-1000), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-1300,-1200), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-1500,-1400), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-1700,-1600), 45,80,img,randint(5,8)))

    choise = randint(0,2)
    img = car_img[choise]
    array.append(Object(randint(146,WIDTH - 190),randint(-1900,-1800), 45,80,img,randint(5,8)))



# прорисовка массива
def draw_array(array):
    for car in array:
        check = car.move()
        if not check:
            choise = randint(0,2)
            img = car_img[choise]
            x = randint(145,650)
            y = randint(-400,-80)

            car.return_self(x,y,img)
# дорога
doroga_img = pygame.image.load("doroga.png")
doroga_img2 = pygame.image.load("doroga2.png")
y = 0
y2 = - HEIGHT
def doroga():
    global y,y2
    if y <= HEIGHT:
        display.blit(doroga_img,(0,y))
        y += 4
    else:
        y = 0
    if y2 <= 0:
        display.blit(doroga_img2,(0,y2))
        y2 += 4
    else:
        y2 = -HEIGHT

# Пишем текст на экране
def print_text (message,x,y, font_color = (255, 255, 255), font_type = 'text.otf',font_size = 30):
    font_type = pygame.font.Font(font_type,font_size)
    text = font_type.render(message,True,font_color)
    display.blit(text,(x,y))

# Пауза
def pause():
    paused = True
    pygame.mixer.music.pause()
    while paused: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
        print_text("Пауза.Нажмите Enter чтобы продолжить.", 130,300)

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RETURN]:
            paused = False    
        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()

# Игра ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def game_cycle ():
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound.stop(game_over_sound)
    game=True
    car_arr = []
    create_car_arr(car_arr)
   
# Цикл игры ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    while game:
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверяем, закрывается ли окно
            if event.type == pygame.QUIT:
                sys.exit()
                game = False
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            left()     
        if keys[pygame.K_RIGHT]:
            right()
        if keys[pygame.K_UP]:
            up()
        if keys[pygame.K_DOWN]:
            down()             
        if keys[pygame.K_ESCAPE]:
            pause() 
        
        doroga() # дорога
        draw_player() # Игрок
        draw_array(car_arr) # машины
        check_if_borders() #проверка на границы
        print_text("Очки: " + str(scores), 570,10) # счётчик очков
        left_btn = Button(80,40)
        right_btn = Button(80,40)
        up_btn = Button(50,80)
        down_btn = Button(50,80)

        left_btn.draw(200,550,"←",left,40)
        right_btn.draw(300,550,"→",right,40)
        up_btn.draw(600,450,"↑",up,40)
        down_btn.draw(600,550,"↓",down,40)

        if check_collision(car_arr):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play (game_over_sound)
            game = False
        if check_collision2(car_arr):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play (game_over_sound)
            game = False

        count_scores(car_arr)

        pygame.display.update() # обновление дисплея
        pygame.display.flip() # После отрисовки всего, переворачиваем экран
         # Держим цикл на правильной скорости
        clock.tick(60)
    return game_over() #/////////////////////////////////////////////////////////////////////////////////////////////////////

# функция столкновений 
def check_collision(barriers):
    for barrier in barriers:
        if usr_y + usr_height >= barrier.y:
            if  barrier.x + 5 <=usr_x <= barrier.x + 41 or barrier.x + 9  <= usr_x  +usr_widrh <= barrier.x + 41:
                if  usr_y + usr_height <= barrier.y or usr_y + usr_height >= barrier.y +79 :
                    return False
                else:
                    return True
def check_collision2(barriers):
    for barrier in barriers:
        if usr_y <= barrier.y + 79:
            if barrier.x + 5 <=usr_x <= barrier.x + 45 or barrier.x + 5 <= usr_x  + usr_widrh <= barrier.x + 45:
                if  usr_y  <= barrier.y or usr_y  >= barrier.y + 79:
                    return False
                else:
                    return True

# Игровое меню
menu_bc = pygame.image.load("фон.png")
def show_menu():
    global menu_bc
    start_btn = Button(320,70)
    quit_btn =  Button(400,70)

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        display.blit(menu_bc,(0,0))
        start_btn.draw(20,400,"Начать игру!",start_game,50)
        quit_btn.draw(20,500,"Выйти из игры.",quit,50)
        pygame.display.update()
        clock.tick(60)

def start_game():
    global scores,usr_y,usr_x,usr_height,HEIGHT,WIDTH
    scores = 0
    usr_y = HEIGHT - usr_height - 100
    usr_x = WIDTH / 2 - 80
    while game_cycle():
        scores = 0
        usr_y = HEIGHT - usr_height - 100
        usr_x = WIDTH / 2 - 80

# функция завершения игры
def game_over():
    global max_scores, scores
    if scores > max_scores:
        max_scores = scores
    stopped = True
    while stopped:  
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
        print_text("Игра окончена.", 290,300)
        print_text("Нажмите Enter чтобы начать заново,Esc чтобы выйти.",15,340)
        print_text("Максимум очков: " + str(max_scores),290,380)
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.Sound.stop(game_over_sound)
            return False

        pygame.display.update()
        clock.tick(15)

# Счётчик очков
scores = 0
max_scores = 0
above_car = False
def count_scores(barriers):
    global scores, above_car
    if not above_car:
        for barrier in barriers:
            if barrier.y <= usr_y + usr_height /2 <= barrier.y + barrier.height:
                if usr_y <= barrier.y:
                    above_car = True
                    break
    else:
        for barrier in barriers:
            if usr_y + usr_height <= barrier.y:
                scores +=1
                above_car = False

# Кнопки 
class Button:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.inactive_clr = (194, 188, 188)
        self.active_clr = (214, 212, 212)
    def draw(self,x,y,message,action=None,font_size = 30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display,self.active_clr,(x,y,self.width,self.height))

            if click[0] == 1 and action is not None: # (0) левая кнопка мыши (1) нажата 
                if action == quit:
                    pygame.QUIT()
                    sys.exit()
                else:
                    action()
        else:
            pygame.draw.rect(display,self.inactive_clr,(x,y,self.width,self.height))
        print_text(message = message, x = x + 5 , y = y + 10, font_size = font_size)

show_menu()
pygame.QUIT()
sys.exit()
