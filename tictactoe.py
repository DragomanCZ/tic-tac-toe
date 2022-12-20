import pygame
import sys

pygame.init()
pygame.font.init()

# Window variables
window_size = width, height = [600, 650]
box_width = width / 3
box_height = 600 / 3
box_size = [box_width, box_height]

# Game variables
round_count = 0
winner = ""
x_win = 0
o_win = 0

# Colors
black = 0, 0, 0
red = 250, 0, 0
white = 255, 255, 255

# Screen initialization
screen = pygame.display.set_mode(window_size)
screen.fill(white)
pygame.display.set_caption("Tick Tack Toe")
pygame_icon = pygame.image.load("tictactoe_effects/TickTackToe_Icon.jpg")
pygame.display.set_icon(pygame_icon)

# Fonts
font = pygame.font.SysFont("Copperplate Gothic Bold", 350)
font2 = pygame.font.SysFont("Copperplate Gothic Bold", 32)
font3 = pygame.font.SysFont("Calibri light ", 22)

# Sound effects
x_sound = pygame.mixer.Sound("tictactoe_effects/x_sound.mp3")
o_sound = pygame.mixer.Sound("tictactoe_effects/o_sound.mp3")

# Choosing current player at the start of the round
if round_count % 2 == 0:
    player = True
else:
    player = False


# Box class
class Box:
    def __init__(self, size, box_number, center, is_available=True, item=""):
        self.size = size
        self.box_number = box_number
        self.center = center
        self.is_available = is_available
        self.item = item

    # Drawing box field
    def draw_box(self):
        if 1 <= self.box_number <= 3:
            pygame.draw.rect(screen, black,
                             pygame.Rect(0 + box_width * (self.box_number - 1), 0, self.size[0], self.size[1]), 3)
        if 4 <= self.box_number <= 6:
            pygame.draw.rect(screen, black,
                             pygame.Rect(0 + box_width * (self.box_number - 4), box_height, self.size[0], self.size[1]),
                             3)
        if 7 <= self.box_number <= 9:
            pygame.draw.rect(screen, black,
                             pygame.Rect(0 + box_width * (self.box_number - 7), box_height * 2, self.size[0],
                                         self.size[1]), 3)

    def draw(self):
        global player
        if self.is_available:
            self.is_available = False
            if player:
                self.draw_x()
                player = False
            else:
                player = True
                self.draw_o()

    def draw_x(self):
        text = font.render("x", True, black)
        text_rect = text.get_rect(center=self.center)
        screen.blit(text, text_rect)
        pygame.mixer.Sound.play(x_sound)
        self.item = "x"

    def draw_o(self):
        text = font.render("o", True, black)
        text_rect = text.get_rect(center=self.center)
        screen.blit(text, text_rect)
        pygame.mixer.Sound.play(o_sound)
        self.item = "o"


# Creating box objects
box1 = Box(box_size, 1, (100, 100), item="1")
box2 = Box(box_size, 2, (100, 300), item="2")
box3 = Box(box_size, 3, (100, 500), item="3")
box4 = Box(box_size, 4, (300, 100), item="4")
box5 = Box(box_size, 5, (300, 300), item="5")
box6 = Box(box_size, 6, (300, 500), item="6")
box7 = Box(box_size, 7, (500, 100), item="7")
box8 = Box(box_size, 8, (500, 300), item="8")
box9 = Box(box_size, 9, (500, 500), item="9")


def draw_field():
    box1.draw_box()
    box2.draw_box()
    box3.draw_box()
    box4.draw_box()
    box5.draw_box()
    box6.draw_box()
    box7.draw_box()
    box8.draw_box()
    box9.draw_box()

# Drawing buttons
def draw_buttons():
    pygame.draw.rect(screen,white, (410,605,180,30))
    pygame.draw.rect(screen, black, (430, 602, 140, 40), 2, 4)
    text = font3.render("Press R to restart", True, black)
    text2 = font3.render("Press ESC to exit", True, black)
    text_rect = text.get_rect(center=(500, 613))
    text2_rect = text2.get_rect(center=(500, 628))
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)


