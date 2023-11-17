import pygame, sys
import time
import json
import random
from list_grids import new_grid

from pygame.locals import *
pygame.init()
WIDTH = 800
HEIGHT = 550
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5

def generate(sudoku_grid):    
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    button_font = pygame.font.SysFont('Comic Sans MS', 20)
    
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    
    for i in range(0, len(sudoku_grid[0])):
        for j in range(0, len(sudoku_grid[0])):
            if(0<sudoku_grid[i][j]<10):
                value = myfont.render(str(sudoku_grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
 
    button_1 = pygame.Rect(550, 250, 200, 50)
    pygame.draw.rect(win, (0, 0, 0), button_1)
    button1_text = button_font.render(("Solve Puzzle!"), True, (255, 255, 255))
    win.blit(button1_text, (590, 260))
    pygame.display.update()

    click = False
    while True: 
        pos = pygame.mouse.get_pos()
        if button_1.collidepoint(pos):
            if click:
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
##### Simple #####
N = 9
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()

def isSafe(grid, row, col, num):

    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

count_tries = 0
count_errors = 0
def solveSudoku(grid, row, col, win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1,win)
    for num in range(1, N + 1, 1):

        if isSafe(grid, row, col, num):
            grid[row][col] = num
            pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
            value = myfont.render(str(num), True, (0,0,0))
            win.blit(value, ((col+1)*50 +15,(row+1)*50))
            pygame.display.update()
            global count_tries
            count_tries = count_tries + 1
            pygame.time.delay(25)
 
            if solveSudoku(grid, row, col + 1, win):
                return True
        else:
            grid[row][col] = 0
            pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
            pygame.display.update()
            global count_errors
            count_errors += 1
            pygame.time.delay(1)
    return False

def simple(grid): 
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    newfont = pygame.font.SysFont('Comic Sans MS', 20)
    
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, (original_grid_element_color))
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()

    start = time.time()
    solveSudoku(grid,0,0,win)
    stop = time.time()
    difference = stop - start
    
    algo_title = newfont.render(("Default Algorithm:"), True, original_grid_element_color)
    win.blit(algo_title, (520, 150))

    tries = newfont.render(("Number of Tries:"), True, original_grid_element_color)
    tries_number = newfont.render((str(count_tries)), True, original_grid_element_color)
    win.blit(tries, (520, 200))
    win.blit(tries_number, (710, 200))
    pygame.display.update()

    errors = newfont.render(("Number of Errors:"), True, original_grid_element_color)
    error_number = newfont.render((str(count_errors)), True, original_grid_element_color)
    win.blit(errors, (520, 250))
    win.blit(error_number, (710, 250))
    pygame.display.update()

    time_taken = newfont.render(("Time Taken:"), True, original_grid_element_color)
    time_taken1 = newfont.render((str('%.2f'%difference)+" s"), True, original_grid_element_color)
    win.blit(time_taken, (520, 300))
    win.blit(time_taken1, (710, 300))
    pygame.display.update()

    tries_num = count_tries
    error_num = count_errors
    time_num = difference

    pygame.time.delay(750)

    button_1 = pygame.Rect(550, 370, 200, 50)
    pygame.draw.rect(win, (0, 0, 0), button_1)
    button1_text = newfont.render(("Smart Game Solver"), True, (255, 255, 255))
    win.blit(button1_text, (560, 380))
    pygame.display.update()

    click = False
    
    while True: 

        pos = pygame.mouse.get_pos()
        if button_1.collidepoint(pos):
            if click:
                return tries_num, error_num, time_num

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

#### BT ####
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print (arr[i][j], end = " ")
        print()
 
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

def check_location_is_safe(arr, row, col, num):

    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)

