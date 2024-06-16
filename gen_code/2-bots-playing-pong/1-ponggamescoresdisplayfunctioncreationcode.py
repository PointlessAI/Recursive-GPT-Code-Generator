import pygame
import sys

# Initialize the game
pygame.init()

# Set up the screen parameters
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the paddles
paddle_width = 10
paddle_height = 100
left_paddle = pygame.Rect(50, 250, paddle_width, paddle_height)
right_paddle = pygame.Rect(740, 250, paddle_width, paddle_height)

# Set up the ball parameters
ball = pygame.Rect(screen_width//2 - 15, screen_height//2 - 15, 30, 30)
ball_speed_x = 6
ball_speed_y = 6

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Enhancement: Create a function to display scores by blitting them on the screen
def display_score(left_score, right_score):
    font = pygame.font.SysFont('calibri', 40)
    text = font.render(f'{left_score}  {right_score}', True, white)
    screen.blit(text, (screen_width//2 - text.get_width()//2, 100))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles as per logic for bots
    if ball.centerx < screen_width // 2:
        if ball.y > left_paddle.centery:
            left_paddle.y += 5
        elif ball.y < left_paddle.centery:
            left_paddle.y -= 5
    else:
        if ball.y > right_paddle.centery:
            right_paddle.y += 5
        elif ball.y < right_paddle.centery:
            right_paddle.y -= 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Check score
    if ball.left <= 0:
        # Player 2 (right paddle) scores
        ball.center = (screen_width//2, screen_height//2)
        ball_speed_x *= -1
        right_score += 1
    elif ball.right >= screen_width:
        # Player 1 (left paddle) scores
        ball.center = (screen_width//2, screen_height//2)
        ball_speed_x *= -1
        left_score += 1

    # Update the screen
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, ball)
    display_score(left_score, right_score)
    pygame.display.flip()
    clock.tick(60)
