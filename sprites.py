import pygame
import os
import config


class BaseSprite(pygame.sprite.Sprite):
    images = dict()

    def __init__(self, row, col, file_name, transparent_color=None):
        pygame.sprite.Sprite.__init__(self)
        if file_name in BaseSprite.images:
            self.image = BaseSprite.images[file_name]
        else:
            self.image = pygame.image.load(os.path.join(config.IMG_FOLDER, file_name)).convert()
            self.image = pygame.transform.scale(self.image, (config.TILE_SIZE, config.TILE_SIZE))
            BaseSprite.images[file_name] = self.image
        # making the image transparent (if needed)
        if transparent_color:
            self.image.set_colorkey(transparent_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (col * config.TILE_SIZE, row * config.TILE_SIZE)
        self.row = row
        self.col = col


class Agent(BaseSprite):
    def __init__(self, row, col, file_name):
        super(Agent, self).__init__(row, col, file_name, config.DARK_GREEN)

    def move_towards(self, row, col):
        row = row - self.row
        col = col - self.col
        self.rect.x += col
        self.rect.y += row

    def place_to(self, row, col):
        self.row = row
        self.col = col
        self.rect.x = col * config.TILE_SIZE
        self.rect.y = row * config.TILE_SIZE

    # game_map - list of lists of elements of type Tile
    # goal - (row, col)
    # return value - list of elements of type Tile
    def get_agent_path(self, game_map, goal):
        pass


class ExampleAgent(Agent):
    def __init__(self, row, col, file_name):
        super().__init__(row, col, file_name)

    def get_agent_path(self, game_map, goal):
        path = [game_map[self.row][self.col]]

        row = self.row
        col = self.col
        while True:
            if row != goal[0]:
                row = row + 1 if row < goal[0] else row - 1
            elif col != goal[1]:
                col = col + 1 if col < goal[1] else col - 1
            else:
                break
            path.append(game_map[row][col])
        return path


class Aki(Agent):
    def __init__(self, row, col, file_name):
        super().__init__(row, col, file_name)

    def __get_path_to_root(self, root_row, root_col, start_row, start_col, current_father_son_relations) -> list:

        path_to_root = [(start_row, start_col)]

        while (start_row, start_col) != (root_row, root_col):

            for father_son in current_father_son_relations:
                father, son = father_son

                if son == (start_row, start_col):
                    start_row, start_col = father
                    break

            path_to_root.append((start_row, start_col))

        return path_to_root

    def __get_valid_neighbours(self, root_row, root_col, game_map, current_row, current_col, current_father_son_relations) -> list:

        # edges of the board
        top_edge = 0
        right_edge = len(game_map[current_row]) - 1
        bottom_edge = len(game_map) - 1
        left_edge = 0

        print(top_edge, right_edge, bottom_edge, left_edge)

        # prepare next values for determining what is the next expanding field
        # next_row = current_row  # dummy value
        # next_col = current_col  # dummy value
        # next_cost = game_map[current_row][current_col]  # dummy value

        path_to_root = self.__get_path_to_root(root_row, root_col, current_row, current_col, current_father_son_relations)
        print(path_to_root)

        valid_neighbours = []

        if top_edge < current_row:
            # north direction
            print(game_map[current_row - 1][current_col])
            next_row = current_row - 1
            next_col = current_col
            next_cost = game_map[next_row][next_col].cost()

            if (next_row, next_col) not in path_to_root:
                valid_neighbours.append((next_row, next_col, next_cost, 4))

        if current_col < right_edge:
            # east direction
            print(game_map[current_row][current_col + 1])
            next_row = current_row
            next_col = current_col + 1
            next_cost = game_map[next_row][next_col].cost()

            if (next_row, next_col) not in path_to_root:
                valid_neighbours.append((next_row, next_col, next_cost, 3))

        if current_row < bottom_edge:
            # south direction
            print(game_map[current_row + 1][current_col])
            next_row = current_row + 1
            next_col = current_col
            next_cost = game_map[next_row][next_col].cost()

            if (next_row, next_col) not in path_to_root:
                valid_neighbours.append((next_row, next_col, next_cost, 2))

        if left_edge < current_col:
            # west direction
            print(game_map[current_row][current_col - 1])
            next_row = current_row
            next_col = current_col - 1
            next_cost = game_map[next_row][next_col].cost()

            if (next_row, next_col) not in path_to_root:
                valid_neighbours.append((next_row, next_col, next_cost, 1))

        return valid_neighbours

    def __insert_neighbours_in_appropriate_order(self, neighbours, list_for_expanding):

        neighbours.sort(key=lambda elem: (elem[2], -elem[3]))

        neighbours.reverse()

        for neighbour in neighbours:
            list_for_expanding.append((neighbour[0], neighbour[1]))

    def get_agent_path(self, game_map, goal):

        # path1 = [game_map[self.row][self.col]]
        print(goal)
        path = []

        row = self.row
        col = self.col

        list_for_expanding = []
        father_son_relations = []

        while True:
            print()
            print("expanded", row, col)

            neighbours = self.__get_valid_neighbours(self.row, self.col, game_map, row, col, father_son_relations)

            self.__insert_neighbours_in_appropriate_order(neighbours, list_for_expanding)

            next_row, next_col = list_for_expanding.pop()

            print("go to", next_row, next_col)

            father_son_relations.append([(row, col), (next_row, next_col)])

            if (next_row, next_col) == goal:
                final_row = next_row
                final_col = next_col
                break

            row = next_row
            col = next_col

            # if row != goal[0]:
            #     row = row + 1 if row < goal[0] else row - 1
            # elif col != goal[1]:
            #     col = col + 1 if col < goal[1] else col - 1
            # else:
            #     break

            # path1.append(game_map[row][col])
        # return path1
        path_tuples = self.__get_path_to_root(self.row, self.col, final_row, final_col, father_son_relations)
        path_tuples.reverse()

        path_fields = []

        for row_col in path_tuples:
            path_fields.append(game_map[row_col[0]][row_col[1]])

        return path_fields



class Tile(BaseSprite):
    def __init__(self, row, col, file_name):
        super(Tile, self).__init__(row, col, file_name)

    def position(self):
        return self.row, self.col

    def cost(self):
        pass

    def kind(self):
        pass

    def __str__(self) -> str:
        pass


class Stone(Tile):
    def __init__(self, row, col):
        super().__init__(row, col, 'stone.png')

    def cost(self):
        return 1000

    def kind(self):
        return 's'

    def __str__(self) -> str:
        return "Stone [" + str(self.cost()) + "] (" + str(self.row) + "," + str(self.col) + ")"


class Water(Tile):
    def __init__(self, row, col):
        super().__init__(row, col, 'water.png')

    def cost(self):
        return 500

    def kind(self):
        return 'w'

    def __str__(self) -> str:
        return "Water [" + str(self.cost()) + "] (" + str(self.row) + "," + str(self.col) + ")"


class Road(Tile):
    def __init__(self, row, col):
        super().__init__(row, col, 'road.png')

    def cost(self):
        return 2

    def kind(self):
        return 'r'

    def __str__(self) -> str:
        return "Road [" + str(self.cost()) + "] (" + str(self.row) + "," + str(self.col) + ")"

class Grass(Tile):
    def __init__(self, row, col):
        super().__init__(row, col, 'grass.png')

    def cost(self):
        return 3

    def kind(self):
        return 'g'

    def __str__(self) -> str:
        return "Grass [" + str(self.cost()) + "] (" + str(self.row) + "," + str(self.col) + ")"


class Mud(Tile):
    def __init__(self, row, col):
        super().__init__(row, col, 'mud.png')

    def cost(self):
        return 5

    def kind(self):
        return 'm'

    def __str__(self) -> str:
        return "Mud [" + str(self.cost()) + "] (" + str(self.row) + "," + str(self.col) + ")"


class Dune(Tile):
    def __init__(self, row, col):
        super().__init__(row, col, 'dune.png')

    def cost(self):
        return 7

    def kind(self):
        return 's'

    def __str__(self) -> str:
        return "Dune [" + str(self.cost()) + "] (" + str(self.row) + "," + str(self.col) + ")"


class Goal(BaseSprite):
    def __init__(self, row, col):
        super().__init__(row, col, 'x.png', config.DARK_GREEN)


class Trail(BaseSprite):
    def __init__(self, row, col, num):
        super().__init__(row, col, 'trail.png', config.DARK_GREEN)
        self.num = num

    def draw(self, screen):
        text = config.GAME_FONT.render(f'{self.num}', True, config.WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
