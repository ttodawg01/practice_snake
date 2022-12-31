import pygame

pygame.init()

dis=pygame.display.set_mode((600,500))
pygame.display.update()
pygame.display.set_caption('Cachetona Game')
game_ending = False

snake_color = (255,255,255) 
red = (255,0,0) #boxes we want to catch with the snake

x1 = 300
y1 = 300

x1_change = 0 #this is used to hold the updating values of the X and Y cooridinates
y1_change = 0

clock = pygame.time.Clock()

while not game_ending:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ending = True
        if event.type == pygame.KEYDOWN
        pygame.draw.rect(dis,snake_color,[200,150,20,20]) #the [] determines the length and height of the snake moving
        #dis represents all of this dislaying to the screen
        pygame.display.update()


pygame.quit()
quit()