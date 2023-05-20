from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        # TURTLE VISIBILITY IS OFF SO THAT WE CAN WRITE ON SCORECARD
        super().__init__(shape, undobuffersize, visible)
        self.color('white')
        self.pu()
        self.goto((0, 270))
        self.shapesize(5, 5)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
