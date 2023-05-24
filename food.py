from turtle import Turtle
import random


class Food(Turtle):
    # CREATING FOOD'S SHAPE AND SIZE
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.pu()
        self.color('blue')
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.food_refresh()

    def food_position(self):        # food position
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        return (x_cor, y_cor)

    def food_refresh(self, snake_body_list=[]):        # creates food in new position
        self.setposition(self.food_position())
        for body in snake_body_list:
            while (body.position() == self.position() and body.distance(self) < 20):
                self.setposition(self.food_position())
                # this loop prevents food summoning into snake's body for some extent (not perfect)
                # game crashes if game is won (hehe!)
