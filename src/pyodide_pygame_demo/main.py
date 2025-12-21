import asyncio
import importlib.resources
import pygame

BALL_RADIUS = 40
BALL_SPEED = 0.25
BG_COLOUR = pygame.Color("black")
FRAME_DELAY = 1.0 / 120.0
HINT_COLOUR = pygame.Color("white")
HINT_OFFSET = 40
HINT_SIZE = 48
HINT_TEXT = "Click/tap to mute/unmute"
HUE_MAX = 360
HUE_RATE = 0.5
SCREEN_CENTRE = (320, 240)
SCREEN_SIZE = (640, 480)


def draw_centred_text(
    surface: pygame.Surface, font: pygame.Font, position: tuple[int, int], text: str
) -> None:
    x, y = position
    width, height = font.size(text)
    surface.blit(font.render(text, True, HINT_COLOUR), (x - width / 2, y - height / 2))


def wrap(value: int, max: int) -> int:
    return value % max if value > max else value


async def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    running = True
    muted = False

    ball_colour = pygame.Color("blue")
    ball_direction = pygame.Vector2(1, 1)
    ball_position = pygame.Vector2(*SCREEN_CENTRE)

    bounce_sound = pygame.Sound(
        importlib.resources.files().joinpath("assets", "blip.wav")
    )
    bounce_sound.set_volume(0.25)

    hint_font = pygame.Font(size=HINT_SIZE)

    last_ticks = pygame.time.get_ticks()
    dt = 0.0

    while running:
        events = pygame.event.get()

        if any(event.type == pygame.QUIT for event in events):
            running = False
        elif any(event.type == pygame.MOUSEBUTTONDOWN for event in events):
            muted = not muted

        screen.fill(BG_COLOUR)

        # Shift hue according to HUE_RATE and time since last frame
        h, *sla = ball_colour.hsla
        ball_colour.hsla = (wrap(h + round(dt * HUE_RATE), HUE_MAX), *sla)

        # Move ball position in the current direction according to BALL_SPEED
        # and time since last frame
        ball_position += ball_direction * BALL_SPEED * dt

        # Track if the ball bounced to determine whether to play the sound
        bounced = False

        # Bounce the ball if it hits the left or right sides
        if ball_position.x - BALL_RADIUS < 0:
            ball_direction.x = 1
            bounced = True
        elif ball_position.x + BALL_RADIUS > SCREEN_SIZE[0]:
            ball_direction.x = -1
            bounced = True

        # Bounce the ball if it hits the top or bottom sides
        if ball_position.y - BALL_RADIUS < 0:
            ball_direction.y = 1
            bounced = True
        elif ball_position.y + BALL_RADIUS > SCREEN_SIZE[1]:
            ball_direction.y = -1
            bounced = True

        # Play the sound effect if we bounced off of any edge
        if bounced and not muted:
            bounce_sound.play()

        # Draw the ball, hint text, and flip the framebuffer
        pygame.draw.circle(screen, ball_colour, ball_position, BALL_RADIUS)
        draw_centred_text(
            screen,
            hint_font,
            (SCREEN_CENTRE[0], SCREEN_SIZE[1] - HINT_OFFSET),
            HINT_TEXT,
        )
        pygame.display.flip()

        # Replacement for framerate-less pygame.Clock.tick
        ticks = pygame.time.get_ticks()
        dt = ticks - last_ticks
        last_ticks = ticks

        # Yield each frame, pyodide doesn't work properly with a value of 0 so we use a small delay
        await asyncio.sleep(FRAME_DELAY)


if __name__ == "__main__":
    asyncio.run(main())
