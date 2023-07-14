from turtle import Turtle
UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180


class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segs = []
        self.create_snake()

    def add_seg(self, posi):
        s1 = Turtle(shape="square")
        s1.penup()
        s1.goto(posi)
        s1.color("white")
        self.segs.append(s1)

    def create_snake(self):
        for pos in self.positions:
            self.add_seg(pos)

    def extend(self):
        self.add_seg(self.segs[-1].position())

    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            new_x = self.segs[i - 1].xcor()
            new_y = self.segs[i - 1].ycor()
            self.segs[i].goto(new_x, new_y)
        self.segs[0].fd(20)

    def up(self):
        if self.segs[0].heading() != DOWN:
            self.segs[0].setheading(UP)

    def down(self):
        if self.segs[0].heading() != UP:
            self.segs[0].setheading(DOWN)

    def left(self):
        if self.segs[0].heading() != RIGHT:
            self.segs[0].setheading(LEFT)

    def right(self):
        if self.segs[0].heading() != LEFT:
            self.segs[0].setheading(RIGHT)