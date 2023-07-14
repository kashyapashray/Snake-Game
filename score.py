from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.ht()
        self.ate = 0
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.ate}", False, "center")

    def scored(self):
        self.clear()
        self.ate +=1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center")


