from turtle import Screen
from Snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Detect collision with food
    ate_food =False
    if snake.segs[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        ate_food = True
    # Maintaining Score
    if ate_food:
        score.scored()
    # Detect collision with wall
    if snake.segs[0].xcor() > 280 or snake.segs[0].xcor() < -280 or snake.segs[0].ycor() > 300 or snake.segs[0].ycor() < -280:
        score.reset()
        snake.reset()
    # Detect collision with tail
    for seg in snake.segs[1:]:
        if snake.segs[0].distance(seg) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
