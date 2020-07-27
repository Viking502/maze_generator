import pygame as pg
from random import randint
from heap import Node, Heap


class Maze:

    def __init__(self, width: int = 10, height: int = 10, tileSize: int = 10):
        self.width = width
        self.height = height
        self.grid = [[{
            'horizontal': True,
            'vertical': True}
            for _ in range(width)]
            for _ in range(height)]
        self.tileSize = tileSize
        self.start_point = (0, 0)
        self.end_point = (0, 0)
        # self.vertical_edge = [[randint(0, 100) for _ in range(width - 1)] for _ in range(height)]
        # self.horizontal_edge = [[randint(0, 100) for _ in range(width)] for _ in range(height - 1)]

    def draw(self, win):
        # start point
        pg.draw.rect(win, (200, 0, 0), pg.Rect(
            (self.start_point[0] + 1) * self.tileSize, (self.start_point[1] + 1) * self.tileSize,
            self.tileSize, self.tileSize))
        # end point
        pg.draw.rect(win, (0, 200, 0), pg.Rect(
            (self.end_point[0] + 1) * self.tileSize, (self.end_point[1] + 1) * self.tileSize,
            self.tileSize, self.tileSize))
        # grid
        for y, row in enumerate(self.grid, 1):
            for x, wall in enumerate(row, 1):
                # vertical wall
                color = (40, 40, 40)
                if wall['horizontal']:
                    color = (220, 220, 200)
                pg.draw.line(win, color, [x * self.tileSize, y * self.tileSize],
                             [(x + 1) * self.tileSize, y * self.tileSize])
                # vertical wall
                color = (40, 40, 40)
                if wall['vertical']:
                    color = (220, 220, 200)
                pg.draw.line(win, color, [x * self.tileSize, y * self.tileSize],
                             [x * self.tileSize, (y + 1) * self.tileSize])
                # outline
                height = self.height + 1
                width = self.width + 1
                # vertical
                pg.draw.line(win, (220, 220, 200), [width * self.tileSize, self.tileSize],
                             [width * self.tileSize, height * self.tileSize])
                # horizontal
                pg.draw.line(win, (220, 220, 200), [self.tileSize, height * self.tileSize],
                             [width * self.tileSize, height * self.tileSize])

    def build_walls(self):
        self.grid = [[{
            'horizontal': True,
            'vertical': True}
            for _ in range(self.width)]
            for _ in range(self.height)]

    @staticmethod
    def rand_cost():
        return randint(0, 1000)

    def prime_mst(self):
        visited_cell = [[False for _ in row] for row in self.grid]
        vertices_num = self.width * self.height

        edge_que = Heap()
        edge_que.insert(Node(self.start_point, (1, 0), self.rand_cost()))
        x, y = 0, 0
        while vertices_num > 0:
            edge = edge_que.pop()
            x, y = edge.pos[0] + edge.dir[0], edge.pos[1] + edge.dir[1]
            e_x, e_y = edge.pos[0] + max(0, edge.dir[0]), edge.pos[1] + max(0, edge.dir[1])
            if not visited_cell[y][x]:
                visited_cell[y][x] = True
                vertices_num -= 1
                if edge.dir[0] == 0:
                    self.grid[e_y][e_x]['horizontal'] = False
                else:
                    self.grid[e_y][e_x]['vertical'] = False
                for step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x, next_y = x + step[0], y + step[1]
                    if 0 <= next_x < self.width and 0 <= next_y < self.height\
                            and not visited_cell[next_y][next_x]:
                        edge_que.insert(Node((x, y), step, self.rand_cost()))
        self.end_point = (x, y)


if __name__ == '__main__':

    maze = Maze(20, 20, 40)

    windowSize = [1200, 900]
    window = pg.display.set_mode(windowSize)
    pg.display.set_caption('maze generator')
    clock = pg.time.Clock()

    # prepare initial maze
    maze.prime_mst()

    runFlag = True
    while runFlag:
        clock.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runFlag = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    maze.build_walls()
                    maze.prime_mst()

        window.fill((0, 0, 0))
        maze.draw(window)

        pg.display.update()