from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, move_distance=20):
        self._moveDistance = move_distance
        self._cor = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for p in self._cor:
            self.add_segment(p)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s - 1].xcor()
            new_y = self.segments[s - 1].ycor()
            self.segments[s].goto(new_x, new_y)

        self.head.forward(self._moveDistance)

    def move_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def reset(self):
        for x in self.segments:
            x.goto(1000, 1000)
        self.segments.clear()
        for p in self._cor:
            self.add_segment(p)
        self.head = self.segments[0]


