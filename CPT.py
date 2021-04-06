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
off_white_2 = (246, 246, 246)
  
# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ICS2O1 CPT")

# Set positions
trivia_x = 455
trivia_y = 460
shopping_x = 260
shopping_y = 460
button_length = 160
button_width = 80
exit_x = 0
exit_y = 0
exit_length = 95
exit_width = 65
cart_x = 70
cart_y = 327
cart_length = 305
cart_width = 255
true_x = 530
true_y = 525
false_x = 660
false_y = 525

mouse_click_position = [0,0]
scene = 0
cursor_size = [10, 10]

# Set hardware booleans
button_pressed = False
CPU_selected = False 
mouse_selected = False
monitor_selected = False
reset_checklist = False 
power_supply_selected = False
antivirus_selected = False
motherboard_selected = False
RAM_selected = False
graphics_card_selected = False
keyboard_selected = False
hard_drive_selected = False

# Set other variables
checklist_set = 1

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
cart_image = pygame.transform.scale(cart, [cart_length, cart_width])
floor_image = pygame.image.load("floor.png").convert()
trans_box = pygame.image.load("transparentbox.png").convert()
reset = pygame.image.load("reset.png").convert()
reset.set_colorkey(off_white_2)
reset_button = pygame.transform.scale(reset, [90, 90]) 
x_mark = pygame.image.load("x_mark.png").convert()
x_mark.set_colorkey(off_white_2)
x_mark_image = pygame.transform.scale(x_mark, [25, 25])
checkmark = pygame.image.load("checkmark.png").convert()
checkmark.set_colorkey(off_white_2)
checkmark_image = pygame.transform.scale(checkmark, [25, 25])
sticky_box = pygame.image.load("sticky_box.png").convert()
sticky_box_image = pygame.transform.scale(sticky_box, [25, 25])
gameshow = pygame.image.load("gameshow.png").convert()
gameshow_back = pygame.transform.scale(gameshow, [800, 520])
true_image = pygame.image.load("true.png").convert()
true_button = pygame.transform.scale(true_image, [110, 60])
false_image = pygame.image.load("false.png").convert()
false_button = pygame.transform.scale(false_image, [110, 60])
grey_rect = pygame.image.load("greyrectangle.png").convert()
grey_image = pygame.transform.scale(grey_rect, [800, 90])

# Set images to variables for mouse click
CPU_var = CPU_image
RAM_var = RAM_image
graphics_var = graphics_image
keyboard_var = keyboard_image
hard_drive_var = hard_drive_image
supply_var = power_supply_image
monitor_var = monitor_image
mouse_var = mouse_image
motherboard_var = motherboard_image
antivirus_var = antivirus_image
cursor = trans_box

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

