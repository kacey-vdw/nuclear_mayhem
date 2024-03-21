import pygame, button, random, zombies
pygame.init()

# ------------------------------------------------ #

#game window
screen = pygame.display.set_mode((1000, 600))#window is 1000 x 600 pixels
pygame.display.set_caption("Nuclear mayhem")

#colours and fonts
font = pygame.font.SysFont("arialblack", 40)
text_colour = (255, 255, 255)
outline = (84,90,97)
darker_outline = (74,80,87)
green_colour = (0, 255, 0)
fence_colour = (183, 183, 183)

#harley interview
#fast/addictive/rapid paced, real logic with how accidents occur and how to fix them. expected pause button, mini tutorial, 
#mini tutorial showing how to fix each individual thing

# ------------------------------------------------ #

#load button/bg images
title_screen_img = pygame.image.load("images/title_screen.png").convert_alpha()

fence_bg_img = pygame.image.load("images/fence_fixing.png").convert_alpha() #fence minigame background

map_console_closeup_img = pygame.image.load("images/map_console_closeup.PNG").convert_alpha() #map console background
reactor_console_closeup_img = pygame.image.load("images/reactor_console_closeup.PNG").convert_alpha() #reactor console background
routine_console_closeup_img = pygame.image.load("images/routine_console_closeup.PNG").convert_alpha() #routine console background

left_arrow_img = pygame.image.load("images/left_arrow.PNG").convert_alpha() #left arrow button image
right_arrow_img = pygame.image.load("images/right_arrow.PNG").convert_alpha() #right arrow button image

pause_img = pygame.image.load("images/pause.PNG").convert_alpha() #pause button image
unpause_img = pygame.image.load("images/play.PNG").convert_alpha() #play button image

left_img = pygame.image.load("images/left_panel.PNG").convert_alpha() #left console image
right_img = pygame.image.load("images/right_panel.PNG").convert_alpha() #right console image
centre_img = pygame.image.load("images/centre_panel.PNG").convert_alpha() #centre console image

tutorial_img = pygame.image.load("images/button_tutorial.png").convert_alpha() #tutorial button image
quit_img = pygame.image.load("images/button_quit.png").convert_alpha() #quit button image
back_img = pygame.image.load("images/button_back.png").convert_alpha() #go back button image
play_img = pygame.image.load("images/button_play.png").convert_alpha() #play button image
leaderboard_img = pygame.image.load("images/leaderboard.png").convert_alpha() #leaderboard button image
statistics_img = pygame.image.load("images/button_statistics.png").convert_alpha() #statistics button image

sliderg_img = pygame.transform.scale(pygame.image.load("images/slider_grip.png").convert_alpha(), (60,25)) #slider grip image

power_img = pygame.image.load("images/power_button.png").convert_alpha() #power button images
power_off_img = pygame.image.load("images/power_off_button.png").convert_alpha()

routine_unpressed_img = pygame.image.load("images/routine_rect_unpressed.png").convert_alpha() #routine grey rectangle buttons
routine_pressed_img = pygame.image.load("images/routine_rect_pressed.png").convert_alpha()
routine_switch_down_img = pygame.image.load("images/routine_switch_down.png").convert_alpha() #routine grey flip switchs
routine_switch_up_img = pygame.image.load("images/routine_switch_up.png").convert_alpha()
routine_green_img = pygame.image.load("images/routine_green.png").convert_alpha() #routine coloured buttons
routine_red_img = pygame.image.load("images/routine_red.png").convert_alpha()

clipboard_img = pygame.image.load("images/clipboard.png").convert_alpha() #clipboard button image

red_tri_img = pygame.image.load("images/red_tri.png").convert_alpha() #routine red shapes buttons
red_circle_img = pygame.image.load("images/red_circle.png").convert_alpha()
red_rect_img = pygame.image.load("images/red_rect.png").convert_alpha()
red_semi_img = pygame.image.load("images/red_semi.png").convert_alpha()

green_tri_img = pygame.image.load("images/green_tri.png").convert_alpha() #routine green shapes buttons
green_circle_img = pygame.image.load("images/green_circle.png").convert_alpha()
green_rect_img = pygame.image.load("images/green_rect.png").convert_alpha()
green_semi_img = pygame.image.load("images/green_semi.png").convert_alpha()

blue_tri_img = pygame.image.load("images/blue_tri.png").convert_alpha() #routine blue shapes buttons
blue_circle_img = pygame.image.load("images/blue_circle.png").convert_alpha()
blue_rect_img = pygame.image.load("images/blue_rect.png").convert_alpha()
blue_semi_img = pygame.image.load("images/blue_semi.png").convert_alpha()

yellow_tri_img = pygame.image.load("images/yellow_tri.png").convert_alpha() #routine yellow shapes buttons
yellow_circle_img = pygame.image.load("images/yellow_circle.png").convert_alpha()
yellow_rect_img = pygame.image.load("images/yellow_rect.png").convert_alpha()
yellow_semi_img = pygame.image.load("images/yellow_semi.png").convert_alpha()

clipboard_screen_img = pygame.image.load("images/clipboard_screen.png").convert_alpha() #clipboard background

map_none = pygame.image.load("images/map_none.png").convert_alpha() #different map images with outlines
map_entrance = pygame.image.load("images/map_entrance.png").convert_alpha()
map_building = pygame.image.load("images/map_building.png").convert_alpha()
map_building2 = pygame.image.load("images/map_building2.png").convert_alpha()
map_containment = pygame.image.load("images/map_containment.png").convert_alpha()
map_tower = pygame.image.load("images/map_tower.png").convert_alpha()
map_wires = pygame.image.load("images/map_wires.png").convert_alpha()

info_entrance = pygame.image.load("images/info_entrance.png").convert_alpha()
info_building = pygame.image.load("images/info_building.png").convert_alpha()
info_building2 = pygame.image.load("images/info_building2.png").convert_alpha()
info_containment = pygame.image.load("images/info_containment.png").convert_alpha()
info_tower = pygame.image.load("images/info_tower.png").convert_alpha()
info_wires = pygame.image.load("images/info_wires.png").convert_alpha()

radioactive_spill = pygame.image.load("images/radioactive_spill.png").convert_alpha() #radioactive material for zombies

burnt_background = pygame.image.load("images/burnt_building.png").convert_alpha() #fire minigame images
extinguisher_off_img = pygame.transform.scale(pygame.image.load("images/extinguisher_off.png").convert_alpha(),(262, 247))
extinguisher_on_img = pygame.transform.scale(pygame.image.load("images/extinguisher_on.png").convert_alpha(),(262, 247))
fire_img = pygame.image.load("images/fire.png").convert_alpha()

zombie_img = pygame.transform.scale(pygame.image.load("images/zombie1.png"), (200, 300))

leaderboard_table_img = pygame.image.load("images/leaderboard_table.png").convert_alpha()

# ------------------------------------------------ #
#codes for routine clipboard

arrows_text = ["↑", "↓"]
grey_text = ["O", "X"]
colour_text = ["R", "G"]
circle_text = ["Rc", "Yc", "Bc", "Gc"]
semi_text = ["Rs", "Ys", "Bs", "Gs"]
rect_text = ["Rr", "Yr", "Br", "Gr"]
triangle_text = ["Rt", "Yt", "Bt", "Gt"]

# ------------------------------------------------ #
#creating button instances

left_arrow = button.button(50, 270, left_arrow_img, .19) #x coord, y coord, image, scale of image
right_arrow = button.button(700, 270, right_arrow_img, .19)

left_panel_button = button.button(19, 314, left_img, .19)
right_panel_button = button.button(510, 309, right_img, .19)
centre_panel_button = button.button(287, 292, centre_img, .19)

back_minigames_button = button.button(400, 440, back_img, .8)
back_scenes_button = button.button(315, 500, back_img, .8)
back_leaderboard_button = button.button(410, 525, back_img, .7)
back_button3 = button.button(315, 440, back_img, .7)

pause_button = button.button(40, 40, pause_img, 1)
unpause_button = button.button(40, 40, unpause_img, 1)
statistics_button = button.button(280, 220, statistics_img, 1)
quit_button = button.button(280, 360, quit_img, 1)

play_button = button.button(380, 190, play_img, 1)
play_minigame_button = button.button(410, 410, play_img, 0.7)
tutorial_button = button.button(380, 310, tutorial_img, 1)
leaderboard_button = button.button(380, 430, leaderboard_img, 1)

power_button_on = button.button(200, 230, power_img, 0.06)
power_button_off = button.button(200, 230, power_off_img, 0.06)
power_button = power_button_off #placeholder name to change image

routine_unpressed_button1 = button.button(165, 310, routine_unpressed_img, 0.7)
routine_pressed_button1 = button.button(165, 310, routine_pressed_img, 0.7)
routine1 = routine_unpressed_button1 #placeholder names for routine buttons

routine_unpressed_button2 = button.button(237, 310, routine_unpressed_img, 0.7)
routine_pressed_button2 = button.button(237, 310, routine_pressed_img, 0.7)
routine2 = routine_unpressed_button2

