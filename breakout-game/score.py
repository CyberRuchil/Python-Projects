from turtle import *

class Scoreboard:
    '''
    This class is used to set Score board and calculate score.

    Parameters
    ----------
    width : The width of the screen. Used in calculation of posititon of the score board and place score board on the screen.
    height : The height of the screen. Used in calculation of position of the score board and place score board on the screen.
    '''
    def __init__(self, width:int, height:int):
        self.score = 0
        self.width = width
        self.height = height

    def scoreboard(self):
        '''
        This function creates a score board which shows the score.
        '''
        self.score_board = Turtle()
        self.score_board.hideturtle()
        self.score_board.penup()
        x = 0
        y = (self.height/2 - 40)
        self.score_board.goto(x, y)
        self.score_update()

    def score_update(self):
        '''
        This function updates the score on the score board.
        '''
        self.score_board.clear()
        self.score_board.write(f'Score: {self.score}',align='center', font=('Arial', 32, 'normal'))
