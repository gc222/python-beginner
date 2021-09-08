import pygame
import os                   # to use os.path for files
pygame.font.init()          # load fonts
pygame.mixer.init()         # load sounds

# note: run file with python main.py in powershell
# note: close window with X button doesnt work, type ctrl+c in terminal to close

# notice how movement is done, the spaceship and bullet "moves" by redrawing the images
# on every frame, they're both drawn at 60 frames per second. The spaceships are set to
# be redrawn at x + 5 pixels at every frame, thus it moves at 300 pixels per second.
# you can see it by removing the line, WIN.blit(SPACE, (0, 0)), run file to see 

# notice how the spaceship movement and bullet user input is different. The spaceship
# movement is within the while loop where it is possible to hold down the arrow or
# wasd keys to consistently move the spaceship around. The bullets are placed inside
# a for loop which records events, this only allows one bullet to be shot per button press
# rather than a button hold.  

# Tasks:
# setup loop and event body as first body of code (ALWAYS HAVE LOOP AND EVENT) 
# setup window colour and size
# get spaceship images, resize and rotate, setup position
# draw spaceship (surface) onto window using blit(surface, coords)
# prevent spaceship from moving off window and middle border
# setup key listener key.get_pressed() and map keys to movement (def yellow_movement)
# setup bullet using .Rect and map keys and add colour


# set window dimension
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # set window size
pygame.display.set_caption("First Game!")           # set window name

# COLOURS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0 , 10, HEIGHT)   # line in middle

# SOUNDS
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# VARIABLES
YELLOW_WINS = "Yellow Wins!"
RED_WINS = "Red Wins!"

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 120                                            
VEL = 3                                             # velocity
BULLET_VEL = 5                                      # bullet velocity
MAX_BULLETS = 3                                      
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40          

# EVENTS: create two new events for bullet colliding with spaceship 
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# image.load --> use os.path to get image path --> ./Assets/spaceship_yellow.png
# scale down images (transform.scale) and rotate images (transform.rotate)
# note: the width and height are constants so when rotated, the width is actually
# the height length, and height is the width length
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    # draw the spaceship whever the corresponding rectangle's x y coords are
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))    # use .blit() to draw surfaces on screen
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, RED)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, YELLOW)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10)),

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()            # update the display 

    # the rectangle represents the spaceships and we move the rectangles around the screen
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:    # LEFT, yellow.x-VEL to prevent moving off window
        yellow.x -= VEL             # VEL = 5, moves 300 pixel left per second, 5p * 60fps
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.height < BORDER.x:    # RIGHT          
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:    # UP, subtract b/c negative y is up in the window
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT:  # DOWN, add b/c positive y is down
        yellow.y += VEL

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:    # LEFT
        red.x -= VEL             
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.height < WIDTH:    # RIGHT          
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:    # UP, subtract b/c negative y is up in the window
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT:    # DOWN, add b/c positive y is down
        red.y += VEL

    # loop over the bullets lists to find if any bullet collides with spaceship or offscreen
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL          # bullet moving right: 420px per second, (7*60)
        if red.colliderect(bullet):         # use .colliderect for collision between two rectanble objects
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)                      # remove bullets if collide
        elif bullet.x > WIDTH:                                 # remove bullets offscreen
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):          

            # must use an event because we can't modify the bullets from here (within this function)
            # post event to modify
            pygame.event.post(pygame.event.Event(YELLOW_HIT))   
            red_bullets.remove(bullet)                      
        elif bullet.x < 0:                                  
            red_bullets.remove(bullet)

def draw_winner(text):
    if text == YELLOW_WINS:
        draw_text = WINNER_FONT.render(text, 1, YELLOW)
    else:
        draw_text = WINNER_FONT.render(text, 1, RED)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)               # display for set time and reset game (3 seconds)




def main():
    # rectangle object to store coords to draw (x y positions and size of rect)
    # this is so we can change the positions when it is moved, in this function
    # rect allows us to ref the position of the spaceship with .x .y
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)      
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    winner_text = ""

    # one loop essentially means one frame, each frame/loop draws the surfaces,
    # records event (k)
    clock = pygame.time.Clock()
    run = True              # usually need a loop to open and keep the game open
    while run:    
        clock.tick(FPS)     # set while loop to run at 60fps b/c code throttles

        # loops over all the events occurring during playing the game
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:   # e.g. quitting the game window will end loop
                run = False    
                pygame.quit()                # stop loop and quit game                       
            
            # we don't handle key pressed like the spaceship, we use events 
            # we place it here
            if event.type == pygame.KEYDOWN:        # if key pressed event
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:  
                    # the bullet will be on the right of the spaceship with w: 10px, h: 5px
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 + 4, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2 + 5, 10, 5)
                    red_bullets.append(bullet)   # bullets fired is added to bullets list
                    BULLET_FIRE_SOUND.play()
            
            # event is posted from handle_bullets(), if hit: play sound
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        
        if red_health <= 0:
            winner_text = YELLOW_WINS
        if yellow_health <= 0:
            winner_text = RED_WINS

        keys_pressed = pygame.key.get_pressed()     # takes key input
        yellow_movement(keys_pressed, yellow)       # handle movement
        red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        # draw here, so it goes over the rest of the other drawings
        if winner_text != "":               # if winner_text displayed: draw text and break loop
            draw_winner(winner_text)        # goes back to where main() is called and is called again
            break                           # this will reset the game (new window pops up)

    

if __name__ == "__main__":
    while True:             
        main()              # runs main() when run directly from this file: $ python main.py