"""
Numbers that control the different screens
0 = Main Menu
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
            cursor_x = mouse_click_position[0] - cursor_size[0]/2;
            cursor_y = mouse_click_position[1] - cursor_size[1]/2;

    if scene == 0:
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
        if trivia_button_pressed:
            print("Started trivia game.")
            scene = 2
        elif shop_button_pressed:
            print("Started shopping game.")
            scene = 3         

    if scene == 2 or scene == 3:
        if (exit_x <= mouse_click_position[0] and mouse_click_position[0] <= exit_y + exit_length) and (exit_y <= mouse_click_position[1] and mouse_click_position[1] <= exit_y + exit_width):
            print("User quit, go to main menu.")
            scene = 0                       
            revert_checklist = True
    
    if scene == 3:
        # Check if mouse click is on CPU icon
        if (180 <= mouse_click_position[0] and mouse_click_position[0] <= 180 + 80) and (100 <= mouse_click_position[1] and mouse_click_position[1] <= 100 + 90):
            print("CPU selected")
            CPU_var = trans_box
            cursor = CPU_image
            CPU_selected = True

        # Check if mouse click is on antivirus icon
        if (280 <= mouse_click_position[0] and mouse_click_position[0] <= 280 + 90) and (100 <= mouse_click_position[1] and mouse_click_position[1] <= 100 + 100):
            print("Antivirus selected")
            antivirus_var = trans_box
            cursor = antivirus_image
            antivirus_selected = True
            
        # Check if mouse click is on motherboard icon
        if (370 <= mouse_click_position[0] and mouse_click_position[0] <= 370 + 100) and (100 <= mouse_click_position[1] and mouse_click_position[1] <= 100 + 90):
            print("Motherboard selected")
            motherboard_var = trans_box
            cursor = motherboard_image
            motherboard_selected = True

        # Check if mouse click is on the RAM icon
        if (470 <= mouse_click_position[0] and mouse_click_position[0] <= 470 + 110) and (100 <= mouse_click_position[1] and mouse_click_position[1] <= 100 + 100):
            print("RAM selected")
            RAM_var = trans_box
            cursor = RAM_image
            RAM_selected = True 

        # Check if mouse click is on the graphics card icon
        if (580 <= mouse_click_position[0] and mouse_click_position[0] <= 580 + 110) and (105 <= mouse_click_position[1] and mouse_click_position[1] <= 105 + 90):
            print("Graphics card selected")
            graphics_var = trans_box
            cursor = graphics_image
            graphics_card_selected = True

        # Check if mouse click is on the keyboard icon
        if (95 <= mouse_click_position[0] and mouse_click_position[0] <= 95 + 120) and (240 <= mouse_click_position[1] and mouse_click_position[1] <= 240 + 80):
            print("Keyboard selected")
            keyboard_var = trans_box
            cursor = keyboard_image
            keyboard_selected = True

        # Check if mouse click is on the hard drive icon
        if (230 <= mouse_click_position[0] and mouse_click_position[0] <= 230 + 100) and (235 <= mouse_click_position[1] and mouse_click_position[1] <= 235 + 100):
            print("Hard drive selected")
            hard_drive_var = trans_box
            cursor = hard_drive_image
            hard_drive_selected = True

        # Check if mouse click is on the power supply icon
        if (340 <= mouse_click_position[0] and mouse_click_position[0] <= 340 + 110) and (235 <= mouse_click_position[1] and mouse_click_position[1] <= 235 + 100):
            print("Power supply selected")
            supply_var = trans_box
            cursor = power_supply_image
            power_supply_selected = True

        # Check if mouse click is on the monitor icon
        if (480 <= mouse_click_position[0] and mouse_click_position[0] <= 480 + 110) and (235 <= mouse_click_position[1] and mouse_click_position[1] <= 235 + 90):
            print("Monitor selected")
            monitor_var = trans_box
            cursor = monitor_image
            monitor_selected = True

        # Check if mouse click is on the mouse icon
        if (620 <= mouse_click_position[0] and mouse_click_position[0] <= 620 + 70) and (230 <= mouse_click_position[1] and mouse_click_position[1] <= 230 + 90):
            print("Mouse selected")
            mouse_var = trans_box
            cursor = mouse_image
            mouse_selected = True
        
        # Check if mouse click is on the reset button
        if (10 <= mouse_click_position[0] and mouse_click_position[0] <= 10 + 90) and (500 <= mouse_click_position[1] and mouse_click_position[1] <= 500 + 90):
            print("User chose to switch to checklist 2")
            cursor = trans_box
            motherboard_var = motherboard_image
            hard_drive_var = hard_drive_image
            antivirus_var = antivirus_image
            keyboard_var = keyboard_image
            RAM_var = RAM_image
            graphics_var = graphics_image
            supply_var = power_supply_image
            monitor_var = monitor_image
            mouse_var = mouse_image
            CPU_var = CPU_image
            reset_checklist = True
            checklist_set = 2     

    # --- Game logic should go here

    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command. 
    
    # Render font and text
    button_font = pygame.font.SysFont("Oswald", 25, False, False)
    small_font = pygame.font.SysFont("Alegreya", 23, False, False)
    
    trivia_text = button_font.render("Trivia Mini-Game", True, white) 
    shopping_text_1 = button_font.render("Shopping", True, white)
    shopping_text_2 = button_font.render("Mini-Game", True, white)
    checklist_text_1 = button_font.render("Checklist 1", True, black)
    checklist_text_2 = button_font.render("Checklist 2", True, black)

    CPU_text = small_font.render("CPU", True, black)
    mouse_text = small_font.render("Mouse", True, black)
    monitor_text = small_font.render("Monitor", True, black)
    power_text = small_font.render("Power", True, black)
    supply_text = small_font.render("Supply", True, black)
    graphics_text = small_font.render("Graphics", True, black)
    card_text = small_font.render("Card", True, black)
    RAM_text = small_font.render("RAM", True, black)    
    keyboard_text = small_font.render("Keyboard", True, black)
    antivirus_text = small_font.render("Antivirus", True, black)
    hard_drive_text = small_font.render("Hard Drive", True, black)
    motherboard_text = small_font.render("Motherboard", True, black)

    instr_text_1 = button_font.render("Welcome to the computer hardware shopping game! The checklist below tells you", True, black)
    instr_text_2 = button_font.render("which items to click and put into the cart. You'll know you chose the correct item", True, black)
    instr_text_3 = button_font.render("when the red x turns into a checkmark. Once you get all 5 checkmarks, click on", True, black)
    instr_text_4 = button_font.render("the reset button to get the second checklist and repeat!", True, black)

    # Copy images to screen
    if scene == 0:
        screen.fill(light_green)
        screen.blit(title_image, [70, 50])
        screen.blit(typing_image, [170, 280])
        screen.blit(brain_image, [460, 280])
    if scene == 2:
        screen.blit(gameshow_back, [0, 0])
        screen.blit(grey_image, [0, 510])
        screen.blit(true_button, [true_x, true_y])
        screen.blit(false_button, [false_x, false_y])
    if scene == 3:
        screen.fill(grey)
        screen.blit(CPU_var, [180, 100])
        screen.blit(antivirus_var, [280, 100])
        screen.blit(motherboard_var, [370, 100])
        screen.blit(RAM_var, [470, 100])
        screen.blit(graphics_var, [580, 105])
        screen.blit(keyboard_var, [95, 240])
        screen.blit(hard_drive_var, [230, 235])
        screen.blit(supply_var, [340, 235])
        screen.blit(monitor_var, [480, 235])
        screen.blit(mouse_var, [620, 230])
        screen.blit(cursor, [cursor_x, cursor_y])
        screen.blit(cart_image, [cart_x, cart_y])
        screen.blit(floor_image, [0, 550])
        screen.blit(notepad_image, [545, 355])
        screen.blit(reset_button, [10, 500])
        screen.blit(x_mark_image, [583, 430])
        screen.blit(x_mark_image, [583, 457])
        screen.blit(x_mark_image, [583, 484])
        screen.blit(x_mark_image, [583, 511])
        screen.blit(x_mark_image, [670, 452])

        if reset_checklist:
            checklist_set = 2

        if checklist_set == 1:
            if CPU_selected:
                screen.blit(sticky_box_image, [583, 430])
                screen.blit(checkmark_image, [583, 430])
            if mouse_selected:
                screen.blit(sticky_box_image, [583, 457])
                screen.blit(checkmark_image, [583, 457])
            if RAM_selected:
                screen.blit(sticky_box_image, [583, 484])
                screen.blit(checkmark_image, [583, 484])
            if hard_drive_selected:
                screen.blit(sticky_box_image, [583, 511])
                screen.blit(checkmark_image, [583, 511])
            if power_supply_selected:
                screen.blit(sticky_box_image, [670, 452])
                screen.blit(checkmark_image, [670, 452])
        if checklist_set == 2:
            if antivirus_selected:
                screen.blit(sticky_box_image, [583, 430])
                screen.blit(checkmark_image, [583, 430])
            if monitor_selected:
                screen.blit(sticky_box_image, [583, 457])
                screen.blit(checkmark_image, [583, 457])
            if keyboard_selected:
                screen.blit(sticky_box_image, [583, 484])
                screen.blit(checkmark_image, [583, 484])
            if motherboard_selected:
                screen.blit(sticky_box_image, [583, 511])
                screen.blit(checkmark_image, [583, 511])
            if graphics_card_selected:
                screen.blit(sticky_box_image, [670, 452])
                screen.blit(checkmark_image, [670, 452])

    # --- Drawing code 
    if scene == 0:
        pygame.draw.rect(screen, orange, [shopping_x, shopping_y, button_length, button_width])
        pygame.draw.rect(screen, lavender, [trivia_x, trivia_y, button_length, button_width])
    if scene == 2 or scene == 3:
        pygame.draw.rect(screen, coral, [exit_x, exit_y, exit_length, exit_width])
        screen.blit(exit_image, [exit_x, exit_y + 5])
    
    # Copy text to screen
    if scene == 0:
        screen.blit(shopping_text_1, [shopping_x + 40, shopping_y + 20])
        screen.blit(shopping_text_2, [shopping_x + 35, shopping_y + 40])
        screen.blit(trivia_text, [trivia_x + 8, trivia_y + 30])
    if scene == 3:
        screen.blit(instr_text_1, [110, 13])
        screen.blit(instr_text_2, [110, 33])
        screen.blit(instr_text_3, [110, 53])
        screen.blit(instr_text_4, [110, 73])

        # Shopping checklist possibilities 1 & 2
        if checklist_set == 1:
            screen.blit(checklist_text_1, [615, 410])
            screen.blit(CPU_text, [608, 440])
            screen.blit(mouse_text, [608, 465])
            screen.blit(RAM_text, [608, 490])
            screen.blit(hard_drive_text, [608, 515])
            screen.blit(power_text, [693, 460])
            screen.blit(supply_text, [693, 477])
        if checklist_set == 2:
            screen.blit(checklist_text_2, [615, 410])
            screen.blit(antivirus_text, [608, 440])
            screen.blit(monitor_text, [608, 465])
            screen.blit(keyboard_text, [608, 490])
            screen.blit(motherboard_text, [608, 515])
            screen.blit(graphics_text, [693, 460])
            screen.blit(card_text, [693, 477])
            
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
      
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()