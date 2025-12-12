import pygame

BG_COLOUR = pygame.Color("black")
SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.Clock()
    running = True

    while running:
        events = pygame.event.get()

        if any(event.type == pygame.QUIT for event in events):
            running = False

        screen.fill(BG_COLOUR)
        pygame.display.flip()
        clock.tick()


if __name__ == "__main__":
    main()
