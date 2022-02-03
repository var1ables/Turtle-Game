from turtle import Turtle
import random

CARS = ['red', 'orange', 'yellow', 'blue', 'purple', 'pink']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def placement(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(CARS))
            random_y = random.randint(-240, 260)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level(self):
        self.car_speed += MOVE_INCREMENT

