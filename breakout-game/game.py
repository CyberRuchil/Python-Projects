from turtle import *
from game_components import Components
from score import Scoreboard
import random

WIDTH = 1045 # widht of the screen
HEIGHT = 720 # height of the screen

# ------------------------- Setting up Screen -------------------------
screen = Screen()
screen.colormode(255)
screen.setup(WIDTH,HEIGHT)
screen.title('Breakout Game')


game = Components(WIDTH,HEIGHT)
score_board = Scoreboard(WIDTH,HEIGHT)


# ------------------------- Game's Logic Functions -------------------------

def ball_move():
    '''
    This function is used to move the ball.
    '''
    ball.forward(10)

def ball_direction():
        '''
        This function is used to set the ball's direction.
        '''
        direction = random.choice(['left','right'])
        
        if direction == 'right':
            ball.right(45)

        else:
            ball.left(45)


    

def ball_bounce():
    '''
    This function is used to bounce the ball when it touches the paddle, a block or the north, east, west side of the screen.
    '''
    ballx, bally = ball.position()
    paddlex, paddley = paddle.position()
    xcord = (WIDTH/2 - 25)
    ycord = (HEIGHT/2 - 25)

    if ((0 < (ballx - paddlex) <= 52) or (0 < (paddlex - ballx) <= 52)) and (bally - paddley) <= 24 :
            
            ball.setheading(90)
            ball_direction()


    for block in blocks:
        if ball.distance(block) < 40:
            block.goto(4000,4000)
            score_board.score += 1
            score_board.score_update()
            ball.setheading(270)
            ball_direction()

    if ballx < (-xcord) or  ballx > xcord or bally > ycord:
        if ballx < (-xcord):
            ball.setheading(0)
        elif ballx > xcord:
            ball.setheading(180)
        elif bally > ycord:
            ball.setheading(270)
        
        ball_direction()
    

def paddle_boundary():
    '''
    This function determines that the paddle is within the screen.
    '''
    x = paddle.xcor()
    xcord = (WIDTH/2 - 100)
    if x <  (-xcord):
        paddle.forward(10)
    elif x > xcord:
        paddle.backward(10)


def gameover()->bool: 
    '''
    Function to check if the game is over or not. It return True or False based on certain game's rule.

    Returns
    -------
    True : if the game is over.Either the Player won or lost.
    False : if the game is not over.
    '''
    bally = ball.ycor()
    ycord = (HEIGHT/2 - 10)
    game_over = Turtle()
    game_over.hideturtle()
    game_over.penup()

    if score_board.score == len(blocks):
        game_over.write('Game Over. You Won',align='center', font=('Arial', 32, 'normal'))     
        return True
    
    elif bally < (-ycord):
        game_over.write('Game Over. You Lose',align='center', font=('Arial', 32, 'normal'))
        return True
    
    return False
    
def move_right():
    '''
    Function to move the paddle right.
    '''
    paddle.forward(50)

def move_left():
    '''
    Function to move the paddle left.
    '''
    paddle.back(50)


# ------------------------- Event Listeners -------------------------

screen.listen()
screen.onkeypress(move_right, 'Right')
screen.onkeypress(move_left, 'Left')

# ------------------------- Game -------------------------
screen.tracer(0) 

blocks = game.game_field()
paddle = game.paddle()
x,y = paddle.position()
ball = game.ball(x,y)
score_board.scoreboard()
ball_direction()
screen.update()

is_game_on = True
i=0

while is_game_on:
    paddle_boundary()
    ball_move()
    ball_bounce()
    if gameover():
        is_game_on = False
    screen.update()

screen.mainloop()