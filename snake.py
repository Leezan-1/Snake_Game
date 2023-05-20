import turtle as t
# TODO : Creating snake body
STARTING_POSTION = ((-5, 0), (0, 0), (5, 0))
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # TODO : Create Snake Body
    def __init__(self):

        self.snake_body = []

        for i in range(3):
            self.create_snake()
            self.snake.goto(STARTING_POSTION[i])
            self.snake_body.append(self.snake)

        self.head = self.snake_body[len(self.snake_body)-1]

    def create_snake(self):
        self.snake = t.Turtle('square')
        self.snake.pu()
        self.snake.shapesize(0.6, 0.6)
        self.snake.color('white')

    # TODO : Extend snake body after eating food

    def extend(self):
        self.create_snake()
        self.snake.goto(self.head.position())
        self.snake.setheading(self.head.heading())
        self.snake_body.append(self.snake)
        self.head = self.snake_body[len(self.snake_body)-1]

    # TODO : Moving snake body

    def move(self):
        cor = self.head.position()
        self.head.fd(DISTANCE)
        for i in range(len(self.snake_body)-2, -1, -1):
            cor2 = self.snake_body[i].position()
            self.snake_body[i].goto(cor)
            cor = cor2

    # TODO : Detect Collision with Wall

    def collision(self):
        # checks collision with wall
        if (self.head.xcor() >= 275 or self.head.xcor() <= -275 or self.head.ycor() >= 275 or self.head.ycor() <= -275):
            return False
        else:  # checks collision with tail
            for body in self.snake_body[:len(self.snake_body)-2]:
                if (self.head.distance(body) <= 10):
                    return False
            return True

    # TODO : Control Snake body

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
