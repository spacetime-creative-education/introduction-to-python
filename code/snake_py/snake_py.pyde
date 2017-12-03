# Snake video game
import random

# CONSTANTS
SCRN_WIDTH = 300
SCRN_HEIGHT = 400
GRID_LENGTH = 10
X_LENGTH = (SCRN_WIDTH // GRID_LENGTH)
Y_LENGTH = (SCRN_HEIGHT // GRID_LENGTH)

# AFTER DEFEAT
defeat_cnt = 0
game_over_on = True

def setup():
    size(SCRN_WIDTH, SCRN_HEIGHT)
    global python
    python = Snake()
    python.draw_food()
    frameRate(4)
    ellipseMode(CORNER)

def draw():
    global python
    global defeat_cnt
    global game_over_on
    clear()
    noStroke()
    fill(128)
    for x in range(0, int(SCRN_WIDTH/GRID_LENGTH)):
        for y in range(0, int(SCRN_HEIGHT/GRID_LENGTH)):
            rect(x*GRID_LENGTH, y*GRID_LENGTH, GRID_LENGTH, GRID_LENGTH)
    
    if not python.defeat:    
        fill(255)
        python.update()
        python.draw_snake()
        python.draw_food()
        if python.captured_food:
            python.create_food()
    else:
        defeat_cnt += 1
        if defeat_cnt % 2 == 0:
            game_over_on = not game_over_on
        print(game_over_on, defeat_cnt)
        if game_over_on:
            fill(255)
            for bx_x, bx_y in python.boxes:
                rect(bx_x*GRID_LENGTH, bx_y*GRID_LENGTH, GRID_LENGTH, GRID_LENGTH)
            textSize(24)
            text("GAME OVER", int(SCRN_WIDTH/GRID_LENGTH)*GRID_LENGTH, int(SCRN_HEIGHT/GRID_LENGTH)*GRID_LENGTH)
        else:
            fill(0)
            
def keyPressed():
    global python
    if keyCode == UP and python.direction != [0, 1]:
        python.direction = [0, -1]
    elif keyCode == DOWN and python.direction != [0, -1]:
        python.direction = [0, 1]
    elif keyCode == RIGHT and python.direction != [-1, 0]:
        python.direction = [1, 0]
    elif keyCode == LEFT and python.direction != [1, 0]:
        python.direction = [-1, 0]
    else:
        pass
    
class Snake(object):
    def __init__(self):
        self.length = 4
        self.speed = 1     # box per frame
        self.direction = [1, 0]    # [i, j] ref. unit vector for x direction
        self.boxes = []
        self.captured_food = False
        self.food = []
        self.defeat = False
        for bx in range(0, self.length):
            bx_x = (SCRN_WIDTH / 2 // GRID_LENGTH) - bx
            bx_y = (SCRN_HEIGHT / 2 // GRID_LENGTH)
            self.boxes.append([bx_x, bx_y])    # the location of top-left corners of boxes, head to tail
        fill(255)
        self.draw_snake()
            
    def update(self):
        bx_x = self.boxes[0][0]
        bx_y = self.boxes[0][1]
        
        bx_x = bx_x + self.direction[0]*self.speed
        bx_y = bx_y + self.direction[1]*self.speed
        
        # if the snake goes out of boundary bring it from the other side
        if bx_x > X_LENGTH:
            bx_x = 0
        if bx_x < 0:
            bx_x = X_LENGTH
        if bx_y > Y_LENGTH:
            bx_y = 0
        if bx_y < 0:
            bx_y = Y_LENGTH
        
        
        if not self.captured_food:
            self.boxes.pop(-1)    # remove the last box from tail
            
        self.boxes.insert(0, [bx_x, bx_y])
        
        # check if the snake has eaten itself
        for sk_x, sk_y in self.boxes[1:]:
            if [bx_x, bx_y] == [sk_x, sk_y]:
                self.defeat = True
    
    def draw_snake(self):
        stroke(192)
        for bx_x, bx_y in self.boxes:
            rect(bx_x*GRID_LENGTH, bx_y*GRID_LENGTH, GRID_LENGTH, GRID_LENGTH)
        
        if self.food and self.boxes[0] == self.food:
            self.length += 1
            self.captured_food = True
        else:
            self.captured_food = False
        
    def create_food(self):
        food_x = random.randint(0, int(SCRN_WIDTH/GRID_LENGTH))
        food_y = random.randint(0, int(SCRN_HEIGHT/GRID_LENGTH))
        self.food = [food_x, food_y]
        
    def draw_food(self):
        """
        Food is randomly placed on any square in the grid
        """
        if not self.food:
            self.create_food()
        ellipse(self.food[0]*GRID_LENGTH, self.food[1]*GRID_LENGTH, GRID_LENGTH, GRID_LENGTH)