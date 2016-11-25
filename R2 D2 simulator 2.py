import random
import pygame



class asteroidleft: 
    
    def __init__(self):
        #spawn in a random location off screen.
        self.rand_x = random.randint(-90, -30)
        #keep object within the screen.
        self.rand_y = random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
        self.asteroidw_change = 0
        #need this to work out the collision of the rectangle at any point.
        self.asteroidw = self.rand_x + self.asteroid_thickness
        self.asteroidh = self.rand_y + self.asteroid_thickness
        detection = False
    
    def move(self):
        #change direction if if object is off screen
        if self.rand_x < 0:
            self.rand_x_change += 10
            self.asteroidw_change += 10
        if self.rand_x > 1350:
            self.rand_x_change += -10
            self.asteroidw_change += - 10
        self.rand_x += self.rand_x_change
        self.asteroidw += self.asteroidw_change
            
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])
    def collision(self):
        if rect_overlap((ship_x, ship_y, block_size, block_size), (self.rand_x, self.rand_y, self.asteroid_thickness, self.asteroid_thickness)):
            colour = 255,255,255
            pygame.draw.rect(screen, colour, [ship_x,ship_y,block_size,block_size])
            pygame.display.flip()

        
class asteroidright:
    
    def __init__(self):
        self.rand_x = random.randint(1351, 1400)
        self.rand_y = random.randint(0,670)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
    def move(self):
        random_change = random.randint(10,100)
        if self.rand_x < -90:
            self.rand_x_change += 10
        if self.rand_x > 1350:
            self.rand_x_change += -10
        self.rand_x += self.rand_x_change
        if rect_overlap((ship_x, ship_y, block_size, block_size), (self.rand_x, self.rand_y, self.asteroid_thickness, self.asteroid_thickness)):
            detection = True
            
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])

class asteroidup:
    
    def __init__(self):
        self.rand_x = random.randint(0, 1240)
        self.rand_y = random.randint(-90,-30)
        self.asteroidlist = [20,25,30,35,40]
        self.asteroid_thickness = random.choice(self.asteroidlist)
        self.rand_x_change = 0
        self.rand_y_change = 0
    def move(self):
        if self.rand_y < -20:
            self.rand_y_change += 10
        if self.rand_y > 800:
            self.rand_y_change += -10
        self.rand_y += self.rand_y_change
        if rect_overlap((ship_x, ship_y, block_size, block_size), (self.rand_x, self.rand_y, self.asteroid_thickness, self.asteroid_thickness)):
            detection = True
    def draw(self):
        pygame.draw.rect(screen, GREY, [self.rand_x,self.rand_y,self.asteroid_thickness,self.asteroid_thickness])



pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()
fps = 15

BLACK = 0,0,0
GREY = 126,126,126
colour = 255,0,0

ship_x = (width/2)-25
ship_y = (height/2)-25
block_size = 50

#collision function.
def rect_overlap(a, b):
    return \
    a[0] < b[0] + b[2] and \
    a[0] + a[2] > b[0] and \
    a[1] < b[1] + b[3] and \
    a[1] + a[3] > b[1]

objectsleft = []
for o in range(10): # create 5 objects and append them to the empty list
    asteroid1 = asteroidleft()
    objectsleft.append(asteroid1)

objectsright = []
for a in range(10):
    asteroid2 = asteroidright()
    objectsright.append(asteroid2)

objectsup = []
for b in range(10):
    asteroid3 = asteroidup()
    objectsup.append(asteroid3)

#main game
def gameLoop():
    gameOver = False
    
    while not gameOver:
        
        #event detection that will close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver = True

        screen.fill(BLACK)
        #objects made before the loop to be drawn.
        for asteroid1 in objectsleft:
            asteroid1.draw()
        for asteroid2 in objectsright:
            asteroid2.draw()
        for asteroid3 in objectsup:
            asteroid3.draw()
        #objects drawn before to be moved across the screen.
        for asteroid1 in objectsleft:
            asteroid1.move()
        for asteroid2 in objectsright:
            asteroid2.move()
        for asteroid3 in objectsup:
            asteroid3.move()
        for asteroid1 in objectsleft:
            asteroid1.collision()
        #create red block in middle of screen.
        pygame.draw.rect(screen, colour, [ship_x,ship_y,block_size,block_size])
        pygame.display.flip()
        clock.tick(fps)

gameLoop()
pygame.quit()
       
