from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #Detect collision with food
    if snake.snake_parts[0].distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    #Detect collision with wall
    if snake.snake_parts[0].xcor() > 280 or snake.snake_parts[0].xcor() < -280 or snake.snake_parts[0].ycor() > 280 or snake.snake_parts[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for snake_part in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(snake_part) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()