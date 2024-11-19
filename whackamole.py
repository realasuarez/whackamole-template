import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_rect = pygame.Rect(mole_x, mole_y, 32, 32)
                    if mole_rect.collidepoint(event.pos):
                        mole_x = random.randrange(0,640,32)
                        mole_y = random.randrange(0,512,32)
            screen.fill((113, 7, 184))
            for x in range(0,640,32):
                pygame.draw.line(screen, "black",(x,0), (x,512))
            for y in range(0,512,32):
                pygame.draw.line(screen,"black",(0,y),(640,y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