# Drawing text on the bottom
def draw_player():
    if player:
        turn = "X"
    else:
        turn = "O"

    pygame.draw.rect(screen, white, pygame.Rect(0, 600, 400, 100))
    text = font2.render(f"Player {turn}´s turn", True, black)
    text_rect = text.get_rect(center=(100, 620))
    screen.blit(text, text_rect)

    text2 = font2.render(f"X:{int(x_win/2)}  O:{int(o_win/2)}", True, black)
    text2_rect = text2.get_rect(center=(300, 620))
    screen.blit(text2, text2_rect)


# Blocking the mouse because of a bug
def block_mouse():
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.MOUSEWHEEL)

# Restarting the game
def restart():
    global screen, font, player
    screen.fill(white)
    font = pygame.font.SysFont("Copperplate Gothic Bold", 350)
    draw_field()
    box1.is_available = True
    box2.is_available = True
    box3.is_available = True
    box4.is_available = True
    box5.is_available = True
    box6.is_available = True
    box7.is_available = True
    box8.is_available = True
    box9.is_available = True
    draw_buttons()
    box1.item = "1"
    box2.item = "2"
    box3.item = "3"
    box4.item = "4"
    box5.item = "5"
    box6.item = "6"
    box7.item = "7"
    box8.item = "8"
    box9.item = "9"


# Mainloop
while True:
    pygame.event.set_grab(True)
    draw_field()
    draw_buttons()
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
    while True:
        draw_player()
        # Checking for win
        if box1.item == box2.item == box3.item or box1.item == box5.item == box9.item or box1.item == box4.item == box7.item or box2.item == box5.item == box8.item or box3.item == box6.item == box9.item or box4.item == box5.item == box6.item or box7.item == box8.item == box9.item or box3.item == box5.item == box7.item:
            if player:
                pygame.draw.rect(screen, white, pygame.Rect(0, 600, 350, 100))
                text = font2.render("O WON!", True, red)
                text_rect = text.get_rect(center=(100, 620))
                text2 = font2.render("Press R to continue", True, red)
                text2_rect = text.get_rect(center=(240, 620))
                screen.blit(text,text_rect)
                screen.blit(text2, text2_rect)
                winner = "o"
                block_mouse()
                break
            else:
                pygame.draw.rect(screen, white, pygame.Rect(0, 600, 360, 100))
                text = font2.render("X WON!", True, red)
                text_rect = text.get_rect(center=(100, 620))
                text2 = font2.render("Press R to continue", True, red)
                text2_rect = text.get_rect(center=(240, 620))
                screen.blit(text, text_rect)
                screen.blit(text2, text2_rect)
                winner = "x"
                block_mouse()
                break
                
        for event in pygame.event.get():
            # Turning off the game
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart()
            # Mouse click
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # Checking row
                if pos[0] <= box_width:
                    # Checking column
                    if pos[1] <= box_height:
                        box1.draw()

                    elif pos[1] <= box_height * 2:
                        box2.draw()
                    elif pos[1] <= 600:
                        box3.draw()

                elif pos[0] <= box_width * 2:
                    if pos[1] <= box_height:
                        box4.draw()
                    elif pos[1] <= box_height * 2:
                        box5.draw()
                    elif pos[1] <= 600:
                        box6.draw()
                elif pos[0] <= 600:
                    if pos[1] <= box_height:
                        box7.draw()

                    elif pos[1] <= box_height * 2:
                        box8.draw()
                    elif pos[1] <= 600:
                        box9.draw()

        pygame.display.update()

    for event in pygame.event.get():

        # Getting the winner
        if pygame.mouse.get_focused():
            if winner == "o":
                o_win += 1
            else:
                x_win += 1
        else:
            if winner == "o":
                o_win -= 1
            else:
                x_win -= 1
        # Turning off the game
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            round_count += 1
            restart()

    pygame.display.update()
