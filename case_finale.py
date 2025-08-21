import pyglet

largeur = 20


class Case:
    def __init__(self, x, y, largeur=20):
        self.x = x
        self.y = y
        self.largeur = largeur

    def draw(self, decalage=0):
        bordure = pyglet.shapes.Rectangle(
            x=self.x,
            y=self.y + decalage,
            width=(self.largeur),
            height=(self.largeur),
            color=(150, 150, 150),
        )
        rectangle = pyglet.shapes.Rectangle(
            x=self.x + 1,
            y=self.y + 1 + decalage,
            width=(self.largeur - 2),
            height=(self.largeur - 2),
            color=(255, 255, 255),
        )
        bordure.draw()
        rectangle.draw()


class Polyo:
    def __init__(self,):
        self.cases = []

    def draw(self, decalage=0):
        for case in self.cases:
            case.draw(decalage=decalage)
