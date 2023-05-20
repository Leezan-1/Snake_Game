from turtle import Turtle
import random


class Food(Turtle):
    # creating food shape and design
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.pu()
        self.color('blue')
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.food_refresh()

    # food position
    def food_position(self):
        xcor = random.randint(-270, 270)
        ycor = random.randint(-270, 270)
        return (xcor, ycor)

    # creates food
    def food_refresh(self, snake_body_list=[]):
        self.setposition(self.food_position())
        # if snake_body_list != []:
        for body in snake_body_list:
            while (body.position() == self.position() and body.distance(self) < 10):
                self.setposition(self.food_position())
                # While loop prevents food summoning into snake's body for some extent (not perfect)
                # game crashes if game is won (hehe!)
