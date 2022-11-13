import numpy as np
from typing import Union
import torch


class Game:
    board = np.zeros(shape=(10, 10), dtype=np.int8)
    size = 10

    def __init__(self, size: int = 10):
        self.size = size
        self.board = np.zeros(shape=(size, size), dtype=np.int8)

    def step(self, x: int, y: int, character: Union[-1, 1] = 1) -> None:
        """
        走一步祺
        :param x: 落子的 x 坐标
        :param y: 落子的 y 坐标
        :param character: 角色，1 或者 2
        :return:
        """
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise Exception("无法在棋盘外落子")
        elif self.board[x, y] != 0:
            raise Exception("该位置已有棋子")
        elif character not in [-1, 1]:
            raise Exception("byd多P是吧")
        else:
            self.board[x][y] = character

    def restart(self):
        self.board = np.zeros(shape=(self.size, self.size), dtype=np.int8)

    def check_win(self, x: int, y: int) -> int:
        """
        检查下完这一步之后是否出现胜负
        :param x: 落子的 x 坐标
        :param y: 落子的 y 坐标
        :return: 胜利的一方，如果是 0 说明没分出胜负
        """
        c1, c2 = 0, 0
        # 横向
        while x + c1 < self.size and self.board[x + c1][y] == self.board[x][y]:
            c1 += 1
        while x - c2 >= 0 and self.board[x - c2][y] == self.board[x][y]:
            c2 += 1
        if c1 + c2 >= 4:
            return self.board[x][y]
        c1, c2 = 0, 0
        # 纵向
        while y + c1 < self.size and self.board[x][y + c1] == self.board[x][y]:
            c1 += 1
        while y - c2 >= 0 and self.board[x][y - c2] == self.board[x][y]:
            c2 += 1
        if c1 + c2 >= 4:
            return self.board[x][y]
        c1, c2 = 0, 0
        # 右上到左下
        while x + c1 < self.size and y + c1 < self.size and self.board[x + c1][y + c1] == self.board[x][y]:
            c1 += 1
        while x - c2 >= 0 and y - c2 >= 0 and self.board[x - c2][y - c2] == self.board[x][y]:
            c2 += 1
        if c1 + c2 >= 4:
            return self.board[x][y]
        c1, c2 = 0, 0
        # 左上到右下
        while x + c1 < self.size and y - c1 >= 0 and self.board[x + c1][y - c1] == self.board[x][y]:
            c1 += 1
        while x - c2 >= 0 and y + c2 < self.size and self.board[x - c2][y + c2] == self.board[x][y]:
            c2 += 1
        if c1 + c2 >= 4:
            return self.board[x][y]
        return 0


