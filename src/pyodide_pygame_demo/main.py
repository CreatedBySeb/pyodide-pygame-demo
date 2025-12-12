import pygame

BALL_RADIUS = 40
BALL_SPEED = 0.25
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
    ball_direction = pygame.Vector2(1, 1)
    ball_position = pygame.Vector2(*SCREEN_CENTRE)
    dt = 0.0

    while running:
        events = pygame.event.get()

        if any(event.type == pygame.QUIT for event in events):
            running = False

        screen.fill(BG_COLOUR)

        # Shift hue according to HUE_RATE and time since last frame
        h, *sla = ball_colour.hsla
        ball_colour.hsla = (wrap(h + round(dt * HUE_RATE), HUE_MAX), *sla)

        # Move ball position in the current direction according to BALL_SPEED
        # and time since last frame
        ball_position += ball_direction * BALL_SPEED * dt

        # Bounce the ball if it hits the left or right sides
        if ball_position.x - BALL_RADIUS < 0:
            ball_direction.x = 1
        elif ball_position.x + BALL_RADIUS > SCREEN_SIZE[0]:
            ball_direction.x = -1

        # Bounce the ball if it hits the top or bottom sides
        if ball_position.y - BALL_RADIUS < 0:
            ball_direction.y = 1
        elif ball_position.y + BALL_RADIUS > SCREEN_SIZE[1]:
            ball_direction.y = -1

        pygame.draw.circle(screen, ball_colour, ball_position, BALL_RADIUS)

        pygame.display.flip()
        dt = clock.tick()


if __name__ == "__main__":
    main()
