from turtle import Turtle

FONT = ('Courier', 24, 'normal')
SCORE = 0
ALIGNMENT = 'left'
FINISH_LINE = (0,280)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color('black')
        self.increase_score()

    def update_score(self):
        self.clear()
        self.write(f'Level:{self.score}', align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER')
