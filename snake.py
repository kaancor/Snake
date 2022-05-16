from turtle import Turtle
ALL_TURTLE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coord in ALL_TURTLE_POSITIONS:
            m_turtle = Turtle(shape='square')
            m_turtle.color('white')
            m_turtle.penup()
            m_turtle.goto(coord)
            self.segments.append(m_turtle)

    def move(self):
        for turtle in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turtle - 1].xcor()
            new_y = self.segments[turtle - 1].ycor()
            self.segments[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)





