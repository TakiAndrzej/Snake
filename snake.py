from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.xcor = 0
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.setposition(position)
        self.snake_parts.append(snake)

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def reset(self):
        for part in self.snake_parts:
            part.hideturtle()
        self.snake_parts.clear()
        self.create_snake()

    def move(self):
        for snake in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[snake].goto(self.snake_parts[snake - 1].position())
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)

    def left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)

    def right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)