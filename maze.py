import pygame as pg
from random import randint
from heap import Node, Heap

class Maze:

    def __init__(self, width=10, height=10, tileSize=10):
        self.width = width
        self.height = height
        self.grid = [[{'horizontal': [True, randint(0, 100)], 'vertical': [True, randint(0, 100)]} for _ in range(width)] for _ in range(height)]
        self.tileSize = tileSize
        self.vertical_edge = [[randint(0, 100) for _ in range(width - 1)] for _ in range(height)]
        self.horizontal_edge = [[randint(0, 100) for _ in range(width)] for _ in range(height - 1)]

    def draw(self, window):
        for y, row in enumerate(self.grid, 1):
            for x, wall in enumerate(row, 1):
                # vertical wall
                color = (40, 40, 40)
                if wall['horizontal'][0]:
                    color = (220, 220, 200)
                pg.draw.line(window, color, [x * self.tileSize, y * self.tileSize],
                             [(x + 1) * self.tileSize, y * self.tileSize])
                # vertical wall
                color = (40, 40, 40)
                if wall['vertical'][0]:
                    color = (220, 220, 200)
                pg.draw.line(window, color, [x * self.tileSize, y * self.tileSize],
                             [x * self.tileSize, (y + 1) * self.tileSize])
                # outline
                height = self.height + 1
                width = self.width + 1
                pg.draw.line(window, (220, 220, 200), [width * self.tileSize, self.tileSize],
                             [width * self.tileSize, height * self.tileSize])
                pg.draw.line(window, (220, 220, 200), [self.tileSize, height * self.tileSize],
                             [width * self.tileSize, height * self.tileSize])

    def prime_mst(self):
        pass


if __name__ == '__main__':

    maze = Maze(20, 20, 40)

    windowSize = [1200, 900]
    window = pg.display.set_mode(windowSize)
    clock = pg.time.Clock()

    runFlag = True

    while runFlag:
        clock.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runFlag = False

        window.fill((0, 0, 0))
        maze.draw(window)

        pg.display.update()