routine_unpressed_button3 = button.button(309, 310, routine_unpressed_img, 0.7)
routine_pressed_button3 = button.button(309, 310, routine_pressed_img, 0.7)
routine3 = routine_unpressed_button3

routine_unpressed_button4 = button.button(381, 310, routine_unpressed_img, 0.7)
routine_pressed_button4 = button.button(381, 310, routine_pressed_img, 0.7)
routine4 = routine_unpressed_button4

routine_down_button1 = button.button(170, 190, routine_switch_down_img, .7)
routine_up_button1 = button.button(170, 143, routine_switch_up_img, .7)
r_switch1 = routine_down_button1

routine_down_button2 = button.button(250, 190, routine_switch_down_img, .7)
routine_up_button2 = button.button(250, 143, routine_switch_up_img, .7)
r_switch2 = routine_down_button2

routine_down_button3 = button.button(330, 190, routine_switch_down_img, .7)
routine_up_button3 = button.button(330, 143, routine_switch_up_img, .7)
r_switch3 = routine_down_button3

routine_down_button4 = button.button(410, 190, routine_switch_down_img, .7)
routine_up_button4 = button.button(410, 143, routine_switch_up_img, .7)
r_switch4 = routine_down_button4

routine_green_button1 = button.button(500, 140, routine_green_img, 0.5)
routine_red_button1 = button.button(500, 140, routine_red_img, 0.5)
r_colour_button1 = routine_green_button1

routine_green_button2 = button.button(590, 140, routine_green_img, 0.5)
routine_red_button2 = button.button(590, 140, routine_red_img, 0.5)
r_colour_button2 = routine_green_button2

routine_green_button3 = button.button(680, 140, routine_green_img, 0.5)
routine_red_button3 = button.button(680, 140, routine_red_img, 0.5)
r_colour_button3 = routine_green_button3 

red_tri_button = button.button(520, 270, red_tri_img, 1)
red_rect_button = button.button(520, 353, red_rect_img, 1)
red_circle_button = button.button(630, 270, red_circle_img, 1)
red_semi_button = button.button(630, 353, red_semi_img, 1)

green_tri_button = button.button(520, 270, green_tri_img, 1)
green_rect_button = button.button(520, 353, green_rect_img, 1)
green_circle_button = button.button(630, 270, green_circle_img, 1)
green_semi_button = button.button(630, 353, green_semi_img, 1)

blue_tri_button = button.button(520, 270, blue_tri_img, 1)
blue_rect_button = button.button(520, 353, blue_rect_img, 1)
blue_circle_button = button.button(630, 270, blue_circle_img, 1)
blue_semi_button = button.button(630, 353, blue_semi_img, 1)

yellow_tri_button = button.button(520, 270, yellow_tri_img, 1)
yellow_rect_button = button.button(520, 353, yellow_rect_img, 1)
yellow_circle_button = button.button(630, 270, yellow_circle_img, 1)
yellow_semi_button = button.button(630, 353, yellow_semi_img, 1)

r_tri = green_tri_button #placeholder names for routine shape buttons
r_circle = yellow_circle_button
r_rectangle = blue_rect_button
r_semi = red_semi_button

clipboard_button = button.button(0, 441, clipboard_img, 1)

extinguisher_button = button.button(700, 300, extinguisher_off_img, 1)

zombie_dragged = [False, False, False] #states of zombies being dragged, stored together

zombie1 = zombies.zombie(120, 90, 1.4) #initialising zombies
zombie2 = zombies.zombie(100, 270, 1.4)
zombie3 = zombies.zombie(120, 500, 1.4)

zombie_list = [zombie1, zombie2, zombie3] #list for running through

fence_dragging = [False, False, False, False, False] #states of dragging fence wires
fence_connected = [False, False, False, False, False] #states of fence wires being fixed

# ------------------------------------------------ #
#rectangles: x position, y position, width, length

left_slider_scale = pygame.Rect(400, 163, 10, 250) #slider rectangles
right_slider_scale = pygame.Rect(540, 163, 10, 250)
grip1 = pygame.Rect(374, 381, 60, 25)
grip2 = pygame.Rect(514,381, 60, 25)

shapes_outer = pygame.Rect (515, 265, 230, 180) #aesthetic/appearance rectangles
upper_left = pygame.Rect(520, 270, 107, 80)
upper_right = pygame.Rect(633, 270, 107, 80)
lower_left = pygame.Rect(520, 356, 107, 84)
lower_right = pygame.Rect(633, 356, 107, 84)
panel_rect = pygame.Rect(800, 0, 200, 600)
panel_outline_rect = pygame.Rect(790, 0, 10, 600)
minigame_popup = pygame.Rect(300, 75, 400, 450)
minigame_popup_outline = pygame.Rect(295, 70, 410, 460)

entrance = pygame.Rect(443, 400, 78, 50) #map section rectangles
building = pygame.Rect(54, 313, 152, 120)
building2 = pygame.Rect(155, 180, 95, 90)
containment = pygame.Rect(35, 167, 110, 120)
wires = pygame.Rect(440, 285, 130, 45)
tower = pygame.Rect(270, 170, 115, 105)

radioactive_spill_rect = pygame.Rect(500, 300, 90, 50)

fence_start1 = pygame.Rect(270, 310, 25, 25) #fence minigame rectangles
fence_end1 = pygame.Rect(428, 468, 25, 25)
fence_start2 = pygame.Rect(265, 180, 25, 25)
fence_end2 = pygame.Rect(538, 455, 25, 25)
fence_start3 = pygame.Rect(315, 110, 25, 25)
fence_end3 = pygame.Rect(620, 418, 25, 25)
fence_start4 = pygame.Rect(450, 122, 25, 25)
fence_end4 = pygame.Rect(668, 340, 25, 25)
fence_start5 = pygame.Rect(523, 75, 25, 25)
fence_end5 = pygame.Rect(770, 324, 25, 25)

boss_rect = pygame.Rect(110, 20, 600, 20)

leader1 = pygame.Rect(820, 97, 124, 65)
leader2 = pygame.Rect(820, 170, 124, 65)
leader3 = pygame.Rect(820, 247, 124, 65)
leader4 = pygame.Rect(820, 320, 124, 65)
leader5 = pygame.Rect(820, 394, 124, 65)
leader6 = pygame.Rect(820, 470, 124, 65)

# ------------------------------------------------ #
#functions

#draws text on screen
def draw_text(text, font, text_colour, x, y, scale):
	img = font.render(text, True, text_colour)
	img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
	screen.blit(img, (x, y))

#controls dragging of slider
def slider_movement(grip):
	if pygame.mouse.get_pressed()[0] == 1:#while mouse pressed
		mouse_x, mouse_y = pygame.mouse.get_pos()
		grip.y = mouse_y - 10

		if grip.y < 167:#lower y bound
			grip.y = 168
		if grip.y > 382:#upper y bound
			grip.y = 381

#draws info panel
def draw_panel(panel_rect, panel_outline_rect, seconds, time, points, demand, output, text_colour):
	pygame.draw.rect(screen, outline, panel_rect) #draws background rects
	pygame.draw.rect(screen, darker_outline, panel_outline_rect)

	draw_text("Info panel" , font, text_colour, 810, 0, 0.85) #draws text
	draw_text("Secs: "+str(round(seconds)) , font, text_colour, 810, 100, 0.65)
	draw_text(str(time) , font, text_colour, 810, 140, 1)
	draw_text("Score: "+str(points) , font, text_colour, 810, 200, 0.65)
	draw_text("Demand:", font, text_colour, 810, 265, 0.7)
	draw_text(str(demand)+"MW", font, text_colour, 810, 300, 0.7)
	draw_text("Output:", font, text_colour, 810, 350, 0.7)
	draw_text(str(output)+"MW", font, text_colour, 810, 385, 0.7)

#changes button states
def changing_buttons(button1, button2, placeholder):
	if placeholder == button1:
		return button2
	elif placeholder == button2:
		return button1

#changes coloured buttons states
def colour_change(red, green, blue, yellow, placeholder):
	if placeholder == red:
		return green
	elif placeholder == green:
		return blue
	elif placeholder == blue:
		return yellow
	elif placeholder == yellow:
		return red

#checks if buttons are in correct states
def routine_checker(code, button, code_array, button_state1, button_state2):
	if (code == code_array[1] and button == button_state1) or (code == code_array[0] and button == button_state2):
		return True
	else:
		return False

#checks if shape buttons are in correct states
def routine_checker_shapes(code, button, code_array, red, green, blue, yellow):
	if (code == code_array[0] and button == red) or (code == code_array[3] and button == green) or (code == code_array[2] and button == blue) or (code == code_array[1] and button == yellow):
		return True
	else:
		return False

