from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        scoreboard.track()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        game_on = False

    for segment in snake.segments[1:]: #or, for segment in snake.segments: \n  if segment == snake.head  \n  pass
        if snake.head.distance(segment) < 10:

            scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            game_on = False












screen.exitonclick()


















