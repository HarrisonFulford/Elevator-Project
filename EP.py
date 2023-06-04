#DAY 1 PROGRESS: Today I got the basic code down, the mainloop is started and I did some research on the algorithim which is shown in the project note
#DAY 2 PROGRESS: No noteable work because I was presenting Monkopoly, just started flowchart
#DAY 3 PROGRESS: Made flowchart of the whole project
#DAY 4 PROGRESS: Made a rectangle that moves up and down based off key presses
#DAY 5 PROGRESS: Made a class for all the buttons and a for loop in the mainloopd that defines all twelve buttons (including the up/down arrows for all floors except for floor 12 and 1)
#DAY 6 PROGRESS: Displayed all buttons and defined the text of each button
#DAY 7 PROGRESS: Changed colour of buttons and made the elevator move on a floor to floor basis, begining code on calling the elevator with the logic and implementing the floor choosing feature
#DAY 8 PROGRESS: Added button based movement and floor choice logic
#DAY 9 PROGRESS: Coded logic from flow chart, added a class for the up and down buttons to make them work, commented the code, added the log file 


#Importing all used modules
import pygame
import random
import sys
import math
from datetime import datetime

#creating a class for all the floor buttons (I call them buttons but they end up being used as placeholders
class Button:
    #initializing all the importent attributes, ie. the x and y coordinates for all types of buttons, and a definition of it's shape as a rectangle
    def __init__(self, button_num, buttonx, buttony, upx, downx):
        self.button_num = button_num
        self.buttonx = buttonx
        self.buttony = buttony
        self.upx = upx
        self.downx = downx
        self.button_rect = pygame.Rect(self.buttonx, self.buttony, 30, 50)
    #creating a function for displaying the text related to the floor buttons
    def addText(self, screen):
        # sett he font and text
        font = pygame.font.Font(None, 25)
        text_surface = font.render(str(self.button_num), True, (0, 0, 0))
        #location
        text_rect = text_surface.get_rect(center=(self.buttonx + 15, self.buttony + 25))
        #display the text onto the buttons 
        display.blit(text_surface, text_rect)

#creating a class for the elevator 
class Elevator:
    #initializing the elevator for all it's most important attributes ie. it's dimensions and it's coordinates
    def __init__(self, floor_height):
        self.floor_height = floor_height
        self.current_floor = 1
        self.elevator_width = 25
        self.elevator_height = 50
        self.elevator_x = 300
        self.elevator_y = 60 + (self.current_floor - 1) * self.floor_height
        self.destination = None

    # defining a function for moving the elevator up
    def move_up(self): 
        if self.current_floor < 12:
            self.current_floor += 1
            self.elevator_y = 60 + (self.current_floor - 1) * self.floor_height

    #defining a function for moving the elevator down
    def move_down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            self.elevator_y = 60 + (self.current_floor - 1) * self.floor_height

    #defining a function that sets what floors the elevator wants to move to immidiately, which will later be used to affect the highest and lowest drop lists
    def move_to_floor(self, floor):
        if floor > self.current_floor:
            self.destination = floor
            self.move_up()
        elif floor < self.current_floor:
            self.destination = floor
            self.move_down()

    #function that choses a random floor, never ended up being used because this only applies to the down buttons so I added it to the down button class and used it from that instead of this one
    def choose_random_floor(self, direction):
        if direction == "up":
            self.destination = random.randint(self.current_floor + 1, 12)
        elif direction == "down":
            self.destination = random.randint(1, self.current_floor - 1)

    #Defining a funcition to draw the elevator
    def draw_elevator(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.elevator_x, self.elevator_y, self.elevator_width, self.elevator_height))

#defining a function to update the state of the doors on the elevator, the function has no variable dependancies because they already exist within the logic 
def Door_Update():
        pygame.draw.rect(display, (0, 255, 100, 255), pygame.Rect(openX, Current_E_POS, Gap_Width, 50))
        pygame.display.update()

#initializing basic stuff for pygame, ie. initiazing the module
pygame.init()
#setting the screen size
screen = (1000, 800)
#turning the state of the screen into a pygame display so you can put stuff on it, this automaticly reads the size of the screen from the last line
display = pygame.display.set_mode(screen)
#setting a variable for the clock
clock = pygame.time.Clock()
#setting the font outside of the previous class definition so I can use it throughout the project
font = pygame.font.SysFont(None, 25)

#creating text file for logs
with open ('LogFile.txt', 'w') as f:
    f.write("Harrison's Elevator Log" + '\n')

