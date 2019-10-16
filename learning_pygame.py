import pygame 

pygame.init() # initializing pygame, necessary, in general do at the beginning 

game_border_x = 500
game_border_y = 500 
x = 59 
y = 300 
width = 40 
height = 60 
velocity = 5

window = pygame.display.set_mode((game_border_x,game_border_y)) # setting display window, (width, height)
pygame.display.set_caption('test') # naming the game window 

isJump = False 
jumpCount = 10 
realistic = True
# main loop 
run = True 
while run:
    pygame.time.delay(15) # milleseconds 
    for event in pygame.event.get(): # get a list of all the events that happen 
        if event.type == pygame.QUIT: 
            run = False 

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        x -= velocity 
        if x < 0: # setting game boundary 
            x = 0
    if keys[pygame.K_RIGHT]:
        x += velocity 
        if x > (game_border_x-width): # setting game boundary 
            x = game_border_x-width
    '''        
    if keys[pygame.K_UP]:
        y -= velocity
        if y < 0: # setting game boundary 
            y = 0
    if keys[pygame.K_DOWN]:
        y += velocity
        if y > (game_border_y-height): # setting game boundary
            y = (game_border_y-height)
    '''
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:  
        if jumpCount >= -10:
            if realistic: 
                difference = (jumpCount**2)/5 # more realistic parabolic motion; set a gui button in the future that gives you the option to make it more realistic or not 
                if jumpCount < 0: 
                    y += difference
                else: 
                    y -= difference
                jumpCount -= 1 
            else: 
                difference = jumpCount
                y -= difference
                jumpCount -=1
        else:
            isJump = False  
            jumpCount = 10 

    window.fill((0,0,0))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height)) # look at website to see what shapes to draw (window, color, (x,y,width,height)) # how come this goes after?
    pygame.display.update() # updates screen # can use pygame.display.flip() to update whole screen, but typically slower 

pygame.quit()
