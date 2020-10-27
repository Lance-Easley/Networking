import pygame
from network import Network
from player import Player

height = 500
width = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, player1, player2, player3):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    player3.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        p2, p3 = n.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p1.move()
        redrawWindow(win, p1, p2, p3)

main()