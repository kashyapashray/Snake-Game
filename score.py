from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.ht()
        self.ate = 0
        file = open("data.txt")
        self.high_score = int(file.read())
        file.close()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.ate} High Score {self.high_score}", False, "center")

    def scored(self):
        self.ate +=1
        self.show_score()

    def reset(self):
        if self.ate > self.high_score:
            self.high_score = self.ate
            file = open("data.txt", mode="w")
            file.write(str(self.high_score))
            file.close()
        self.ate = 0
        self.show_score()


