import turtle as t

# VARIABLES
STARTING_POSTION = ((-5, 0), (0, 0), (5, 0))
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):     # CREATEES SNAKE BODY

        self.snake_body = []

        for i in range(3):      # SETS SNAKES BODY IN POSITION
            self.create_snake()
            self.snake.goto(STARTING_POSTION[i])
            self.snake_body.append(self.snake)

        # head is the last element in list
        self.head = self.snake_body[len(self.snake_body)-1]

    def create_snake(self):
        self.snake = t.Turtle('square')
        self.snake.pu()
        self.snake.shapesize(0.6, 0.6)
        self.snake.color('white')

    def extend(self):       # EXTENDS SNAKE BODY AFTER EATING FOOD
        self.create_snake()
        self.snake.goto(self.head.position())
        self.snake.setheading(self.head.heading())
        self.snake_body.append(self.snake)
        self.head = self.snake_body[len(self.snake_body)-1]

    def move(self):         # MOVES SNAKE BODY CONTINUOUSLY
        cor = self.head.position()
        self.head.fd(DISTANCE)
        for i in range(len(self.snake_body)-2, -1, -1):
            cor2 = self.snake_body[i].position()
            self.snake_body[i].goto(cor)
            cor = cor2

    def collision(self):        # DETECTS COLLISION WITH THE WALL OR TAIL

        # CHECKS COLLLISION WITH THE WALL
        if (self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 280 or self.head.ycor() <= -300):
            return False

        else:  # CHECKS COLLSION WITH THE TAIL
            for body in self.snake_body[:len(self.snake_body)-2]:
                if (self.head.distance(body) <= 10):
                    return False
            return True

    # CONTROLS SNAKE BODY ON PRESSING BUTTONS
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
