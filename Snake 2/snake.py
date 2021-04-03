class BodyPart():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def draw(self, screen):


class Snake():
    def __init__(self, row, col):
        self.head = BodyPart(row, col)
        self.xspeed = 0
        self.yspeed = 0
        self.body = []

    def total_body(self):
        return len(self.body)

    def update(self):
        if self.total_body() == 0:
            pass

        if self.total_body() == 1:
            self.body[0].row = self.head.row
            self.body[0].col = self.head.col

        if self.total_body() > 1:
            for i in range(self.total_body()-1, 0, -1):
                try:
                    self.body[i].row = self.body[i-1].row
                    self.body[i].col = self.body[i-1].col
                except:
                    pass

        self.head.row += self.yspeed
        self.head.col += self.xspeed

    def draw(self, screen):
