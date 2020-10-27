import pygame
from network import Network
from player import Player

height = 300
width = 300
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, player1, player2, player3, player4, player5, player6, player7, player8, player9):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    player3.draw(win)
    player4.draw(win)
    player5.draw(win)
    player6.draw(win)
    player7.draw(win)
    player8.draw(win)
    player9.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        p2, p3, p4, p5, p6, p7, p8, p9 = n.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p1.move()
        redrawWindow(win, p1, p2, p3, p4, p5, p6, p7, p8, p9)

main()