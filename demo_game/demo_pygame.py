import  sys
import  pygame
from ship import Ship
def youxi_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("blue sky")

    bg_color = (0,124,195)
    s = Ship(screen)

    while True:
        screen.fill(bg_color)
        s.biltme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
youxi_game()