#running a for loop to add all the floor buttons to a list such that their location and displayable number are dependant on each button
buttons = []
for button_num in range(1, 13):
        #the math behind the y value 
        #simply behind the idea that you do 13 
        #(or in this case the y value of 13 as a multiple of 60 because that's how I want to space the buttons) 
        #minus the actual value of the button so you get the value of the buttons opposit in regards to 1 through 12. 
        #ie. button 12 is at the top of the screen 
        #(normally where button 1 inherently is because of x and y coordinates in pygame)
        buttons.append(Button(button_num, 180, 780-(button_num)*60, 440, 480))

#Up button definitions start here:
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#creating list for the current and future floors I can travel up to
C_U_Floor = []
D_U_Floor = []

#creating a class for all the up buttons
class U_Button:
    #re initializing the the current and future lists within the class so they can be used (honestly not sure if I even need these but I don't care)
    UpList = []
    C_U_Floor = []
    D_U_Floor = []
    # creating a dictionary for all the coordinates that I stop at when I travel up for the text log
    Up_Cords = {}
   
    #defining variable initializations
    def __init__(self, floor):
        #the current floor
        self.floor = floor
        #the dimenstions and coordinates
        self.x = 140
        self.y = floor * 60
        self.rect = pygame.Rect(self.x, self.y, 30, 50)      
        self.floor = (13) - self.floor
   
    #defining a function that is called when the elevator moves up
    def up(self):
        #adding the current floor the current floor list
        U_Button.C_U_Floor.append(self.floor)
        #adding a random floor to the future floor list
        U_Button.D_U_Floor.append(random.randint(self.floor + 1, 12))
        #Hsetting the value of 
        U_Button.UpList = U_Button.C_U_Floor + U_Button.D_U_Floor; U_Button.UpList = list(set(U_Button.UpList)); U_Button.UpList.sort(); U_Button.Up_Cords = dict(zip(U_Button.C_U_Floor, U_Button.D_U_Floor))

        
        with open ('LogFile.txt', 'w') as f:
            f.write(currentTime+'/'+str(self.floor)+'/'+'up request made'+''+'\n')
            
#defining a funcition to draw the up arrows
def up_arrow(x,y,colour):
    pygame.draw.polygon(display, (colour), [(x + 150, y + 150), (x + 50, y + 350), (x + 250, y + 350)])

#defining a function to create all the up arrows
def U_Button_Create():
       if button.floor != 12:


           if button.floor in U_Button.C_U_Floor:
               col = 255, 0, 0
           else:
               col = 0, 255, 100            


           pygame.draw.rect(display, (col), button.rect)
           display.blit(font.render('', False, (0, 0, 0)), (button.x + 17, button.y))
           # Draw up arrow
           pygame.draw.polygon(display, (0, 0, 0), [(button.x + 15, button.y + 15), (button.x + 5, button.y + 35), (button.x + 25, button.y + 35)])

#defining a function to add all previous up moves to the up list so they can be put onto the text log
def U_List_Edit():
        U_Button.UpList = U_Button.C_U_Floor + U_Button.D_U_Floor
        U_Button.UpList = list(set(U_Button.UpList))
        U_Button.UpList.sort()

#up button definition ends here: 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#All of the following code is the same as the up button definitions, just for the down buttons, so they have slightly different variable names:
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C_D_Floor = []
D_D_Floor = []

class D_Button:
   
    DownList = []
    C_D_Floor = []
    D_D_Floor = []
    Down_Cords = {}
   
    def __init__(self, floor):
        self.floor = floor
        self.x = 100
        self.y = floor * 60
        self.rect = pygame.Rect(self.x, self.y, 30, 50)


        self.floor = (13) - self.floor
   
    def down(self):
        D_Button.C_D_Floor.append(self.floor)
       
        if self.floor != 2: weightedRandList = [1] * 9 + [random.randint(2, self.floor - 1)] * 1
        elif self.floor == 2: weightedRandList = [1] * 10
        
        D_Button.D_D_Floor.append(weightedRandList[random.randint(0, len(weightedRandList) - 1)]); D_Button.DownList = D_Button.C_D_Floor + D_Button.D_D_Floor; D_Button.DownList = list(set(D_Button.DownList)); D_Button.DownList.sort(reverse = True); D_Button.Down_Cords = dict(zip(D_Button.C_D_Floor, D_Button.D_D_Floor))
        
        weightedRandList = []
        
        with open ('LogFile.txt', 'w') as f:
            f.write(currentTime+'/'+str(self.floor)+'/'+'down request made'+''+'\n')
        