#formats seconds into 24hr time
def time_format(seconds, days, demand, demand_nums): 
	if days < 5: #until days reaches 5
		time_speed = 7-days
	else: #lower limit is 3 seconds for 10 mins
		time_speed = 3

	if days > 0: #subtracts seconds from first day (7s per 10min)
		seconds -= 756
	if days > 1: #subtract seconds from second day (6s per 10min)
		seconds -= 864
	if days > 2: #subtracts seconds from third day (5s per 10min)
		seconds -= 720
	if days > 3: #subtracts seconds from fourth day (4s per 10min)
		seconds -= 576
	if days > 4: #subtracts seconds from all next days (3s per 10min)
		seconds -= 432*(days-4)

	hours = round(seconds//(6*time_speed)) #number of game hours that have passed
	minutes = round(((seconds//time_speed)*10)-(hours*60)) #number of game minutes passed
	if days == 0:
		hours += 6

	if minutes < 10: #adds 0 if a 1 digit number
		str_minutes = "0" + str(minutes)
	else:
		str_minutes = str(minutes)

	if hours < 10: #adds 0 if 1 digit number
		str_hours = "0" + str(hours)
	else:
		str_hours = str(hours)

	if str_hours == "24" and str_minutes == "00":
		days += 1 #increments days
		str_hours = "00" #sets hours to 0

	for x in range(0,24): #0-23
		if hours == x:
			if minutes == 0: #for beginning of hour
				demand = demand_nums[x]
			elif minutes == 30: #for half hour
				if x == 23: #for when x+1 is out of range
					demand = (demand_nums[0]+demand_nums[23])/2
				else: #set demand to halfway between x and x+1 hour
					demand = (demand_nums[x]+demand_nums[x+1])/2

	result = str_hours + ":" + str_minutes
	return result, days, round(demand)

#controls dragging and connection of fence wires
def wire(node1, end_node1, dragging, connected):
	pos = pygame.mouse.get_pos()

	if dragging == False:
		if pygame.mouse.get_pressed()[0] == 1 and node1.collidepoint(pos):
			dragging = True

	if dragging == True:#while mouse pressed
		connected = False
		pygame.draw.line(screen, (183, 183, 183), node1.center, pos, 19)
		if pygame.mouse.get_pressed()[0] == 0 and end_node1.collidepoint(pos):
			connected = True

	if pygame.mouse.get_pressed()[0] == 0:
		dragging = False

	return dragging, connected
 
def fire(image, scale, fire_rect, ex_rect):
	mid = fire_rect.center #placeholder for centre

	if pygame.mouse.get_pressed()[0] == 1: #on mouse press
		if fire_rect.colliderect(ex_rect): #fire colliding with extinguisher
			scale -= 0.005
	image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
	fire_rect = image.get_rect() #sets rect to size of image
	fire_rect.center = mid #sets centre back to original

	if scale > 0.005: #until too small, keep displaying image
		screen.blit(image, fire_rect)

	return scale, fire_rect

def boss_bar(measure, end, bg_rect):

	rect = pygame.Rect(110, 20, measure*6, 20) #initialises rectangle
	pygame.draw.rect(screen, (56, 56, 56), bg_rect) #draws background rect underneath

	if measure > 80: #81-100
		pygame.draw.rect(screen, (0, 255, 68), rect)

	elif measure > 60: #61-80
		pygame.draw.rect(screen, (174, 255, 0), rect)

	elif measure > 40: #41-60
		pygame.draw.rect(screen, (255, 242, 0), rect)

	elif measure > 20: #21-40
		pygame.draw.rect(screen, (255, 115, 0), rect)

	elif measure > 0: #1-20
		pygame.draw.rect(screen, (255, 0, 0), rect)

	elif measure < 1: #0 #game end if 0 or below
		end = True

	return end

def boss_adjust(measure, change):#change can be neg or pos
	if change < 0: #if neg
		measure += change
	elif change > 0 and measure <= 100-change: #if pos and wont go over 100
		measure += change

	return measure

def update_leaderboard():
	numItems = 6
	while numItems>1: #bubble sorts array by points
		for count in range(0,5):
			if leaderboard[count][0] < leaderboard[count+1][0]:#sorts greatest to smallest					
				temp = leaderboard[count] #scores swapped so it isnt lost
				leaderboard[count] = leaderboard[count+1]
				leaderboard[count+1] = temp
		numItems = numItems-1

	file = open("leaderboard.txt", "w") #opens file in write mode
	for x in range(0,6): #puts contents of leaderboard array into
		leader_line = str(leaderboard[x][0]) + "," + str(leaderboard[x][1]) + "," + str(leaderboard[x][2]) + "," + str(leaderboard[x][3]) + "," + str(leaderboard[x][4])
		file.write(leader_line +'\n') #write on new line
	file.close() #close file

def delete_leaderboard(row_num): #set values of deleted to 0
	for x in range(0,5): #each value in row
		leaderboard[row_num][x] = 0
	update_leaderboard() #sorts and writes into file

def new_leaderboard(new_vals): #if score > sixth rows score, replace it
	if new_vals[0] > leaderboard[5][0]:
		for x in range(0,5): #each value in row
			leaderboard[5][x] = new_vals[x]
	update_leaderboard() #sorts and writes into file

# ------------------------------------------------ #
#game variables

clock = pygame.time.Clock()#so time can be used

draw_routine_popup = False #these decide which popup will appear
draw_fail_routine_popup = False
draw_first_routine_popup = False

routine_check = True

minigame = False
minigame_state = "main"
minigame_states = ["fence", "zombies", "fire"]
                     #0        #1        #2
fps = 60 #frames per second
speed = 5 #speed of slider movement
days = 0 #number of 24 hour days elapsed

coolant_pumps = False

minigame_probability = 1
popup_start_time = 0

control_rod_pos = 0 #default slider value
seconds_irl = 0 #time in seconds
time_formatted = 0 #time in units (string)
points = 0
measure = 100
game_end = False
minigames_no = 0
pauses_no = 0

energy_demand = 1145 #when starting at 6am
energy_output = 0
demand_nums = [1045, 1025, 1035, 1035, 1040, 1055, 1145, 1245, 1300, 1145, 1150, 1145, 1165, 1130, 1245, 1290, 1415, 1475, 1530, 1555, 1530, 1385, 1260, 1160]
control_rod = False

run = True #controls running of program
start = False #controls forced menu screen upon running
game_paused = False #controls use of pause menu


menu_state = "main" #default for menu screen
pause_state = "main" #default for pause screen
game_state ="control panels" #default for game
slider_state = "left" #default left slider

#tutorial variables
tutorial, tutorial_state = False, "control panels"
continue_map, continue_coolant, continue_lslider, continue_rslider = False,False,False,False
clipboard_open, correct_code, demand_tut = False, False, 1145
switch_tut, press_tut, colour_tut = routine_down_button3, routine_unpressed_button2, routine_green_button3
tri_tut, circle_tut, rect_tut, semi_tut = green_tri_button, yellow_circle_button, blue_rect_button, red_semi_button
button1_tut , button2_tut, button3_tut, button4_tut= False,False,False,False
button5_tut, button6_tut, button7_tut = False,False,False
tutorial_popup1, tutorial_popup2, tutorial_popup3, tutorial_popup4, tutorial_popup5 = True, True, True, True, True
old_time_tut = 0


#leaderboard init
leaderboard = [[0]*5 for _ in range(6)] #create array for leaderboard
text_file = open('leaderboard.txt', "r") #open text file
all_lines = text_file.readlines()
for x in range(0,6): #copy text file into array
	pointsL, secondsL, minigamesL, daysL, pausesL = all_lines[x].strip().split(',')
	leaderboard[x][0] = int(pointsL)
	leaderboard[x][1] = int(secondsL)
	leaderboard[x][2] = int(minigamesL)
	leaderboard[x][3] = int(daysL)
	leaderboard[x][4] = int(pausesL)

text_file.close()

#game loop
while run:
	clock.tick(fps)
	screen.fill((52, 78, 91))

	#start screen
	if start == False: #always happens as start defaults to false

		if menu_state == "main": #default state
			#screen.blit(title_screen_img, (0,0))
			draw_text("NUCLEAR MAYHEM", font, outline, 50, 0, 2.15)
			draw_text("NUCLEAR MAYHEM", font, text_colour, 60, 0, 2.1)

			if play_button.draw(screen): #continue to game and reset all variables
				start = True
				draw_routine_popup, draw_fail_routine_popup, draw_first_routine_popup = False, False, False
				coolant_pumps, game_end, control_rod, routine_check = False, False, False, True
				minigame_probability, speed, measure, energy_demand = 1, 5, 100, 1145
				popup_start_time, control_rod_pos, seconds_irl, points = 0,0,0,0
				menu_state, pause_state, game_state, slider_state = "main","main","control panels","left"
				days, minigames_no, pauses_no, energy_output = 0,0,0,0
				grip1 = pygame.Rect(374, 381, 60, 25)
				grip2 = pygame.Rect(514,381, 60, 25)

			if tutorial_button.draw(screen): #start tutorial
				start = True
				tutorial = True
				grip1 = pygame.Rect(374, 381, 60, 25)
				grip2 = pygame.Rect(514,381, 60, 25)
				old_time_tut = pygame.time.get_ticks()

			if leaderboard_button.draw(screen): #open leaderboard
				menu_state = "leaderboard"

		if menu_state == "leaderboard":
			screen.fill((52, 78, 91))
			screen.blit(leaderboard_table_img, (0,-20))
			if back_leaderboard_button.draw(screen):
				menu_state = "main"

			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP and event.button == 1:#if mouse click released
					if leader1.collidepoint(pygame.mouse.get_pos()): #if hovering over X 'button'
						delete_leaderboard(0)
					if leader2.collidepoint(pygame.mouse.get_pos()):
						delete_leaderboard(1)
					if leader3.collidepoint(pygame.mouse.get_pos()):
						delete_leaderboard(2)
					if leader4.collidepoint(pygame.mouse.get_pos()):
						delete_leaderboard(3)
					if leader5.collidepoint(pygame.mouse.get_pos()):
						delete_leaderboard(4)
					if leader6.collidepoint(pygame.mouse.get_pos()):
						delete_leaderboard(5)

			for x in range(0,6):
				draw_text(str(leaderboard[x][0]), font, text_colour, 80, 100+(75*x), 1)
				draw_text(str(leaderboard[x][1]), font, text_colour, 240, 100+(75*x), 1)
				draw_text(str(leaderboard[x][2]), font, text_colour, 400, 100+(75*x), 1)
				draw_text(str(leaderboard[x][3]), font, text_colour, 550, 100+(75*x), 1)
				draw_text(str(leaderboard[x][4]), font, text_colour, 710, 100+(75*x), 1)

# ------------------------------------------------ #
	elif tutorial == True:
		if tutorial_state == "control panels":

			if left_panel_button.draw(screen): #can only click on left panel
				tutorial_state = "left panel"
				old_time_tut = pygame.time.get_ticks()

			centre_panel_button.draw(screen)
			right_panel_button.draw(screen)
			pause_button.draw(screen)
			draw_panel(panel_rect, panel_outline_rect, 0, "06:00", 0, 0, 0, text_colour) #panel with custom variables
			boss_bar(measure, False, boss_rect)

			if tutorial_popup1 == True:
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("Welcome to the tutorial!  " , font, text_colour, 310, 100, 0.65)
				draw_text("This is the control room, " , font, text_colour, 310, 130, 0.65)
				draw_text("and it has three different" , font, text_colour, 310, 160, 0.65)
				draw_text("panels. The boss bar at the" , font, text_colour, 310, 190, 0.65)
				draw_text("top of the screen shows   " , font, text_colour, 310, 220, 0.65)
				draw_text("how close you are to being" , font, text_colour, 310, 250, 0.65)
				draw_text("fired, and the info panel " , font, text_colour, 310, 280, 0.65)
				draw_text("has some useful stuff too." , font, text_colour, 310, 310, 0.65)
				draw_text("You should click on the   " , font, text_colour, 310, 370, 0.65)
				draw_text("left panel first!         " , font, text_colour, 310, 400, 0.65)

				if pygame.time.get_ticks() - old_time_tut >= 15000:
					tutorial_popup1 = False

		elif tutorial_state == "left panel":
			screen.blit(map_console_closeup_img, (0,0))
			screen.blit(map_none, (25 ,145))

			#same code as map panel, but only wires can be clicked
			if entrance.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_entrance, (25, 145))
			if building.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_building, (25, 145))
			if wires.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_wires, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1:
					screen.blit(info_wires, (200, 200))
					continue_map = True
			if containment.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_containment, (25, 145))
			if building2.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_building2, (25, 145))
			if tower.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_tower, (25, 145))

			if continue_map == True:
				if right_arrow.draw(screen):
					tutorial_state = "centre panel"
					old_time_tut = pygame.time.get_ticks()
			right_arrow.draw(screen)
			pause_button.draw(screen)
			boss_bar(measure, False, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, 7, "06:10", 0, 0, 0, text_colour)

			if tutorial_popup2 == True:
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("This is the map panel, here" , font, text_colour, 310, 100, 0.65)
				draw_text("you can learn some stuff " , font, text_colour, 310, 130, 0.65)
				draw_text("about the power plant by" , font, text_colour, 310, 160, 0.65)
				draw_text("clicking on one of the  " , font, text_colour, 310, 190, 0.65)
				draw_text("buildings. Try clicking " , font, text_colour, 310, 220, 0.65)
				draw_text("on the power lines first." , font, text_colour, 310, 250, 0.65)
				draw_text("Once you've done that," , font, text_colour, 310, 280, 0.65)
				draw_text("click on the arrow to " , font, text_colour, 310, 310, 0.65)
				draw_text("see the middle panel!" , font, text_colour, 310, 340, 0.65)

				if pygame.time.get_ticks() - old_time_tut >= 12000:
					tutorial_popup2 = False


		elif tutorial_state == "centre panel":

			screen.blit(reactor_console_closeup_img, (0,20))
			pygame.draw.rect(screen, outline, left_slider_scale)
			pygame.draw.rect(screen, outline, right_slider_scale)
			left_arrow.draw(screen)
			pause_button.draw(screen)
			pygame.draw.circle(screen, (255, 0, 0), (545, 430), 8) #draw red circle
			pygame.draw.circle(screen, (255, 0, 0), (405, 430), 8) #draw red circle
			screen.blit(sliderg_img, (grip1.x, grip1.y)) #draws sliders on screen
			screen.blit(sliderg_img, (grip2.x, grip2.y))
			draw_text("Coolant pumps" , font, text_colour, 160, 190, 0.6)
			draw_text("Control rods" , font, text_colour, 330, 130, 0.5)
			draw_text("Steam output" , font, text_colour, 490, 130, 0.5)

			control_rod_tut = round(-(700/213)*(grip1.y) + (152800/71)) #function to map y values to values between 1-100
			energy_tut = round(-(700/213)*(grip2.y) + (152800/71)) #function to map y values to values between 1-100
			draw_text(str(energy_tut) , font, text_colour, 520, 445, 0.7)

			if power_button_off.draw(screen) and continue_coolant == False: #can only turn coolant on
				continue_coolant = True
				old_time_tut = pygame.time.get_ticks()

			if continue_coolant == True: #can only move left slider
				power_button_on.draw(screen)

				mouse_x, mouse_y = pygame.mouse.get_pos()#mouse position
				if grip1.collidepoint(mouse_x, grip1.y) and mouse_y < 500: #if hovering and in correct Y range
					slider_movement(grip1) #call slider movement procedure

				if control_rod_tut > (demand_tut-30) and control_rod_tut < (demand_tut+30): #if within 30 of demand
					pygame.draw.circle(screen, (0, 255, 0), (405, 430), 8) #draw green circle
					continue_lslider = True #progress when light green

				elif control_rod_tut > (demand_tut-100) and control_rod_tut < (demand_tut+100): #if within 100 of demand
					pygame.draw.circle(screen, (255, 255, 0), (405, 430), 8) #draw yellow circle
					continue_lslider = False 

				else:
					pygame.draw.circle(screen, (255, 0, 0), (405, 430), 8) #draw red circle
					continue_lslider = False

				if continue_lslider == True: #can move right slider
					if grip2.collidepoint(mouse_x, grip2.y) and mouse_y < 500:
						slider_movement(grip2)

					if energy_tut > (demand_tut-30) and energy_tut < (energy_demand+30): ##if within 30 of demand
						pygame.draw.circle(screen, (0, 255, 0), (545, 430), 8) #draw green circle
						continue_rslider = True

					elif energy_tut > (energy_demand-100) and energy_tut < (energy_demand+100): #if within 100 of demand
						pygame.draw.circle(screen, (255, 255, 0), (545, 430), 8) #draw yellow circle
						continue_rslider = False

					else:
						pygame.draw.circle(screen, (255, 0, 0), (545, 430), 8) #draw red circle
						continue_rslider = False

					if continue_rslider == True: #can click on arrow to right panel
						if right_arrow.draw(screen):
							tutorial_state = "right panel"
							old_time_tut = pygame.time.get_ticks()

						pygame.draw.rect(screen, outline, minigame_popup_outline)
						pygame.draw.rect(screen, (110,116,125), minigame_popup)
						draw_text("Awesome, you're producing" , font, text_colour, 310, 100, 0.65)
						draw_text("energy! Press the right " , font, text_colour, 310, 130, 0.65)
						draw_text("arrow to see the next" , font, text_colour, 310, 160, 0.65)
						draw_text("panel!" , font, text_colour, 310, 190, 0.65)


				if tutorial_popup4 == True:
					pygame.draw.rect(screen, outline, minigame_popup_outline)
					pygame.draw.rect(screen, (110,116,125), minigame_popup)
					draw_text("Great job! Now, use the" , font, text_colour, 310, 100, 0.65)
					draw_text("first slider to move the" , font, text_colour, 310, 130, 0.65)
					draw_text("control rods, and the" , font, text_colour, 310, 160, 0.65)
					draw_text("second to release steam" , font, text_colour, 310, 190, 0.65)
					draw_text("to produce energy! Make " , font, text_colour, 310, 220, 0.65)
					draw_text("sure the lights are green!" , font, text_colour, 310, 250, 0.65)

					if pygame.time.get_ticks() - old_time_tut >= 9000:
						tutorial_popup4 = False

			if tutorial_popup3 == True:
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("This is the reactor panel. " , font, text_colour, 310, 100, 0.65)
				draw_text("The button on the left turns" , font, text_colour, 310, 130, 0.65)
				draw_text("on the coolant pumps, the  " , font, text_colour, 310, 160, 0.65)
				draw_text("first slider moves the     " , font, text_colour, 310, 190, 0.65)
				draw_text("control rods, and the      " , font, text_colour, 310, 220, 0.65)
				draw_text("second controls the steam  " , font, text_colour, 310, 250, 0.65)
				draw_text("for energy output.         " , font, text_colour, 310, 280, 0.65)
				draw_text("To start generating energy," , font, text_colour, 310, 330, 0.65)
				draw_text("turn on the coolant." , font, text_colour, 310, 360, 0.65)

				if pygame.time.get_ticks() - old_time_tut >= 15000:
					tutorial_popup3 = False

			boss_bar(measure, False, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, 14, "06:20", 0, 1145, energy_tut, text_colour)
			
			right_arrow.draw(screen)

		elif tutorial_state == "right panel":
			#background art
			screen.blit(routine_console_closeup_img, (0,0))
			pygame.draw.rect(screen, outline, shapes_outer)
			pygame.draw.rect(screen, (110,116,125), upper_right)
			pygame.draw.rect(screen, (110,116,125), upper_left)
			pygame.draw.rect(screen, (110,116,125), lower_right)
			pygame.draw.rect(screen, (110,116,125), lower_left)

			#non-clickable buttons, info panel, boss bar
			left_arrow.draw(screen)
			pause_button.draw(screen)
			boss_bar(measure, False, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, 21, "06:30", 0, 1145, energy_tut, text_colour)

			#draw buttons ----------------------
			routine_down_button1.draw(screen)
			routine_down_button2.draw(screen)
			if switch_tut.draw(screen): #clickable button
				switch_tut = routine_up_button3 #changes state
				button1_tut = True #boolean for checking if all buttons are correct
			routine_down_button4.draw(screen)

			routine_unpressed_button1.draw(screen)
			if press_tut.draw(screen):
				press_tut = routine_pressed_button2
				button2_tut = True
			routine_unpressed_button3.draw(screen)
			routine_unpressed_button4.draw(screen)

			routine_green_button1.draw(screen)
			routine_green_button2.draw(screen)
			if colour_tut.draw(screen):
				colour_tut = routine_red_button3
				button3_tut = True

			if tri_tut.draw(screen):
				tri_tut = blue_tri_button
				button4_tut = True
			if circle_tut.draw(screen):
				circle_tut = red_circle_button
				button5_tut = True
			if rect_tut.draw(screen):
				rect_tut = yellow_rect_button
				button6_tut = True
			if semi_tut.draw(screen):
				semi_tut = green_semi_button
				button7_tut = True
			# ----------------------------------

			#check if all buttons are correct
			if button1_tut and button2_tut and button3_tut and button4_tut and button5_tut and button6_tut and button7_tut: 
				tutorial_state = "popup"

			if clipboard_button.draw(screen): #open clipboard
				clipboard_open = True

			if clipboard_open == True: #when clipboard is open
				screen.blit(clipboard_screen_img, (0,0))

				if back_scenes_button.draw(screen): #go back to panel
					clipboard_open = False

				draw_text("- ↓↓↑↓", font, outline, 350, 175, 1)
				draw_text("- OXOO", font, outline, 340, 250, 1)
				draw_text("- GGR", font, outline, 330, 325, 1)
				draw_text("- Bt Rc Yr Gs", font, outline, 320, 400, 1)

			if tutorial_popup5 == True:
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("This is the routine panel," , font, text_colour, 310, 100, 0.65)
				draw_text("you must do regular checks" , font, text_colour, 310, 130, 0.65)
				draw_text("here by matching the      " , font, text_colour, 310, 160, 0.65)
				draw_text("buttons to the clipboard  " , font, text_colour, 310, 190, 0.65)
				draw_text("codes. Try it out, most of" , font, text_colour, 310, 220, 0.65)
				draw_text("it has been done for you! " , font, text_colour, 310, 250, 0.65)

				if pygame.time.get_ticks() - old_time_tut >= 10000:
					tutorial_popup5 = False

		elif tutorial_state == "popup":
			pygame.draw.rect(screen, outline, minigame_popup_outline)
			pygame.draw.rect(screen, (110,116,125), minigame_popup)
			draw_text("Good job!" , font, text_colour, 410, 90, 1)
			draw_text("You completed the tutorial," , font, text_colour, 310, 160, 0.65)
			draw_text("feel ready to try the real " , font, text_colour, 310, 190, 0.65)
			draw_text("thing? Give it a go!       " , font, text_colour, 310, 220, 0.65)
			draw_text("Just be careful, sometimes " , font, text_colour, 310, 250, 0.65)
			draw_text("unexpected things happen..." , font, text_colour, 310, 280, 0.65)

			if back_minigames_button.draw(screen): #resets variables and goes to main menu

				start = False
				tutorial, tutorial_state = False, "control panels"
				continue_map, continue_coolant, continue_lslider, continue_rslider = False,False,False,False
				clipboard_open, correct_code, demand_tut = False, False, 1145
				switch_tut, press_tut, colour_tut = routine_down_button3, routine_unpressed_button2, routine_green_button3
				tri_tut, circle_tut, rect_tut, semi_tut = green_tri_button, yellow_circle_button, blue_rect_button, red_semi_button
				button1_tut , button2_tut, button3_tut, button4_tut= False,False,False,False
				button5_tut, button6_tut, button7_tut = False,False,False
				tutorial_popup1, tutorial_popup2, tutorial_popup3, tutorial_popup4, tutorial_popup5 = True, True, True, True, True

