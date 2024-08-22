from turtle import Screen, Turtle
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
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #xac dinh khi nao con ran va cham voi thuc an
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #xac dinh con ran dam vao tuong
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <- 280:
        game_is_on = False
        scoreboard.game_over()
    #xac dinh con ran dam vao than
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()


















screen.exitonclick()