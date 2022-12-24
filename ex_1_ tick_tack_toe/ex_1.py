#3.Создайте программу для игры в "Крестики-нолик
import pygame
# import sys
pygame.init()

def check_win(lst,sign):
    for row in lst:
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if lst[0][col] == sign and lst[1][col] == sign and lst[2][col] == sign:
            return sign
        if lst[0][0] == sign and lst[1][1] == sign and lst[2][2] == sign:
            return sign
        if lst[0][2] == sign and lst[1][1] == sign and lst[2][0] == sign:
            return sign
    return False



size_block = 100
margin = 10
width = heigth = size_block * 3  + margin * 4

size_window = (width, heigth ) 

screen = pygame.display.set_mode((size_window))
pygame.display.set_caption("крестики-нолики")

red = (255, 0, 0)
green = (0, 255, 0)              
white = (255, 255, 255)
black = (0, 0, 0)  

lst = [[0] * 3 for i in range(3)]                  
query = 0 #1 2 3 4 5 6 7 8 
while True:                                  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()   # получение координат при нажатии мышки
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if lst[row][col] == 0:
                if query % 2 == 0:
                    lst[row][col] = 'x'
                else:
                    lst[row][col] = 'O'
                query = query + 1



    for row in range(3): 
        for col in range(3):
            if lst[row][col] == 'x':
                color = red
            elif lst[row][col] == 'O':
                color = green
            else:
                color = white 
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin                         
            pygame.draw.rect(screen,color, (x, y, size_block, size_block))
            if color == red:
                pygame.draw.line(screen, white, (x, y), (x + size_block, y + size_block), 3)
                pygame.draw.line(screen, white, (x + size_block, y), (x, y + size_block), 3)
            elif color == green:
                pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2, 3)
    if (query - 1) % 2 == 0:
        game_over = check_win(lst,'x')
    else:
        game_over = check_win(lst,'O')

    if game_over:
        font = pygame.font.SysFont('stxingkai', 200)
        text = font.render(game_over,True,black)
        screen.blit(text,[200,200])
        # exit()

        
    
    pygame.display.update()                                            
    
#img = pygame.image.load("путь к файлу с картинкой") иконка окна программы
#pygame.display.set_icon(img)