# ------------------------------------------------ #

	elif game_end == True: #when boss bar measure is 0
		new_values = [points, round(seconds_irl), minigames_no, days, pauses_no] #stores game vals

		#draw popup
		pygame.draw.rect(screen, outline, minigame_popup_outline)
		pygame.draw.rect(screen, (110,116,125), minigame_popup)
		draw_text("Game over" , font, text_colour, 420, 90, 1)
		draw_text("You were fired. Well, at  " , font, text_colour, 310, 160, 0.65)
		draw_text("least you tried. Those folks" , font, text_colour, 310, 190, 0.65)
		draw_text("with no power will have to" , font, text_colour, 310, 220, 0.65)
		draw_text("figure something out.     " , font, text_colour, 310, 250, 0.65)

		if back_minigames_button.draw(screen): #resets variable and goes to leaderboard
				game_end = False
				start = False
				measure = 100
				menu_state = "leaderboard"
				new_leaderboard(new_values) 

# ------------------------------------------------ #

	#check if game is paused
	elif game_paused == True: #when game is paused
		
		#check menu state
		if pause_state == "main": #pause menu
			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)
			draw_text("PAUSED", font, text_colour, 180, 5, 2.5)

			#draw pause screen buttons
			if statistics_button.draw(screen): #open statistics
				pause_state = "statistics"
			if quit_button.draw(screen): #end game
				run = False
			if unpause_button.draw(screen): #resume game
				game_paused = False

		if pause_state == "statistics":
			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)
			draw_text("STATISTICS", font, text_colour, 130, 0, 2)
			draw_text("Points: "+str(points), font, text_colour, 300, 120, 0.9)
			draw_text("Seconds: "+str(round(seconds_irl)), font, text_colour, 300, 170, 0.9)
			draw_text("Minigames won: "+str(minigames_no), font, text_colour, 300, 220, 0.9)
			draw_text("Days survived: "+str(days), font, text_colour, 300, 270, 0.9)
			draw_text("Times paused: "+str(pauses_no), font, text_colour, 300, 320, 0.9)
			screen.blit(zombie_img, (70, 100))

			if back_button3.draw(screen):
				pause_state = "main"
