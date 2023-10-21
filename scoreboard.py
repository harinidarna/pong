from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def update_score(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, "center", ("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, "center", ("courier", 80, "normal"))

    def left_score(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.clear()
        self.r_score += 1
        self.update_score()