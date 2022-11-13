import re
import time
from typing import Tuple
from subprocess import Popen, PIPE


class Competitor:
    def __init__(self, engine_file: str):
        self.proc = Popen(args=f'wine {engine_file}', shell=True, encoding='utf-8', stdin=PIPE, stdout=PIPE,
                          stderr=PIPE)

    def send(self, command: str, pattern: str):
        self.proc.stdin.write(command + '\n')
        self.proc.stdin.flush()
        while True:
            line = self.proc.stdout.readline()
            info = re.findall(pattern, line, re.M | re.I)
            if info:
                return info[0]
            time.sleep(0.5)

    def start(self, size: int = 10) -> None:
        """
        开始游戏
        :param size: 棋盘大小
        :return:
        """
        self.send(f'START {size}', pattern=r'OK')

    def begin(self) -> Tuple[int]:
        """
        命令电脑先下
        :return: 电脑落点的 x y 坐标
        """
        return self.send(f'BEGIN', pattern='([0-9]+),([0-9]+)')

    def turn(self, x, y) -> Tuple[int]:
        """
        落子
        :param x: 要落子的 x 坐标
        :param y: 要落子的 y 坐标
        :return: 电脑落点的 x y 坐标
        """
        return self.send(f'TURN {x} {y}', pattern='([0-9]+),([0-9]+)')

    def restart(self) -> None:
        """
        以当前的棋盘大小重新开始游戏
        :return:
        """
        self.send(f'RESTART', pattern=r'OK')


if __name__ == '__main__':
    competitor = Competitor('../engines/pbrain-Yixin2018.exe')
    competitor.start(10)
    competitor.begin()

