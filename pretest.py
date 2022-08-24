import random
import pygame

pygame.init()

pygame.display.set_caption("ANTS")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))

user_in = int(input("Enter a whole number: "))
#user_in = 4
if user_in % 3 == 0:
    print("boogers")
else:
    print("squirrels!")

for i in range(10, 35, 5):
    print(i)

def midpoint(x1, y1, x2 ,y2):
    return (x1 + x2) / 2, (y1 + y2) / 2
print(midpoint(1,1,2,2))

names = ["Kyle", "Eduardo", "Cory", "Aidan", "Lily"]
if "Mo" in names:
    print("nerd alert")
else:
    print("cool kids only")

class ANT:
    def __init__(self, x: int, y: int, queen_status: bool, color: str):
        self.x_pos = x
        self.y_pos = y
        self.is_queen = queen_status
        if color == "Red":
            self.color_val = (255,0,0)
        elif color == "Blue":
            self.color_val = (0,0,255)
        elif color == "Purple":
            self.color_val = (255,0,255)

    def stat_prnt(self):
        pygame.draw.rect(screen, self.color_val, ((self.x_pos,self.y_pos, 10, 50)))

    def bark(self):
        print("woof")

    def move(self):
        self.x_pos += random.randint(-5, 5)
        self.y_pos += random.randint(-5, 5)


ants = []
for i in range(100):
    if random.randint(1,100) % 99 == 0:
        queen = True
    else:
        queen = False
    if queen:
        color = "Purple"
    else:
        if random.randint(0,1) == 0:
            color = "Blue"
        else:
            color = "Red"
    ants.append(ANT(random.randint(100,700),random.randint(100,700),queen,color))


ticker = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        running = False

    if ticker % 30000 == 0:
        screen.fill((0,0,0))

        for ant in ants:
            ant.stat_prnt()
            ant.bark()
            ant.move()

        pygame.display.flip()
    ticker += 1