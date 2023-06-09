import time
import turtle
import random
#author: spasemax0
#description: simple snake game in python with score tracking
#in order to customize background simply drag any .gif image file into the snake game folder, copy path, and paste path in required section

#set up the game window
from shutil import move

import food as food
import snake as snake

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# Register the grass image
#turtle.register_shape("INSERT BACKGROUND IMAGE PATH HERE")
wn.bgcolor("green") #change color for different background color, comment this line out if using custom background image

# Set up the game screen with the grass background
wn.setup(920, 700)
#wn.bgpic("INSERT BACKGROUND IMAGE PATH HERE")


#Create scoreboard
score = 0
scoreboard = turtle.Turtle()
#scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
#scoreboard.goto(0, 280)
#scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Create the snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # set the head attribute to the first segment of the snake

    def create_snake(self):
        for i in range(3):
            segment = turtle.Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(0, 280)
            self.segments.append(segment)

    def update_score(self):
        global score
        scoreboard.clear()
        scoreboard.goto(0, 280)
        score += 1
        scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, segment):
        self.segments.append(segment)

    def reset(self):
        global score
        score = 0
        for segment in self.segments:
            if segment.isvisible():  # check if segment is still alive
                segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        scoreboard.clear()
        scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))




# Create the food
def create_food():
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(random.randint(-280, 280), random.randint(-280, 280))
    return food


snake = Snake()
food = create_food()

while True:
    wn.update()

    # Move the snake
    snake.move()

    # Set up the keyboard bindings
    wn.onkeypress(snake.go_up, "Up")
    wn.onkeypress(snake.go_down, "Down")
    wn.onkeypress(snake.go_left, "Left")
    wn.onkeypress(snake.go_right, "Right")
    wn.listen()

    # Check for collision with food
    if snake.head.distance(food) < 20:
        # Move the food to a random position
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        snake.add_segment(new_segment)

        # Update the score
        snake.update_score()

    # Check for collision with the border
    if snake.head.xcor() > 420 or snake.head.xcor() < -420 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        time.sleep(1)
        snake.reset()
        scoreboard.reset()
