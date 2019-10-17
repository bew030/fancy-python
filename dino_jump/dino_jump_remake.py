import pygame 

pygame.init() # initializing pygame, necessary, in general do at the beginning 

walkRight = [pygame.image.load('sprite/R'+str(x)+'.png') for x in range(1,10)] 
walkLeft = [pygame.image.load('sprite/L'+str(x)+'.png') for x in range(1,10)]
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

game_border_x = 1000
game_border_y = 500 
x = 50 
y = 385
width = 64
height = 64 
velocity = 5

window = pygame.display.set_mode((game_border_x,game_border_y)) # setting display window, (width, height)
pygame.display.set_caption('Dino Jump') # naming the game window 

isJump = False 
jumpCount = 10 
realistic = True

# need to keep track of what direction character is moving, are they moving, how many steps theyve moved 
left = False 
right = False 
walkCount = 0 # gives you positioning of sprite in list 


def redrawGameWindow():
    global walkCount 
    
    #window.fill((0,0,0)) # black background
    window.blit(bg, (0,0)) # filling with background image 
    if (walkCount + 1) >= 27: # 9 sprites, each sprite for 3 frames 
        walkCount = 0 # pygame.draw.rect(window,(255,255,255),(x,y,width,height)) # look at website to see what shapes to draw (window, color, (x,y,width,height))
    if left: 
        window.blit(walkLeft[walkCount//3],(x,y)) 
        walkCount += 1 
    elif right: 
        window.blit(walkRight[walkCount//3],(x,y))
        walkCount += 1
    else: 
        window.blit(char,(x,y))
    pygame.display.update() # updates screen # can use pygame.display.flip() to update whole screen, but typically slower

# main loop 
run = True 
while run:
    clock.tick(27) # pygame.time.delay(27) # milleseconds 
    for event in pygame.event.get(): # get a list of all the events that happen 
        if event.type == pygame.QUIT: 
            run = False 

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        x -= velocity 
        left = True 
        right = False 
        if x < 0: # setting game boundary 
            x = 0
    elif keys[pygame.K_RIGHT]:
        x += velocity 
        left = False 
        right = True
        if x > (game_border_x-width): # setting game boundary 
            x = game_border_x-width
    else: 
        left = False
        right = False
        walkCount = 0 # what's the point of that? 

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False 
            left = False
            walkCount = 0 
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

    redrawGameWindow()

pygame.quit()
