import pygame
from network import Network

width = 500
height = 500

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.vel
        
        if keys[pygame.K_s]:
            self.y += self.vel
        
        if keys[pygame.K_a]:
            self.x -= self.vel
        
        if keys[pygame.K_d]:
            self.x += self.vel

        self.update()
    
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def redrawWindow(win, player, player2):
    win.fill(WHITE)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    clock = pygame.time.Clock()
    p = Player(startPos[0] ,startPos[1], 100, 100, (GREEN))
    p2 = Player(0, 0, 100, 100, (RED))

    while run:
        clock.tick(60)

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

if __name__ == "__main__":
    main()