# ------------------------------------------------ #

	elif minigame == True: #when random minigame event occurs

		if minigame_state == "main": #defaults to main #show popup and click to continue
			pygame.draw.rect(screen, outline, minigame_popup_outline)
			pygame.draw.rect(screen, (110,116,125), minigame_popup)

			if minigame_type == 0: #popup changes depending on minigame type
				draw_text("Fence" , font, text_colour, 430, 90, 1)
				draw_text("Oh no! The fence has been" , font, text_colour, 310, 160, 0.65)
				draw_text("broken. Drag the left ends" , font, text_colour, 310, 190, 0.65)
				draw_text("to meet the right to fix it." , font, text_colour, 310, 220, 0.65)
				draw_text("Easy" , font, (100, 255, 100), 440, 280, 1)
				fence_complete = False #variable for minigame

			elif minigame_type == 1:
				draw_text("Zombies" , font, text_colour, 410, 90, 1)
				draw_text("Oh no! There has been a" , font, text_colour, 310, 160, 0.65)
				draw_text("radiation leakage. The" , font, text_colour, 310, 190, 0.65)
				draw_text("employees have turned into" , font, text_colour, 310, 220, 0.65)
				draw_text("zombies! Drag them away" , font, text_colour, 310, 250, 0.65)
				draw_text("from the radiation!" , font, text_colour, 310, 280, 0.65)

				if no_zombies == 1: #sets difficulty of minigame depending on number of zombies
					draw_text("Easy", font, (100, 255, 100), 440, 340, 1)
				elif no_zombies == 2:
					draw_text("Average", font, (255, 209, 100), 435, 340, 1)
				if no_zombies == 3:
					draw_text("Hard", font, (255, 100, 100), 440, 340, 1)

				minigame_time = 30 
				all_dead = False
				all_dead1 = False
				all_dead2 = False
				all_dead3 = False

			elif minigame_type == 2:
				draw_text("Fire" , font, text_colour, 430, 90, 1)
				draw_text("Oh no! A fire has broken" , font, text_colour, 310, 160, 0.65)
				draw_text("out! Use the fire    " , font, text_colour, 310, 190, 0.65)
				draw_text("extinguisher to put it out!" , font, text_colour, 310, 220, 0.65)
				draw_text("Easy" , font, (100, 255, 100), 440, 280, 1)
				extinguished = False
				picked_up = False
				minigame_time = 20
				fire_rect1 = pygame.Rect(200, 100, 200, 259)
				fire_scale1 = 1
				fire_rect2 = pygame.Rect(450, 250, 200, 259)
				fire_scale2 = 1
				fire_rect3 = pygame.Rect(600, 80, 200, 259)
				fire_scale3 = 1

			if play_minigame_button.draw(screen): #sets minigame state to one matching minigame type
				minigame_state = minigame_states[minigame_type]


		if minigame_state == "fence":#0

			if not fence_complete:
				screen.blit(fence_bg_img, (0,0))

				#calls wire function for each wire
				fence_dragging[0], fence_connected[0] = wire(fence_start1 ,fence_end1, fence_dragging[0], fence_connected[0])
				fence_dragging[1], fence_connected[1] = wire(fence_start2 ,fence_end2, fence_dragging[1], fence_connected[1])
				fence_dragging[2], fence_connected[2] = wire(fence_start3 ,fence_end3, fence_dragging[2], fence_connected[2])
				fence_dragging[3], fence_connected[3] = wire(fence_start4 ,fence_end4, fence_dragging[3], fence_connected[3])
				fence_dragging[4], fence_connected[4] = wire(fence_start5 ,fence_end5, fence_dragging[4], fence_connected[4])

				#checks connected state of each wire
				if fence_connected[0] == True:
					pygame.draw.line(screen, fence_colour, fence_start1.center, fence_end1.center, 19)
				if fence_connected[1] == True:
					pygame.draw.line(screen, fence_colour, fence_start2.center, fence_end2.center, 19)
				if fence_connected[2] == True:
					pygame.draw.line(screen, fence_colour, fence_start3.center, fence_end3.center, 19)
				if fence_connected[3] == True:
					pygame.draw.line(screen, fence_colour, fence_start4.center, fence_end4.center, 19)
				if fence_connected[4] == True:
					pygame.draw.line(screen, fence_colour, fence_start5.center, fence_end5.center, 19)

				#checks connected state of all wires
				if all(fence_connected):
					fence_complete = True

			else: #when successful
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("You Won!" , font, text_colour, 410, 90, 1)
				draw_text("Congrats, you fixed the" , font, text_colour, 310, 160, 0.65)
				draw_text("fence (+50 points)     " , font, text_colour, 310, 200, 0.65)
				draw_text("Not that it was        " , font, text_colour, 310, 240, 0.65)
				draw_text("difficult or anything. " , font, text_colour, 310, 280, 0.65)

				if back_minigames_button.draw(screen):#resets variables and adds points
					minigame = False
					minigame_state = "main"
					fence_connected = [False, False, False, False, False]
					points += 50
					measure = boss_adjust(measure, 4)
					minigames_no += 1


		if minigame_state == "zombies":#1
			time_rect = pygame.Rect(200, 50, (minigame_time*20), 30) #timer at top of screen initialised

			if minigame_time > 0 and not all_dead: #if there is still time left and at least one zombie is alive
				screen.blit(radioactive_spill, (500, 300))
				pygame.draw.rect(screen, (255, 0, 0), time_rect)
				minigame_time -= 1/60 #decreases time

				if no_zombies == 1:
					all_dead, zombie_dragged[0] = zombie1.draw(screen, zombie_dragged[1], zombie_dragged[2])

				elif no_zombies == 2:
					all_dead1, zombie_dragged[0] = zombie1.draw(screen, zombie_dragged[1], zombie_dragged[2])
					all_dead2, zombie_dragged[1] = zombie2.draw(screen, zombie_dragged[0], zombie_dragged[2])
					if all_dead1 and all_dead2:
						all_dead = True

				elif no_zombies == 3:
					all_dead1, zombie_dragged[0] = zombie1.draw(screen, zombie_dragged[1], zombie_dragged[2])
					all_dead2, zombie_dragged[1] = zombie2.draw(screen, zombie_dragged[0], zombie_dragged[2])
					all_dead3, zombie_dragged[2] = zombie3.draw(screen, zombie_dragged[0], zombie_dragged[1])
					if all_dead1 and all_dead2 and all_dead3:
						all_dead = True

			elif all_dead: #if fail minigame
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("You lost." , font, text_colour, 410, 90, 1)
				draw_text("Great job, genius. They" , font, text_colour, 310, 160, 0.65)
				draw_text("all died (-100 points) " , font, text_colour, 310, 200, 0.65)
				draw_text("So much paperwork...   " , font, text_colour, 310, 240, 0.65)
				
				if back_minigames_button.draw(screen): #resets variables and objects, and subtracts points
					minigame = False
					minigame_state = "main"
					points -= 100
					measure = boss_adjust(measure, -(8*no_zombies))
					for x in range(0,no_zombies):
						(zombie_list[x]).reset()

			else: #if time runs out
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("You Won!" , font, text_colour, 410, 90, 1)
				draw_text("Congrats, you saved the " , font, text_colour, 310, 160, 0.65)
				draw_text("employees (+150 points) " , font, text_colour, 310, 200, 0.65)
				draw_text("Now they can go back to " , font, text_colour, 310, 240, 0.65)
				draw_text("work for 16 hours a day!" , font, text_colour, 310, 280, 0.65)

				if back_minigames_button.draw(screen):  #resets variables and objects, and adds points
					minigame = False
					minigame_state = "main"
					points += 150
					minigames_no += 1
					measure = boss_adjust(measure, 3*no_zombies)
					for x in range(0,no_zombies):
						(zombie_list[x]).reset()



		if minigame_state == "fire":#2
			time_rect = pygame.Rect(200, 550, (minigame_time*30), 30) #timer at top of screen initialised

			if minigame_time > 0 and not extinguished: #if there is still time left and at least one zombie is alive
				screen.blit(burnt_background, (0,0))
				pygame.draw.rect(screen, (255, 0, 0), time_rect)
				minigame_time -= 1/60 #decreases time

				if picked_up == False: #cannot do anything until extinguisher picked up
					if extinguisher_button.draw(screen):
						picked_up = True

					screen.blit(fire_img, fire_rect1.topleft)
					screen.blit(fire_img, fire_rect2.topleft)
					screen.blit(fire_img, fire_rect3.topleft)

				else: #extinguisher picked up
					posx, posy = pygame.mouse.get_pos() #mouse position
					rectE = pygame.Rect((posx - 200), (posy - 100), 100, 100) #area where extingisher foam covers
					fire_scale1, fire_rect1 = fire(fire_img, fire_scale1, fire_rect1, rectE)
					fire_scale2, fire_rect2 = fire(fire_img, fire_scale2, fire_rect2, rectE)
					fire_scale3, fire_rect3 = fire(fire_img, fire_scale3, fire_rect3, rectE)

					if pygame.mouse.get_pressed()[0] == 1: #when mouse is down				
						screen.blit(extinguisher_on_img, (posx - 200, posy - 100)) #extinguisher on image

					else:
						screen.blit(extinguisher_off_img, (posx - 200, posy - 100)) #extinguisher off image

					if fire_scale1 < 0.005 and fire_scale2 < 0.005 and fire_scale3 < 0.005: #makes fire extinguished when small
						extinguished = True

			elif extinguished: #if succeed minigame
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("You Won!" , font, text_colour, 410, 90, 1)
				draw_text("Wow! You saved the day!     " , font, text_colour, 310, 160, 0.65)
				draw_text("You put out the fires!      " , font, text_colour, 310, 200, 0.65)
				draw_text("(+100 points) only minor    " , font, text_colour, 310, 240, 0.65)
				draw_text("damage to the paint..." , font, text_colour, 310, 280, 0.65)
				
				if back_minigames_button.draw(screen): #resets variables and objects, and subtracts points
					minigame = False
					minigame_state = "main"
					points += 100
					minigames_no += 1
					measure = boss_adjust(measure, 5)

			else: #if time runs out (fail)
				pygame.draw.rect(screen, outline, minigame_popup_outline)
				pygame.draw.rect(screen, (110,116,125), minigame_popup)
				draw_text("You lost." , font, text_colour, 410, 90, 1)
				draw_text("Well, the building burned" , font, text_colour, 310, 160, 0.65)
				draw_text("down thanks to you.      " , font, text_colour, 310, 200, 0.65)
				draw_text("(-75 points) " , font, text_colour, 310, 240, 0.65)

				if back_minigames_button.draw(screen):  #resets variables and objects, and adds points
					minigame = False
					minigame_state = "main"
					points -= 75
					measure = boss_adjust(measure, -10)


