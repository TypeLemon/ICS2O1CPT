""" 
----------------------------------------------------------------------------------------------
Name: CPT.py

Purpose: Interactive mini-games that test the user's computer knowledge on course content

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
off_white = (245, 245, 245)
  
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
notepad_image = pygame.transform.scale(note, [250, 230])
antivirus = pygame.image.load("antivirus.png").convert()
antivirus.set_colorkey(white)
antivirus_image = pygame.transform.scale(antivirus, [90, 100])
CPU = pygame.image.load("CPU.png").convert()
CPU.set_colorkey(white)
CPU_image = pygame.transform.scale(CPU, [80, 90])
motherboard = pygame.image.load("motherboard.jpeg").convert()
motherboard.set_colorkey(white)
motherboard_image = pygame.transform.scale(motherboard, [100, 90])
RAM = pygame.image.load("RAM.png").convert()
RAM.set_colorkey(white)
RAM_image = pygame.transform.scale(RAM, [110, 100])
graphics = pygame.image.load("graphicscard.png").convert()
graphics.set_colorkey(white)
graphics_image = pygame.transform.scale(graphics, [110, 90])
keyboard = pygame.image.load("keyboard.png").convert()
keyboard.set_colorkey(white)
keyboard_image = pygame.transform.scale(keyboard, [120, 80])
hard_drive = pygame.image.load("harddrive.jpeg").convert()
hard_drive.set_colorkey(white)
hard_drive_image = pygame.transform.scale(hard_drive, [100, 100])
power_supply = pygame.image.load("powersupply.png").convert()
power_supply.set_colorkey(white)
power_supply_image = pygame.transform.scale(power_supply, [110, 100])
monitor = pygame.image.load("monitor.jpg").convert()
monitor.set_colorkey(white)
monitor_image = pygame.transform.scale(monitor, [110, 90])
mouse = pygame.image.load("mouse.jpg").convert()
mouse.set_colorkey(white)
mouse_image = pygame.transform.scale(mouse, [70, 90])
cart = pygame.image.load("shoppingcart.png").convert()
cart.set_colorkey(off_white)
cart_image = pygame.transform.scale(cart, [305, 256])
floor_image = pygame.image.load("floor.png").convert()

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

   #if scene == 3:
        

    # --- Game logic should go here

    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command. 
    
    # Render font and text
    button_font = pygame.font.SysFont("Oswald", 25, False, False)
    small_font = pygame.foont.SysFont("Alegreya", 15, False, False)

    cus_text_1 = button_font.render("Character", True, white)
    cus_text_2 = button_font.render("Customization", True, white)
    trivia_text = button_font.render("Trivia Mini-Game", True, white) 
    shopping_text_1 = button_font.render("Shopping", True, white)
    shopping_text_2 = button_font.render("Mini-Game", True, white)
    checklist_text = button_font.render("Checklist", True, black)

    CPU_text = small_font.render("CPU", True, black)
    mouse_text = small_font.render("Mouse", True, black)
    monitor_text = small_font.render("Monitor", True, black)
    power_text = small_font.render("Power Supply", True, black)
    graphics_text = small_font.render("Graphics Card", True, black)
    RAM_text = small_font.render("RAM", True, black)    
    keyboard_text = small_font.render("Keyboard", True, black)
    antivirus_text = small_font.render("Antivirus", True, black)
    hard_drive_text = small_font.render("Hard Drive", True, black)
    motherboard_text = small_font.render("Motherboard", True, black)

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
        screen.blit(CPU_image, [180, 100])
        screen.blit(antivirus_image, [280, 100])
        screen.blit(motherboard_image, [370, 100])
        screen.blit(RAM_image, [470, 100])
        screen.blit(graphics_image, [580, 105])
        screen.blit(keyboard_image, [95, 240])
        screen.blit(hard_drive_image, [230, 235])
        screen.blit(power_supply_image, [340, 235])
        screen.blit(monitor_image, [480, 235])
        screen.blit(mouse_image, [620, 230])
        screen.blit(cart_image, [70, 345])
        screen.blit(floor_image, [0, 569])
        screen.blit(notepad_image, [545, 355])

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
    if scene == 3:
        screen.blit(checklist_text, [615, 410])
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit() 