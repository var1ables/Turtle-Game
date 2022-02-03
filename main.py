import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing')

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game = True
while game:
    time.sleep(0.065)
    screen.update()
    scoreboard.update_score()
    cars.placement()
    cars.movement()
    for car in cars.all_cars:
        if car.distance(player) < 10:
            game = False
            scoreboard.game_over()

    if player.finish():
        player.start()
        scoreboard.increase_score()
        scoreboard.update_score()
        cars.level()




screen.exitonclick()
