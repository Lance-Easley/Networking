import pygame
from network import Network
from player import Player

height = 400
width = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, p1, players):
    win.fill((255, 255, 255))
    for p in players:
        p.draw(win)
    p1.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        players = n.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p1.move()
        redrawWindow(win, p1, players)

main()