import pygame

BALL_RADIUS = 40
BG_COLOUR = pygame.Color("black")
SCREEN_CENTRE = (320, 240)
SCREEN_SIZE = (640, 480)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.Clock()
    running = True
    ball_colour = pygame.Color("blue")

    while running:
        events = pygame.event.get()

        if any(event.type == pygame.QUIT for event in events):
            running = False

        screen.fill(BG_COLOUR)

        pygame.draw.circle(screen, ball_colour, SCREEN_CENTRE, BALL_RADIUS)

        pygame.display.flip()
        clock.tick()


if __name__ == "__main__":
    main()
