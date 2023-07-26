from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

R_POS = (350, 0)
L_POS = (-350, 0)

# Screen Set up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# Paddle Set up
r_paddle = Paddle(R_POS)
l_paddle = Paddle(L_POS)

# Ball Set up
ball = Ball()

# Create Scoreboard
score = Score()

# Paddle Movement
screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect R Out of Bounds
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L Out of Bounds
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score == 5 or score.r_score == 5:
        game_on = False
        score.game_over()

screen.exitonclick()
