from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):       # CREATES SCOREBOARD FOR SNAKE GAME

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False):  # -> False
        # TURTLE VISIBILITY IS OFF SO THAT WE CAN WRITE ON SCORECARD
        super().__init__(shape, undobuffersize, visible)
        self.color('white')
        self.pu()
        self.goto((0, 270))
        self.shapesize(5, 5)
        self.score = 0
        self.update_score()

    def update_score(self):     # PRINTS SCORE IN SCOREBOARD
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def new_score(self):        # UPDATES SCORE IN SCOREBOARD
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):         # PRINTS GAME0VER PROMPT
        self.goto(0, 0)
        self.write("Game Over", False, ALIGNMENT, FONT)

    def start_prompt(self):     # PRINTS STARTING PROMPT
        self.clear()
        self.write("Press Enter to START", False, ALIGNMENT, FONT)