def down_arrow(x,y,colour):
    pygame.draw.polygon(display, (colour), [(x + 150, y + 350), (x + 50, y + 150), (x + 250, y + 150)])

def D_Button_Create():
        if button.floor != 1:

            if button.floor in D_Button.C_D_Floor:
                col = 255, 0, 0
            else:
                col = 0, 255, 100


            pygame.draw.rect(display, (col), button.rect)
            display.blit(font.render('', False, (0, 0, 0)), (button.x + 17, button.y))
            # Draw down arrow
            pygame.draw.polygon(display, (0, 0, 0), [(button.x + 15, button.y + 35), (button.x + 5, button.y + 15), (button.x + 25, button.y + 15)])

def D_List_Edit():
            D_Button.DownList = D_Button.C_D_Floor + D_Button.D_D_Floor
            D_Button.DownList = list(set(D_Button.DownList))
            D_Button.DownList.sort(reverse = True)

#down button definition ends here:
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#creating a list to set the button values for the newly defined up and down buttons, all twelve of each
U_ButtonList = [U_Button(1),U_Button(2), U_Button(3), U_Button(4),U_Button(5), U_Button(6),U_Button(7), U_Button(8), U_Button(9),U_Button(10),U_Button(11),U_Button(12)]
D_ButtonList = [D_Button(1),D_Button(2),D_Button(3), D_Button(4),D_Button(5),D_Button(6), D_Button(7),D_Button(8),D_Button(9), D_Button(10),D_Button(11), D_Button(12)]

#setting values to define the previously initiated elevator attributes
#x position
Elevetor_x = 180
#current y position
Current_E_POS = 720
#future y position
Future_E_POS = 720
#mode, (idle, up or down)
MODE = 'I'
#the current floor number
CurrentFloor = 1
#the future floor number
Future_Floor = 1
#the goal y position (furthest possible y to travel to)
Y_Cord_End = 720

Hold_Button = pygame.Rect(220, 180, 70, 50)
Highest_Drop = []; Lowest_Drop = []; PREV_POS = 0; PREV_MODE = ''; Drop_Check = False; Middle_x = 15.5; Gap_Width = 0; Opening_Check = True; Open_Timer = 0; Door_State_Open = False; Door_State_Closed = False; Move_Log = 0; Hold_Check = False; Idle_Timer = 0

#setting 12 nested lists for the x and y locations of each floor on the keypad
KEYPAD_LOC = [[220, 420], [260, 420],[220, 480], [260, 480],[220, 540], [260, 540],[220, 600], [260, 600],[220, 660], [260, 660],[220, 720], [260, 720],]

#defining a function to draw and change the current floor display
def floor_Counter():
    pygame.draw.rect(display, (0,255,100), pygame.Rect(220, 60, 70, 50))
    if round(Floor_Get(Current_E_POS)) >= 10: displayNum = str(round(Floor_Get(Current_E_POS)))
    else: displayNum = ' ' + str(round(Floor_Get(Current_E_POS)))                                              
    display.blit(font.render(displayNum, False, (255, 0, 0)), (220, 60))

#making a function to get the y coordinates of the goal floor
def Goal_Floor_Cords(floor):
    floor = 13 - floor
    yCord = floor * 60
    return yCord

#making a function to get the y value from any given floor
def Floor_Get(y):
    floor = y/60
    floor = 13 - floor
    return floor
       






