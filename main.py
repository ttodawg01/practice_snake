import pygame

pygame.init()

dis=pygame.display.set_mode((600,500))
pygame.display.update()
pygame.display.set_caption('Cachetona Game')
game_ending = False

snake_color = (255,255,255) 
red = (255,0,0) #boxes we want to catch with the snake
black = (0,0,0)


x1 = 300
y1 = 300

x1_change = 0 #this is used to hold the updating values of the X and Y cooridinates
y1_change = 0

clock = pygame.time.Clock()

while not game_ending:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ending = True
        #keys to get our snake moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10 #going to the left with the left arrow key X axis
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10 #going to the right with the right arrrow key on the x axis
                y1_change = 0
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10 #press the bottom arrow key to go down on the Y axis
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10 #press the up arrow key to go up the Y axis

        x1 += x1_change #the reason we do this is because its based to do whatever the user presses to the box can change directions
        y1 += y1_change
        dis.fill(black) #make sure the background screen is black

        pygame.draw.rect(dis, snake_color, [x1, y1, 20, 20])#the [] determines the length and height of the snake moving
        #dis represents all of this dislaying to the screen
        pygame.display.update()

        clock.tick(30)


pygame.quit()
quit()