count_tries = 0
count_errors = 0
def solve_sudoku(arr, win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    l =[0, 0]

    if(not find_empty_location(arr, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):

        if(check_location_is_safe(arr, 
                          row, col, num)):
            arr[row][col]= num
            pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
            value = myfont.render(str(num), True, (0,0,0))
            win.blit(value, ((col+1)*50 +15,(row+1)*50))
            pygame.display.update()
            pygame.time.delay(25)

            global count_tries
            count_tries = count_tries + 1
            
            if(solve_sudoku(arr,win)):
                return True
            else:
                arr[row][col] = 0
                pygame.draw.rect(win, background_color, ((col+1)*50 + buffer, (row+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                pygame.display.update()
                global count_errors
                count_errors += 1
                pygame.time.delay(1)
    
    return False

def backtracking(grid):    
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    newfont = pygame.font.SysFont('Comic Sans MS', 20)
    
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()

    start = time.time()
    solve_sudoku(grid, win)
    stop = time.time()
    difference = stop - start

    algo_title = newfont.render(("SGS Algorithm:"), True, original_grid_element_color)
    win.blit(algo_title, (520, 150))
    
    tries = newfont.render(("Number of Tries:"), True, original_grid_element_color)
    tries_number = newfont.render((str(count_tries)), True, original_grid_element_color)
    win.blit(tries, (520, 200))
    win.blit(tries_number, (710, 200))
    pygame.display.update()

    errors = newfont.render(("Number of Errors:"), True, original_grid_element_color)
    error_number = newfont.render((str(count_errors)), True, original_grid_element_color)
    win.blit(errors, (520, 250))
    win.blit(error_number, (710, 250))
    pygame.display.update()

    time_taken = newfont.render(("Time Taken:"), True, original_grid_element_color)
    time_taken1 = newfont.render((str('%.2f'%difference)+" s"), True, original_grid_element_color)
    win.blit(time_taken, (520, 300))
    win.blit(time_taken1, (710, 300))
    pygame.display.update()

    button_1 = pygame.Rect(550, 370, 200, 50)
    pygame.draw.rect(win, (0, 0, 0), button_1)
    button1_text = newfont.render(("Analytics Report"), True, (255, 255, 255))
    win.blit(button1_text, (570, 380))
    pygame.display.update()    

    bt_tries = count_tries
    bt_errors = count_errors
    bt_time = difference

    click = False
    while True: 
        pos = pygame.mouse.get_pos()
        if button_1.collidepoint(pos):
            if click:
                return bt_tries, bt_errors, bt_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

###Algo Analysis###
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
def algo_analysis(tries_num1, error_num1, time_num1, tries_num2, error_num2, time_num2):
    
    screen = pygame.display.set_mode((800, 500),0,32)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    button_font = pygame.font.SysFont('Comic Sans MS', 20)
    
    screen.fill((255,255,255))
    draw_text('Algorithm Analysis', font, (0, 0, 0), screen, 250, 20)
    newfont = pygame.font.SysFont('Comic Sans MS', 20)
    original_grid_element_color = (52, 31, 151)

    button_1 = pygame.Rect(115, 270, 200, 50)
    button_2 = pygame.Rect(515, 270, 200, 50)

    pygame.draw.rect(screen, (211, 211, 211), button_1)
    button1_text = button_font.render(("Default Algorithm"), True, (0, 0, 0))
    screen.blit(button1_text, (135, 280))
    pygame.draw.rect(screen, (211, 211, 211), button_2)
    button2_text = button_font.render(("SGS Algorithm"), True, (0, 0, 0))
    screen.blit(button2_text, (545, 280))

    draw_text("Number of Tries:", newfont, original_grid_element_color, screen, 100, 110)
    draw_text((str(tries_num1)), newfont, original_grid_element_color, screen, 300, 110)

    draw_text("Number of Errors:", newfont, original_grid_element_color, screen, 100, 160)
    draw_text((str(error_num1)), newfont, original_grid_element_color, screen, 300, 160)
    
    draw_text("Time Taken:", newfont, original_grid_element_color, screen, 100, 210)
    draw_text((str('%.2f'% time_num1)), newfont, original_grid_element_color, screen, 300, 210)

    draw_text("Number of Tries:", newfont, original_grid_element_color, screen, 500, 110)
    draw_text((str(tries_num2)), newfont, original_grid_element_color, screen, 700, 110)

    draw_text("Number of Errors:", newfont, original_grid_element_color, screen, 500, 160)
    draw_text((str(error_num2)), newfont, original_grid_element_color, screen, 700, 160)
    
    draw_text("Time Taken:", newfont, original_grid_element_color, screen, 500, 210)
    draw_text((str('%.2f'% time_num2)), newfont, original_grid_element_color, screen, 700, 210)

    # print("tries1: "+ str(tries_num1))
    # print("error1: "+ str(error_num1))
    # print("time1: "+ str(time_num1))
    # print("tries2: "+ str(tries_num2))
    # print("error2: "+ str(error_num2))
    # print("time2: "+ str(time_num2))

    button_1 = pygame.Rect(290, 380, 250, 50)
    pygame.draw.rect(screen, (0, 0, 0), button_1)
    button1_text = newfont.render(("Generate New Puzzle!"), True, (255, 255, 255))
    screen.blit(button1_text, (320, 390))
    pygame.display.update() 

    click = False

    while True: 
        pos = pygame.mouse.get_pos()
        if button_1.collidepoint(pos):
            if click:
                return 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

#### Difficulty ####
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
def difficulty_level():
    pygame.display.set_caption('Menu')
    screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
    font = pygame.font.SysFont('Comic Sans MS', 25)
    button_font = pygame.font.SysFont('Comic Sans MS', 30)

    while True:
        screen.fill((255,255,255))
        draw_text('Do you want:', font, (0, 0, 0), screen, 330, 120)
 
        mx, my = pygame.mouse.get_pos()
        
        easier = 1
        harder = 2
 
        button_1 = pygame.Rect(300, 170, 200, 50)
        button_2 = pygame.Rect(300, 240, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                return easier
        if button_2.collidepoint((mx, my)):
            if click:
                return harder
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        button1_text = button_font.render(("Easier"), True, (255, 255, 255))
        screen.blit(button1_text, (360, 173))
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        button2_text = button_font.render(("Harder"), True, (255, 255, 255))
        screen.blit(button2_text, (350, 243))
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()

def process_easier_grid(a,b,c,d,e,f):
    average_tries = (a+d)/2
    average_error = (b+e)/2
    average_time = (c+f)/2

    # print("Average Tries: " + str(average_tries))
    # print("Average Errors:" + str(average_error))
    # print("Average Time: " + str(average_time))

    new_tries = average_tries - 100
    new_error = average_error - 500 
    new_time = average_time - 2

    easier_state = 1

    return new_tries, new_error, new_time, easier_state

def process_harder_grid(a,b,c,d,e,f):
    average_tries = (a+d)/2
    average_error = (b+e)/2
    average_time = (c+f)/2

    print("Average Tries: " + str(average_tries))
    print("Average Errors:" + str(average_error))
    print("Average Time: " + str(average_time))

    new_tries = average_tries + 100
    new_error = average_error + 500 
    new_time = average_time + 2

    harder_state = 2

    return new_tries, new_error, new_time, harder_state

def process_grid(new_tries, new_error, new_time, state, grid_pos, new_grid):
    if new_tries == 0:
        grid = new_grid[20]
        return grid
    else:
        ran_num = random.randint(1,5)
        if state == 1:
            store_num = new_tries + new_error + new_time
            grid = new_grid[grid_pos-ran_num]
            return grid
        elif state == 2:
            store_num = new_tries + new_error + new_time
            grid = new_grid[grid_pos+ran_num]
            return grid

def gridcopy(grid):
    grid_json = json.dumps(grid)
    grid_copy = json.loads(grid_json)
    return grid_copy

def main():
    new_tries, new_error, new_time, state, grid_pos = 0, 0, 0, 0, 0
    list_grid = new_grid
    while True:
        grid = (process_grid(new_tries, new_error, new_time, state, grid_pos, list_grid))
        grid2 = gridcopy(grid)
        grid_pos = new_grid.index(grid)
        if grid_pos <= 0:
            break
        # print(grid_pos)
        generate(grid)
        a,b,c =(simple(grid))
        d,e,f = (backtracking(grid2))
        algo_analysis(a,b,c,d,e,f)
        level = (difficulty_level())
        if level == 1:
           new_tries, new_error, new_time, state = (process_easier_grid(a,b,c,d,e,f))
        elif level == 2:
            new_tries, new_error, new_time, state = (process_harder_grid(a,b,c,d,e,f))
        
main()

