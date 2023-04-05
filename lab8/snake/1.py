import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (46, 139, 87)
greenyellow = (173,255,47)
yellowgreen = (154,205,50)
blue = (137, 207, 240)
 
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25) #шрифт
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow) #Метод для отображения текста
    dis.blit(value, [dis_width / 6, dis_height / 3+50]) #подставляем на указанные координаты

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellowgreen, [x[0], x[1], snake_block, snake_block]) #рисуем змейку

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
def add_level(level):
    dis.fill(blue)
    if(level==1): 
        return
    elif(level==2):
        pygame.draw.rect(dis, yellow, [0, 0, 300, snake_block])

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Round - округлять число
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #randrange - рандомные цифры
    current_level = 1

    while not game_over:
        
        while game_close == True:
            
            dis.fill(blue)
            message("You Lost!", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() #перезапускаем игру
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            if current_level>1:
                if x1<=300 and y1>=10:
                    print(x1)
                    print(y1)
                    game_close=True
                    break
            else:
                game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        current_score=Length_of_snake-1
    
        if current_score>=2:
            add_level(2)
            current_level=2
            
        
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()