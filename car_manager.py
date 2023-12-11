import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        random_color = random.choice(COLORS)
        random_locationY = random.randint(-230, 230)
        self.penup()
        self.color(random_color)
        self.goto(-320, random_locationY)
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(0)

    def move(self):
        self.forward(MOVE_INCREMENT)
