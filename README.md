# Pong Game in Python

This is a simple implementation of the classic Pong game in Python using the Turtle graphics library. The game features two paddles and a ball that bounces between the paddles. Players can control their paddles to hit the ball back and forth, and the game keeps track of the score.

## How to Play

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your computer.
3. Open a terminal or command prompt and navigate to the directory where the files are located.
4. Run the game by executing the `main.py` file:

```
python main.py
```

5. Use the following controls to play the game:

- Player 1 (right paddle):
  - Move up: `Up Arrow`
  - Move down: `Down Arrow`

- Player 2 (left paddle):
  - Move up: `w`
  - Move down: `s`

6. The game will continue until one of the players reaches the score limit of 5.

## File Organization

The code for the Pong game is organized into several files:

1. `main.py`: This is the main script that runs the game. It sets up the screen, paddles, ball, and the scoreboard. It also handles the game loop and player input.

2. `ball.py`: This module contains the code for the Ball class. The Ball class handles the ball's movement, bouncing off walls and paddles, and resetting its position after scoring.

3. `score.py`: This module contains the code for the Score class. The Score class keeps track of the players' scores and updates the scoreboard when a player scores a point.

4. `paddle.py`: This module contains the code for the Paddle class. The Paddle class represents a player's paddle and handles its movement up and down.

Thank you for playing! Enjoy the game!