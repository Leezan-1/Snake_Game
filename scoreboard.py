from turtle import Turtle
FONT = ('Arial', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):       # CREATES SCOREBOARD FOR SNAKE GAME

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False):  # -> False
        # TURTLE VISIBILITY IS OFF SO THAT WE CAN WRITE ON SCORECARD
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.highscore = 0
        with open(file="./data.txt", mode='r') as data:
            self.highscore = int(data.read())
        self.scorespeed = 0.1

        self.color('white')
        self.pu()
        self.goto((0, 270))
        self.shapesize(5, 5)
        self.update_score()

    def update_score(self):     # PRINTS SCORE IN SCOREBOARD
        self.clear()
        if (self.score > self.highscore):
            self.highscore = self.score
            with open(file="./data.txt", mode='w') as data:
                data.write(f"{self.highscore}")

        self.write(
            f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def new_score(self):        # UPDATES SCORE IN SCOREBOARD
        self.scorespeed -= 0.001
        self.score += 1
        self.update_score()

    def reset(self):         # PRINTS GAME0VER PROMPT
        self.clear()
        self.score = 0
        self.scorespeed = 0.1
        self.update_score()

    def start_prompt(self):     # PRINTS STARTING PROMPT
        self.clear()
        self.write("Press Enter to START", False, ALIGNMENT, FONT)

    def game_over(self):
        self.clear()
        g_over = Turtle()
        g_over.hideturtle()
        g_over.write("Gameover!", False, ALIGNMENT, FONT)
