import pygame

BALL_RADIUS = 40
BG_COLOUR = pygame.Color("black")
HUE_MAX = 360
HUE_RATE = 0.5
SCREEN_CENTRE = (320, 240)
SCREEN_SIZE = (640, 480)


def wrap(value: int, max: int) -> int:
    return value % max if value > max else value


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.Clock()
    running = True
    ball_colour = pygame.Color("blue")
    dt = 0.0

    while running:
        events = pygame.event.get()

        if any(event.type == pygame.QUIT for event in events):
            running = False

        screen.fill(BG_COLOUR)

        # Shift hue according to HUE_RATE and time since last frame
        h, *sla = ball_colour.hsla
        ball_colour.hsla = (wrap(h + round(dt * HUE_RATE), HUE_MAX), *sla)
        pygame.draw.circle(screen, ball_colour, SCREEN_CENTRE, BALL_RADIUS)

        pygame.display.flip()
        dt = clock.tick()


if __name__ == "__main__":
    main()
