from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.pu()
        self.color('blue')
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.food_refresh()

    # creates food
    def food_refresh(self):
        xcor = random.randint(-270, 270)
        ycor = random.randint(-270, 270)
        self.setposition((xcor, ycor))