#starting the mainloop
while True:
    #filling the screen before every mainloop so the new shapes can be drawn
    display.fill('black')
    #starting the for loop to sort through all the types of events in pygame we use in this project
    for event in pygame.event.get():
        #quit the game if the window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       #drawing all the up buttons and checking for up button mouse click
        for button in U_ButtonList:
            #is the up button is clicked on
            if event.type == pygame.MOUSEBUTTONUP and button.rect.collidepoint(pygame.mouse.get_pos()):
               #draws it
                button.up()
               
                #if the elevator mode is still idle (hasn't moved up last game loop)
                if MODE == 'I':
                    #set the hgihest possible floor to the calculated drop off floor
                    #this will change the mode later in the game loop
                    Y_Cord_End = Goal_Floor_Cords(U_Button.C_U_Floor[0])

       #literally the same as the up button list itteration just with all the down button variables
        for button in D_ButtonList:
            if event.type == pygame.MOUSEBUTTONUP and button.rect.collidepoint(pygame.mouse.get_pos()):
               
                button.down()


                if MODE == 'I':
                    Y_Cord_End = Goal_Floor_Cords(D_Button.C_D_Floor[0])

        #if the mouse is on the hold button it prevents the elevator from closing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if Hold_Button.collidepoint(event.pos):
                    #this variable determines the elevators ability to open or close
                    Hold_Check = True

        #if the mouse isn't on the hold button the elevator will be allowed to close
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if Hold_Button.collidepoint(event.pos):
                    #this variable determines the elevators ability to open or close
                    Hold_Check = False

    #setting the current time to be measured in seconds for the text log
    currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #itteratig through the button class and printing the up and down buttons
    #floor buttons
    for button in buttons: 
        pygame.draw.rect(display, (0, 255, 100), button.button_rect) 
        button.addText(screen)
    #up buttons
    for button in U_ButtonList:
        U_Button_Create()
    #down buttons
    for button in D_ButtonList:
        D_Button_Create()
        
    #sort through the list of keypad coordinates and check if the elevator will go down or not, if it is going down the floors specified on any given drop list will turn red
    for i, coord in enumerate(KEYPAD_LOC):
        #setting the colour to red or green
        if 12-i in Highest_Drop or 12-i in Lowest_Drop:
            col = 255, 0, 0
        else:
            col = 0, 255, 100
        
        #drawing the keypad with the specified colours dependant 
        pygame.draw.rect(display, (col), pygame.Rect(coord[0], coord[1], 30, 50))
        display.blit(font.render(str(12 - i), False, (0, 0, 0)), (coord[0], coord[1],))  
    
    #drawing and updating the floor counter by calling the function
    floor_Counter()

    #drawing the up arrow for the elevator moving up
    if MODE == 'U': up_arrow(558, 400, (0,255,100))
    #drawing the down arrow for the elevator if the elevator is moving down
    elif MODE == 'D': down_arrow(558, 400, (255, 0, 0))


    #Drawing and displaying the text for the hold button
    pygame.draw.rect(display, (0,255,100), Hold_Button)
    display.blit(font.render('hold', False, (0, 0, 0)), (220, 180))

    #if there is no drop offs the elevator moves with no door state changes, otherwise it logs the move, still not door state changes
    if Drop_Check == False:
        if Current_E_POS < Y_Cord_End:
            Move_Log += 1


            if Move_Log == 12:
                Current_E_POS += 5
                Move_Log = 0


        elif Current_E_POS > Y_Cord_End:
            Move_Log += 1


            if Move_Log == 12:
                Current_E_POS -= 5
                Move_Log = 0

    #displaying the elevator
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(Elevetor_x, Current_E_POS, 30, 50))

    #if the elevator does have to make a drop off it will change the door state and log the move
    if Drop_Check == True:
        #this is the door opening
        if Opening_Check == True:
            openX = Elevetor_x + Middle_x
            Door_Update()
            with open ('LogFile.txt', 'w') as f:
                f.write(currentTime+'/'+str(CurrentFloor)+'/'+'door open'+''+'\n')
            #math
            Middle_x -= 1/8
            Gap_Width += 1/4
            if Gap_Width >= 30:
                Opening_Check = False
                Door_State_Open = True
         
        #this is the state of the door being open
        if Door_State_Open == True:
            Open_Timer += 1
            Door_Update()
            if Open_Timer >= 120 and Hold_Check == False:
                Door_State_Open = False
                Door_State_Closed = True
                Open_Timer = 0
       
        #this is the door closing
        if Door_State_Closed == True:
            openX = Elevetor_x + Middle_x
            Door_Update() 
            with open ('LogFile.txt', 'w') as f:
                f.write(currentTime+'/'+str(CurrentFloor)+'/'+'door close'+''+'\n')
            #math
            Middle_x += 1/8
            Gap_Width -= 1/4
            if Gap_Width <= 0:
                Door_State_Closed = False
                Drop_Check = False
                Opening_Check = True


    #changing the mode of the elevator based off the difference between the current elevator position and the goal position of the elevator 
    if Current_E_POS < Y_Cord_End:
        MODE = 'D'
    elif Current_E_POS > Y_Cord_End:
        MODE = 'U'

    #if the elevator is in the idle mode it will compare the goal location to the current location and change the mode accordingly 
    if MODE == 'I':
        if PREV_MODE == 'U' and D_Button.C_D_Floor != []:
            Y_Cord_End = Goal_Floor_Cords(sorted(D_Button.C_D_Floor)[-1])
        elif PREV_MODE == 'D' and U_Button.C_U_Floor != []:
            Y_Cord_End = Goal_Floor_Cords(sorted(U_Button.C_U_Floor)[0])

    #if the mode of the elevator if up or idle it will turn the y value of the floor into a floor number and set that to the current floor
    if MODE == 'U' or MODE == 'I': CurrentFloor = int(Floor_Get(Current_E_POS))
    #if the mode of the elevator is down it will round the y value of the current floor to determine the current floor value form 1 -12
    elif MODE == 'D': CurrentFloor = math.ceil(Floor_Get(Current_E_POS))

    #if the mode is up or idle it removes the current floor from the list of floors above the elevator and edits the up list accordingly so it doesn't mess with the log file
    if MODE == 'U' or MODE == 'I':
        #if the goal floor is not in the up button and is bigger than the biggest one list it it updates the goal floor 
        if U_Button.UpList != []:
            if U_Button.UpList[-1] > CurrentFloor:
                Y_Cord_End = Goal_Floor_Cords(U_Button.UpList[-1])
        #if the current floor is in the current floor list for the up button function 
        if CurrentFloor in U_Button.C_U_Floor:
            Highest_Drop.append(U_Button.Up_Cords[CurrentFloor])
            U_Button.C_U_Floor = [f for f in U_Button.C_U_Floor if f != CurrentFloor]
            U_List_Edit()
            pygame.display.update()      
            Drop_Check = True


        #if the current floor is the highest point the elevator will reach:
        if CurrentFloor in Highest_Drop:
            #itterating through the cordinate list and setting a variable to remove the highest floor from the highest drop list
            U_Button.Up_Cords = {k: v for k, v in U_Button.Up_Cords.items() if v != CurrentFloor or k in U_Button.C_U_Floor}
            U_Button.D_U_Floor.remove(CurrentFloor) 
            Highest_Drop = [f for f in Highest_Drop if f != CurrentFloor]

            U_List_Edit()
            
            pygame.display.update()
           
            Drop_Check = True

    #if the mode is up or idles and both lists are empty the y cordinates of the goal is set to 0, this is for the idle function
    if (MODE == 'U' or MODE == 'I') and U_Button.UpList == [] and D_Button.DownList != []:
        Y_Cord_End = Goal_Floor_Cords(D_Button.DownList[0])

    #if the mode is idle and there is nothing in the the lowest drop list and the current down floor list is empty it will set the the y cordinates of the goal to be 0
    if MODE == 'I' and Lowest_Drop != [] and D_Button.C_D_Floor == []:
        Y_Cord_End = Goal_Floor_Cords(sorted(Lowest_Drop)[0])

    #if the mode is down or idle:
    if MODE == 'D' or MODE == 'I':

        #if the list of down movements is not empty and the next down movement is less than the current floor the y coordinate of the goal becomes the next floor in the down movement list
        if D_Button.DownList != []:
            if D_Button.DownList[-1] < CurrentFloor:
                Y_Cord_End = Goal_Floor_Cords(D_Button.DownList[-1])

        #if the current floor is a part of the current down floor movement it will add the current floor to the lowest drop list and ensure it is not the lowest point the elevator must reach
        if CurrentFloor in D_Button.C_D_Floor:
            Lowest_Drop.append(D_Button.Down_Cords[CurrentFloor])
            D_Button.C_D_Floor = [f for f in D_Button.C_D_Floor if f != CurrentFloor]
            D_List_Edit()
            pygame.display.update()
            Drop_Check = True
        
        #if the current floor is the lowest point the elevator must reach then the elevator switches the order of the down lists so the elevator can switch modes on the next iteration of the loop
        if CurrentFloor in Lowest_Drop:
            D_Button.Down_Cords = {k: v for k, v in D_Button.Down_Cords.items() if v != CurrentFloor or k in D_Button.C_D_Floor}
            D_Button.D_D_Floor = [f for f in D_Button.D_D_Floor if f != CurrentFloor]
            Lowest_Drop = [f for f in Lowest_Drop if f != CurrentFloor]
            D_List_Edit()
            pygame.display.update()
            Drop_Check = True

    #if the mode is in idle it adds one to the idle timer
    if MODE == 'I':
        Idle_Timer += 1
    #otherwise it set's the idle timer to 0
    elif MODE != 'I':
        Idle_Timer = 0
    
    #if the idle timer reaches a value representing a 20 second wait based off the frame rate it will move the elevator to floor one
    if Idle_Timer == 600:
        Y_Cord_End = Goal_Floor_Cords(1)
        Idle_Timer = 0
    if Current_E_POS == Y_Cord_End:
        if MODE != 'I': PREV_MODE = MODE
        MODE = 'I'


    pygame.display.update()
    
    #frame rate
    clock.tick(30)
    
    