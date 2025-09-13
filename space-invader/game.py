from turtle import Turtle, Screen
import time

# -------------------- Constants --------------------
WIDTH = 1000
HEIGHT = 700
COLOR = 'green'

# -------------------- Player Controls --------------------
def move_right():
    """Move spaceship to the right within boundary."""
    boundary(spaceship)
    spaceship.forward(10)

def move_left():
    """Move spaceship to the left within boundary."""
    boundary(spaceship)
    spaceship.backward(10)

# -------------------- Game Over Check --------------------
def is_game_on(alien_army):
    """Checks if all aliens are destroyed. If yes, ends the game."""
    if len(alien_army) == 0:
        screen.clear()
        end = Turtle()
        end.hideturtle()
        end.color(COLOR)
        end.penup()
        end.goto(0, 0)
        end.write('Game Over. You Won', align='center', font=("Arial", 28, 'bold'))
        screen.update()
        return False
    return True

# -------------------- Collision & Destruction --------------------
def alien_destroy(missile):
    """Destroys alien if missile collides with it and updates score."""
    global score
    for alien in alien_army:
        if missile.distance(alien) < 8:
            alien.goto(1000, 1000)  # Move off screen
            alien_army.remove(alien)
            missile.goto(1000, 1000)
            score_display.clear()
            score += 1
            score_display.write(f'Score: {score}', font=("Arial", 16, 'bold'))
            break

def check_alien_reach_bottom():
    """Checks if any alien has reached the spaceship's level."""
    for alien in alien_army:
        if alien.ycor() < -(y - 45):  # y-level of spaceship
            game = Turtle()
            game.hideturtle()
            game.color(COLOR)
            game.penup()
            game.goto(0, 0)
            game.write('Game Over. Aliens Won!', align='center', font=("Arial", 28, 'bold'))
            screen.update()
            return True
    return False

# -------------------- Attack Mechanics --------------------
def attack(turtle):
    """Fires a missile from the current position of the spaceship."""
    x, y = turtle.pos()
    missile = Turtle(shape='square')
    missile.shapesize(0.15, 0.5)
    missile.color(COLOR)
    missile.penup()
    missile.setheading(90)
    missile.goto(x, y)
    missile.speed(1)
    move_missile(missile)

def move_missile(missile):
    """Moves the missile upwards and checks for collisions."""
    alien_destroy(missile)
    if missile.ycor() < HEIGHT / 2:
        missile.forward(10)
        screen.ontimer(lambda: move_missile(missile), 30)
    else:
        missile.hideturtle()
        missile.goto(1000, 1000)  # Move off screen and clean up

# -------------------- Boundaries --------------------
def boundary(turtle):
    """Prevents spaceship from moving outside defined boundaries."""
    x = turtle.xcor()
    if x < -200:
        turtle.forward(20)
    if x > 200:
        turtle.backward(20)

def alien_boundary(alien_army):
    """Handles alien direction change on reaching screen edge."""
    for alien in alien_army:
        x = alien.xcor()
        if x < -200:
            for alien in alien_army:
                alien.setheading(0)
            return True
        elif x > 200:
            for alien in alien_army:
                alien.setheading(180)
            return True
    return False

# -------------------- Alien Movement --------------------
def aliens_move(alien_army):
    """Moves all aliens sideways and schedules next movement."""
    alien_boundary(alien_army)
    for alien in alien_army:
        alien.forward(20)
    screen.ontimer(lambda: aliens_move(alien_army), 1000)

def aliens_move_down(alien_army):
    """Moves all aliens downwards (triggered periodically)."""
    for i in range(3):
        for alien in alien_army:
            y_cor = alien.ycor()
            alien.sety(y_cor - (i * 25))

# -------------------- Setup Screen --------------------
screen = Screen()
screen.title('Space Invader')
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

# -------------------- Game State Variables --------------------
life_count = 3
score = 0
alien_army = []

# -------------------- Create Defense Line --------------------
y = HEIGHT / 2 - 140
line = Turtle(shape='square')
line.shapesize(0.1, 24)
line.color(COLOR)
line.penup()
line.goto(0, -y)

# -------------------- Create Player Spaceship --------------------
spaceship = Turtle(shape='square')
spaceship.shapesize(0.85, 1.85)
spaceship.color(COLOR)
spaceship.penup()
spaceship.goto(0, -(y - 45))

# -------------------- Create Alien Army --------------------
for i in range(3):
    for j in range(8):
        alien = Turtle(shape='square')
        alien.shapesize(0.8, 0.8)
        alien.color(COLOR)
        alien.penup()
        alien.speed(3)
        alien.goto(-220 + (j * 25), y - (i * 25))
        alien_army.append(alien)

# -------------------- Score Display --------------------
score_display = Turtle()
score_display.hideturtle()
score_display.color(COLOR)
score_display.penup()
score_display.goto(140, -(y + 35))
score_display.write(f'Score: {score}', font=("Arial", 16, 'bold'))

# -------------------- Life Indicators --------------------
for i in range(life_count - 1):
    life = Turtle(shape='square')
    life.shapesize(0.85, 1.85)
    life.color(COLOR)
    life.penup()
    life.goto(-220 + (i * 45), -(y + 25))

# -------------------- Start Alien Movement --------------------
aliens_move(alien_army)

# -------------------- Key Bindings --------------------
screen.listen()
screen.onkey(move_right, 'Right')
screen.onkey(move_left, 'Left')
screen.onkey(lambda: attack(spaceship), 'space')

# -------------------- Game Loop --------------------
t1 = time.time()

def game_loop():
    """Main game loop: updates alien position and checks game state."""
    global t1
    t2 = time.time()
    t = int(t2 - t1)

    # Drop aliens down every 60 seconds
    if t > 60 and alien_boundary(alien_army):
        t1 = time.time()
        aliens_move_down(alien_army)

    # Continue loop if game is still active
    if is_game_on(alien_army) and not check_alien_reach_bottom():
        screen.update()
        screen.ontimer(game_loop, 100)

# Start the game
game_loop()
screen.mainloop()
