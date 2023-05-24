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
        self.head = None
        self.create_snake()

    def create_snake(self):
        for i in range(3):      # SETS SNAKES BODY IN POSITION
            snake = self.snake_struct()
            snake.goto(STARTING_POSTION[i])
            self.snake_body.append(snake)

        # head is the last element in list
        self.head = self.snake_body[len(self.snake_body)-1]

    def snake_struct(self):
        snake = t.Turtle('square')
        snake.pu()
        snake.shapesize(0.6, 0.6)
        snake.color('white')
        return snake

    def extend(self):       # EXTENDS SNAKE BODY AFTER EATING FOOD
        snake = self.snake_struct()
        snake.goto(self.head.position())
        snake.setheading(self.head.heading())
        self.snake_body.append(snake)

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
            return True

        else:  # CHECKS COLLSION WITH THE TAIL
            for body in self.snake_body[:len(self.snake_body)-2]:
                if (self.head.distance(body) <= 10):
                    return True
            return False

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

    def reset(self):
        self.score = 0
        for body in self.snake_body:
            body.goto(1000, 1000)
            body.hideturtle()
        self.snake_body.clear()
        self.create_snake()
