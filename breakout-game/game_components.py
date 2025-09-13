from turtle import *
import random
from math import floor

WIDTH = 1045
HEIGHT = 720
STRETCH_WIDTH = 1
STRETCH_LEN = 5
OUTLINE = 3

screen = Screen()
screen.colormode(255)

class Components:
    '''
    This class contains all the components used to create the Breakout Game.

    Parameters
    ----------
    width : The width of the screen. Used in calculation of posititon of the components and place components on the screen.
    height : The height of the screen. Used in calculation of position of the components and place components on the screen.
    '''
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height
        self.n = floor((self.width/100))

    def create_block(self,x:float,y:float, block_color:tuple)->object:
        '''
        This function creates a single block/brick which is a part of the game.

        Parameters
        ----------
        x : This parameter is used to place the block in x-axis.
        y : This paramter is used to place the block in y-xis.
        block_color : This parameter is the color of the block.

        Returns
        -------
        It returns the block which we created. It is a turtle object.
        '''
        block = Turtle(shape='square')
        block.shapesize(STRETCH_WIDTH,STRETCH_LEN, outline=OUTLINE)
        block.penup()
        block.color("black",block_color)
        block.goto(x, y)
        return block

    def game_field(self)->list:
        '''
        This function creates a field of blocks using the create_block method.

        Returns
        -------
        It returns the list of all the blocks using which the field was created. 
        '''
        self.blocks_list = []
        j = 0
        block_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        for _ in range(5):
            if j>=1:
                if j % 2 == 0:
                    block_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            for i in range(self.n):
                x = -((self.width/2) - (STRETCH_LEN*10 + OUTLINE)) + (i*103)
                y = 250 - (j*20)
                block = self.create_block(x,y, block_color)
                self.blocks_list.append(block)
            j+=1
        
        return self.blocks_list
        
    def paddle(self)->object:
        '''
        This function is used to create a paddle.

        Returns
        -------
        It returns the paddle object we created.
        '''
        paddle_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.pad = Turtle(shape='square')
        self.pad.shapesize(STRETCH_WIDTH,STRETCH_LEN*2)
        self.pad.penup()
        self.pad.color(paddle_color)
        self.pad.speed(0)
        y = -(self.height/2 - 40)
        self.pad.sety(y)
        return self.pad

    def ball(self,x,y):
        '''
        This function is used to create a ball.

        Returns
        -------
        It returns the ball object we created.
        '''
        self.circle = Turtle(shape='circle')
        self.circle.penup()
        self.circle.setheading(90)
        self.circle.color('#a6a8a5')
        self.circle.goto(x,y+22)
        self.circle.speed(1)
        return self.circle
    