# ------------------------------------------------ #
	
	else:#this is the actual game
		seconds_irl += 1/60 #increases seconds
		time_formatted, days, energy_demand = time_format(seconds_irl, days, energy_demand, demand_nums) #formats time and adjusts number of days

		if round(seconds_irl, 2) % 10 == 0:#increases points for staying alive every 10 seconds
			points += 5

		if round(seconds_irl, 2) % 50 == 0 or seconds_irl == 1/60: #randomises routine code every 50 seconds
			
			upper_left1 = arrows_text[random.randint(0,1)]
			upper_left2 = arrows_text[random.randint(0,1)]
			upper_left3 = arrows_text[random.randint(0,1)]
			upper_left4 = arrows_text[random.randint(0,1)]

			upper_right1 = colour_text[random.randint(0,1)]
			upper_right2 = colour_text[random.randint(0,1)]
			upper_right3 = colour_text[random.randint(0,1)]

			lower_left1 = grey_text[random.randint(0,1)]
			lower_left2 = grey_text[random.randint(0,1)]
			lower_left3 = grey_text[random.randint(0,1)]
			lower_left4 = grey_text[random.randint(0,1)]

			lower_right1 = triangle_text[random.randint(0,3)]
			lower_right2 = circle_text[random.randint(0,3)]
			lower_right3 = rect_text[random.randint(0,3)]
			lower_right4 = semi_text[random.randint(0,3)]

			bullet1 = "- " + upper_left1 + upper_left2 + upper_left3 + upper_left4
			bullet2 = "- " + upper_right1 + upper_right2 + upper_right3
			bullet3 = "- " + lower_left1 + lower_left2 + lower_left3 + lower_left4
			bullet4 = "- " + lower_right1 + " " + lower_right2 + " " + lower_right3 + " " + lower_right4

			#decides what popup to show
			if seconds_irl == 1/60:
				draw_first_routine_popup = True

			elif routine_check == True:
				draw_fail_routine_popup = True
				points -= 40
				measure = boss_adjust(measure, -12)

			else:
				draw_routine_popup = True
				points += 50
				measure = boss_adjust(measure, +6)

			routine_check = True

		# ------------------------------------------------ #

		#minigame start
		minigame_probability += 0.001
		if random.randint(0,15000) < round(minigame_probability):
			
			minigame_type = random.randint(0,2) #chooses out of the minigame options

			if minigame_type == 1: #only if the zombie minigame is chosed
				no_zombies = random.randint(1,3) #randomly decides the number of zombies

			minigame_probability = 1 #resets minigame probability
			minigame = True
			
		# ------------------------------------------------ #
		#point deductions of any game state
		if seconds_irl > 21: #grace period
			if energy_output > (energy_demand+100) or energy_output < (energy_demand-100): #if outside of 100 of demand
				measure = boss_adjust(measure, -0.08)
				if round(seconds_irl, 2) % 10 == 0:
					points -= 5

			elif energy_output > (energy_demand+30) or energy_output < (energy_demand-30): #if outside of 30 of demand
				measure = boss_adjust(measure, -0.02)
				if round(seconds_irl, 2) % 10 == 0:
					points -= 15

			else: #slow increase if doing well
				measure = boss_adjust(measure, 0.005)
				if round(seconds_irl, 2) % 10 == 0:
					points += 10

		# ------------------------------------------------ #

		if game_state == "control panels": #draws panel buttons, info panel, pause button
			screen.fill((52, 78, 91))
			
			#check if panels are pressed
			if left_panel_button.draw(screen):
				game_state = "left panel"
			if right_panel_button.draw(screen):
				game_state = "right panel"
			if centre_panel_button.draw(screen):
				game_state = "centre panel"
			if pause_button.draw(screen):
				game_paused = True
				pauses_no += 1

			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)
			game_end = boss_bar(measure, game_end, boss_rect)

		# ------------------------------------------------ #

		if game_state == "left panel": #when left panel pressed
			screen.fill((52, 78, 91))
			screen.blit(map_console_closeup_img, (0,0))
			screen.blit(map_none, (25 ,145))
			
			if right_arrow.draw(screen): #buttons
				game_state = "centre panel"
			if pause_button.draw(screen):
				game_paused = True
				pauses_no += 1
			if back_scenes_button.draw(screen):
				game_state = "control panels"

			#for each: if mouse hovering over section, show map image where that section is highlighted
			if entrance.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_entrance, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1: #for each: if mouse pressed and hover, draw info box
					screen.blit(info_entrance, (200, 300))

			if building.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_building, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1:
					screen.blit(info_building, (250, 300))

			if wires.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_wires, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1:
					screen.blit(info_wires, (200, 200))

			if containment.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_containment, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1:
					screen.blit(info_containment, (180, 150))

			if building2.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_building2, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1:
					screen.blit(info_building2, (270, 150))

			if tower.collidepoint(pygame.mouse.get_pos()):
				screen.blit(map_tower, (25, 145))
				if pygame.mouse.get_pressed()[0] == 1:
					screen.blit(info_tower, (400, 150))

			game_end = boss_bar(measure, game_end, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)

		# ------------------------------------------------ #

		if game_state == "right panel": #when right panel pressed
			screen.fill((52, 78, 91))
			screen.blit(routine_console_closeup_img, (0,0))
			#rectangles for background
			pygame.draw.rect(screen, outline, shapes_outer)
			pygame.draw.rect(screen, (110,116,125), upper_right)
			pygame.draw.rect(screen, (110,116,125), upper_left)
			pygame.draw.rect(screen, (110,116,125), lower_right)
			pygame.draw.rect(screen, (110,116,125), lower_left)

			if left_arrow.draw(screen):
				game_state = "centre panel"
			if pause_button.draw(screen):
				game_paused = True
				pauses_no += 1
			if back_scenes_button.draw(screen):
				game_state = "control panels"
			if clipboard_button.draw(screen):
				game_state = "clipboard"

			# grey rectangle buttons in lower left quadrant
			if routine1.draw(screen):
				routine1 = changing_buttons(routine_unpressed_button1, routine_pressed_button1, routine1)
			if routine2.draw(screen):
				routine2 = changing_buttons(routine_unpressed_button2, routine_pressed_button2, routine2)
			if routine3.draw(screen):
				routine3 = changing_buttons(routine_unpressed_button3, routine_pressed_button3, routine3)
			if routine4.draw(screen):
				routine4 = changing_buttons(routine_unpressed_button4, routine_pressed_button4, routine4)

			# grey switches in upper left quadrant
			if r_switch1.draw(screen):
				r_switch1 = changing_buttons(routine_down_button1, routine_up_button1, r_switch1)
			if r_switch2.draw(screen):
				r_switch2 = changing_buttons(routine_down_button2, routine_up_button2, r_switch2)
			if r_switch3.draw(screen):
				r_switch3 = changing_buttons(routine_down_button3, routine_up_button3, r_switch3)
			if r_switch4.draw(screen):
				r_switch4 = changing_buttons(routine_down_button4, routine_up_button4, r_switch4)

			# red and green buttons in upper right quadrant
			if r_colour_button1.draw(screen):
				r_colour_button1 = changing_buttons(routine_green_button1, routine_red_button1, r_colour_button1)
			if r_colour_button2.draw(screen):
				r_colour_button2 = changing_buttons(routine_green_button2, routine_red_button2, r_colour_button2)
			if r_colour_button3.draw(screen):
				r_colour_button3 = changing_buttons(routine_green_button3, routine_red_button3, r_colour_button3)	

			# coloured shape buttons in lower right quadrant
			if r_circle.draw(screen):
				r_circle = colour_change(red_circle_button, green_circle_button, blue_circle_button, yellow_circle_button, r_circle)
			if r_tri.draw(screen):
				r_tri = colour_change(red_tri_button, green_tri_button, blue_tri_button, yellow_tri_button, r_tri)
			if r_rectangle.draw(screen):
				r_rectangle = colour_change(red_rect_button, green_rect_button, blue_rect_button, yellow_rect_button, r_rectangle)
			if r_semi.draw(screen):
				r_semi = colour_change(red_semi_button, green_semi_button, blue_semi_button, yellow_semi_button, r_semi)

			game_end = boss_bar(measure, game_end, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)

			#checks states of all routine buttons
			check1 = routine_checker(upper_left1, r_switch1, arrows_text, routine_down_button1, routine_up_button1)
			check2 = routine_checker(upper_left2, r_switch2, arrows_text, routine_down_button2, routine_up_button2)
			check3 = routine_checker(upper_left3, r_switch3, arrows_text, routine_down_button3, routine_up_button3)
			check4 = routine_checker(upper_left4, r_switch4, arrows_text, routine_down_button4, routine_up_button4)

			check5 = routine_checker(upper_right1, r_colour_button1, colour_text, routine_green_button1, routine_red_button1)
			check6 = routine_checker(upper_right2, r_colour_button2, colour_text, routine_green_button2, routine_red_button2)
			check7 = routine_checker(upper_right3, r_colour_button3, colour_text, routine_green_button3, routine_red_button3)

			check8 = routine_checker(lower_left1, routine1, grey_text, routine_pressed_button1, routine_unpressed_button1)
			check9 = routine_checker(lower_left2, routine2, grey_text, routine_pressed_button2, routine_unpressed_button2)
			check10 = routine_checker(lower_left3, routine3, grey_text, routine_pressed_button3, routine_unpressed_button3)
			check11 = routine_checker(lower_left4, routine4, grey_text, routine_pressed_button4, routine_unpressed_button4)

			check12 = routine_checker_shapes(lower_right1, r_tri, triangle_text, red_tri_button, green_tri_button, blue_tri_button, yellow_tri_button)
			check13 = routine_checker_shapes(lower_right2, r_circle, circle_text, red_circle_button, green_circle_button, blue_circle_button, yellow_circle_button)
			check14 = routine_checker_shapes(lower_right3, r_rectangle, rect_text, red_rect_button, green_rect_button, blue_rect_button, yellow_rect_button)
			check15 = routine_checker_shapes(lower_right4, r_semi, semi_text, red_semi_button, green_semi_button, blue_semi_button, yellow_semi_button)

			if check1 and check2 and check3 and check4 and check5 and check6 and check7 and check8 and check9 and check10 and check11 and check12 and check13 and check14 and check15:
				routine_check = False

		# ------------------------------------------------ #

		if game_state == "clipboard": #when clipboard is opened
			screen.fill((52, 78, 91))
			screen.blit(routine_console_closeup_img, (0,0))
			screen.blit(clipboard_screen_img, (0,0))

			if back_scenes_button.draw(screen):
				game_state = "right panel"
			if pause_button.draw(screen):
				game_paused = True
				pauses_no += 1

			if routine_check == True: #draws routine codes
				draw_text(bullet1, font, outline, 350, 175, 1)
				draw_text(bullet2, font, outline, 340, 250, 1)
				draw_text(bullet3, font, outline, 330, 325, 1)
				draw_text(bullet4, font, outline, 320, 400, 1)

			else: #when routine check is already completed
				draw_text("No routine check", font, outline, 300, 250, 0.9)
				draw_text("currently. Good job", font, outline, 290, 290, 0.9)

			game_end = boss_bar(measure, game_end, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)

		# ------------------------------------------------ #

		if game_state == "centre panel": #when centre panel pressed
			screen.fill((52, 78, 91))
			screen.blit(reactor_console_closeup_img, (0,20))
			pygame.draw.rect(screen, outline, left_slider_scale)
			pygame.draw.rect(screen, outline, right_slider_scale)
			
			if power_button.draw(screen): #changes value of variable and state of button
				if coolant_pumps == False:
					coolant_pumps = True
					power_button = power_button_on #green if coolant pumps true
				elif coolant_pumps == True:
					coolant_pumps = False
					power_button = power_button_off #grey if coolant pumps false

			if left_arrow.draw(screen):
				game_state = "left panel"
			if right_arrow.draw(screen):
				game_state = "right panel"
			if back_scenes_button.draw(screen):
				game_state = "control panels"
			if pause_button.draw(screen):
				game_paused = True
				pauses_no += 1

			control_rod_pos = round(-(700/213)*(grip1.y) + (152800/71)) #function to map y values to values between 1-100
			energy_output = round(-(700/213)*(grip2.y) + (152800/71)) #function to map y values to values between 1-100

			if coolant_pumps:
				mouse_x, mouse_y = pygame.mouse.get_pos()#mouse position
				if mouse_y > 160 and mouse_y < 415:
					if grip1.collidepoint(mouse_x, grip1.y): #if hovering and in correct Y range
						slider_movement(grip1) #call slider movement procedure
					if control_rod:
						if grip2.collidepoint(mouse_x, grip2.y):
							slider_movement(grip2)

			if control_rod_pos > (energy_demand-30) and control_rod_pos < (energy_demand+30): #if within 30 of demand
				pygame.draw.circle(screen, (0, 255, 0), (405, 430), 8) #draw green circle
				control_rod = True #allows 2nd slider
			elif control_rod_pos > (energy_demand-100) and control_rod_pos < (energy_demand+100): #if within 100 of demand
				pygame.draw.circle(screen, (255, 255, 0), (405, 430), 8) #draw yellow circle
				control_rod = False #disallow 2nd slider
			else:
				pygame.draw.circle(screen, (255, 0, 0), (405, 430), 8) #draw red circle
				control_rod = False

			if energy_output > (energy_demand-30) and energy_output < (energy_demand+30): ##if within 30 of demand
				pygame.draw.circle(screen, (0, 255, 0), (545, 430), 8) #draw green circle
			elif energy_output > (energy_demand-100) and energy_output < (energy_demand+100): #if within 100 of demand
				pygame.draw.circle(screen, (255, 255, 0), (545, 430), 8) #draw yellow circle
			else:
				pygame.draw.circle(screen, (255, 0, 0), (545, 430), 8) #draw red circle


			screen.blit(sliderg_img, (grip1.x, grip1.y)) #draws sliders on screen
			screen.blit(sliderg_img, (grip2.x, grip2.y))

			draw_text(str(energy_output) , font, text_colour, 520, 445, 0.7)
	
			draw_text("Coolant pumps" , font, text_colour, 160, 190, 0.6)
			draw_text("Control rods" , font, text_colour, 330, 130, 0.5)
			draw_text("Steam output" , font, text_colour, 490, 130, 0.5)
			game_end = boss_bar(measure, game_end, boss_rect)
			draw_panel(panel_rect, panel_outline_rect, seconds_irl, time_formatted, points, energy_demand, energy_output, text_colour)

		# ------------------------------------------------ #

		if draw_routine_popup == True: #draws unique popup after successful routine check
			pygame.draw.rect(screen, outline, minigame_popup_outline)
			pygame.draw.rect(screen, (110,116,125), minigame_popup)
			draw_text("Routine" , font, text_colour, 410, 90, 1)
			draw_text("You successfully completed" , font, text_colour, 310, 160, 0.65)
			draw_text("the last check (+50 points)" , font, text_colour, 310, 200, 0.65)
			draw_text("There is a routine check" , font, text_colour, 310, 340, 0.65)
			draw_text("to be completed" , font, text_colour, 310, 380, 0.65)

		elif draw_first_routine_popup == True: #draws unique popup for first routine check
			pygame.draw.rect(screen, outline, minigame_popup_outline)
			pygame.draw.rect(screen, (110,116,125), minigame_popup)
			draw_text("Welcome!" , font, text_colour, 410, 90, 1)
			draw_text("It's your first day working" , font, text_colour, 310, 160, 0.65)
			draw_text("at the power plant. First, " , font, text_colour, 310, 200, 0.65)
			draw_text("start producing energy,    " , font, text_colour, 310, 240, 0.65)
			draw_text("then do the routine check. " , font, text_colour, 310, 280, 0.65)

		elif draw_fail_routine_popup == True: #draws unique popup after unsuccessful routine check
			pygame.draw.rect(screen, outline, minigame_popup_outline)
			pygame.draw.rect(screen, (110,116,125), minigame_popup)
			draw_text("Routine" , font, text_colour, 410, 90, 1)
			draw_text("You have failed the last" , font, text_colour, 310, 160, 0.65)
			draw_text("check (-40 points)" , font, text_colour, 310, 200, 0.65)
			draw_text("There is a routine check" , font, text_colour, 310, 340, 0.65)
			draw_text("to be completed" , font, text_colour, 310, 380, 0.65)

		if round(seconds_irl, 2) % 50 == 3:#makes popup disappear after 3 seconds
			draw_routine_popup = False #resets variables to do this
			draw_fail_routine_popup = False
			draw_first_routine_popup = False

# ------------------------------------------------ #

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()

pygame.quit()