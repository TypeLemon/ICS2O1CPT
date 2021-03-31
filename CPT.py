""" 
----------------------------------------------------------------------------------------------
Name: CPT.py

Purpose: Interactive mini-games that test the user's computer knowledge on course content
testing
Author: Yeh.A
Created: 28/03/2021 
----------------------------------------------------------------------------------------------
"""
import pygame
pygame.init()
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
salmon = (219, 156, 145)
orange = (232, 170, 56)
lavender = (203, 155, 242)
light_green = (153, 199, 135)
coral = (240, 122, 101)
grey = (211, 211, 211)
off_black = (40, 40, 40)
  
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ICS2O1 CPT")

# Load and size images
title = pygame.image.load("title.png").convert()
title_image = pygame.transform.scale(title, [700, 230])
exit_arrow = pygame.image.load("exitarrow.png").convert()
exit_arrow.set_colorkey(white)
exit_image = pygame.transform.scale(exit_arrow, [90, 50])
typing = pygame.image.load("typing.jpeg").convert()
typing_image = pygame.transform.scale(typing, [250, 145])
brain = pygame.image.load("brain.jpeg").convert()
brain_image = pygame.transform.scale(brain, [210, 145])
note = pygame.image.load("stickynote.png").convert()
note.set_colorkey(white)
notepad_image = pygame.transform.scale(note, [220, 200])
antivirus = pygame.image.load("antivirus.png").convert()
antivirus.set_colorkey(white)
antivirus_image = pygame.transform.scale(antivirus, [100, 110])
CPU = pygame.image.load("CPU.png").convert()
CPU.set_colorkey(white)
CPU_image = pygame.transform.scale(CPU, [95, 110])

# Set positions
custom_x = 130
custom_y = 460
trivia_x = 530
trivia_y = 460
shopping_x = 330
shopping_y = 460
button_length = 160
button_width = 80
exit_x = 0
exit_y = 0
exit_length = 95
exit_width = 65

button_pressed = False
mouse_click_position = [0,0]
scene = 0
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

"""
Numbers that control the different screens
0 = Main Menu
1 = Character Customization Screen (pink)
2 = Trivia Mini Game (lavender)
3 = Shopping Mini Game (orange)
"""
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            print("User asked to quit.")
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button.")
            mouse_click_position = pygame.mouse.get_pos()

    if scene == 0:
        # Check if the mouse click is in the character customization button area
        if (custom_x <= mouse_click_position[0] and mouse_click_position[0] <= custom_x + button_length) and (custom_y <= mouse_click_position[1] and mouse_click_position[1] <= custom_y + button_width):
            cus_button_pressed = True
        else:
            cus_button_pressed = False
        # Check if the mouse click is in the trivia mini game button area
        if (trivia_x <= mouse_click_position[0] and mouse_click_position[0] <= trivia_x + button_length) and (trivia_y <= mouse_click_position[1] and mouse_click_position[1] <= trivia_y + button_width):
            trivia_button_pressed = True
        else:
            trivia_button_pressed = False
        # Check if the mouse click is in the shopping mini game button area
        if (shopping_x <= mouse_click_position[0] and mouse_click_position[0] <= shopping_x + button_length) and (shopping_y <= mouse_click_position[1] and mouse_click_position[1] <= shopping_y + button_width):
            shop_button_pressed = True
        else:
            shop_button_pressed = False
        
        # Main menu buttons that switch screens
        if cus_button_pressed:
            print("Started character customization.")
            scene = 1
        elif trivia_button_pressed:
            print("Started trivia game.")
            scene = 2
        elif shop_button_pressed:
            print("Started shopping game.")
            scene = 3

    if scene == 1 or scene == 2 or scene == 3:
        if (exit_x <= mouse_click_position[0] and mouse_click_position[0] <= exit_y + exit_length) and (exit_y <= mouse_click_position[1] and mouse_click_position[1] <= exit_y + exit_width):
            print("User quit, go to main menu.")
            scene = 0

    # --- Game logic should go here

    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command. 
    
    # Render font and text
    button_font = pygame.font.SysFont("Oswald", 25, False, False)
    cus_text_1 = button_font.render("Character", True, white)
    cus_text_2 = button_font.render("Customization", True, white)
    trivia_text = button_font.render("Trivia Mini-Game", True, white) 
    shopping_text_1 = button_font.render("Shopping", True, white)
    shopping_text_2 = button_font.render("Mini-Game", True, white)

    # Copy images to screen
    if scene == 0:
        screen.fill(light_green)
        screen.blit(title_image, [70, 50])
        screen.blit(typing_image, [170, 280])
        screen.blit(brain_image, [460, 280])
    if scene == 1:
        screen.fill(grey)
    if scene == 2:
        screen.fill(black)
    if scene == 3:
        screen.fill(grey)
        screen.blit(notepad_image, [575, 385])
        screen.blit(antivirus_image, [300, 200])
        screen.blit(CPU_image, [180, 200])

    # --- Drawing code 
    if scene == 0:
        pygame.draw.rect(screen, salmon, [custom_x, custom_y, button_length, button_width])
        pygame.draw.rect(screen, orange, [shopping_x, shopping_y, button_length, button_width])
        pygame.draw.rect(screen, lavender, [trivia_x, trivia_y, button_length, button_width])
    if scene == 1 or scene == 2 or scene == 3:
        pygame.draw.rect(screen, coral, [exit_x, exit_y, exit_length, exit_width])
        screen.blit(exit_image, [exit_x, exit_y + 5])
    
    # Copy text to screen
    if scene == 0:
        screen.blit(cus_text_1, [custom_x + 40, custom_y + 20])
        screen.blit(cus_text_2, [custom_x + 20, custom_y + 40])
        screen.blit(shopping_text_1, [shopping_x + 40, shopping_y + 20])
        screen.blit(shopping_text_2, [shopping_x + 35, shopping_y + 40])
        screen.blit(trivia_text, [trivia_x + 8, trivia_y + 30])
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit() 