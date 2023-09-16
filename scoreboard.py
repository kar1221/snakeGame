from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self._score = 0
        self._title = Turtle()
        self._title.penup()
        self._title.hideturtle()
        self._title.color("white")
        self._title.goto(0, 270)

        # Highscore input
        try:
            with open("Highscore.txt", "r") as text:
                self.highScore = int(text.readline())
        except FileNotFoundError:
            with open("Highscore.txt", "w") as text:
                text.write("0")
            self.highScore = 0


        self.updateScoreboard()

    def updateScoreboard(self):
        self._title.clear()

        self._title.write(f"Score: {self._score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def addScore(self):
        self._score += 1
        self.updateScoreboard()

    def reset(self):
        if self._score > self.highScore:
            self.highScore = self._score
        self._score = 0
        self.updateScoreboard()
        with open("Highscore.txt", "w") as file:
            file.write(str(self.highScore))

    # def gameOver(self):
    #     self._title.goto(0, 0)
    #     self._title.write(f"Game Over!", align=ALIGNMENT, font=FONT)


