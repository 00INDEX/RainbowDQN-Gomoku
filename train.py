from utils import Competitor, Game
from model import Model
from dataclasses import dataclass
import numpy as np
from typing import Tuple, Union
import torch

epoch = 100
batch_size = 32
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = Model()
game = Game()
buffers = []
competitor = Competitor(engine_file=r'./engines/pbrain-Yixin2018.exe')

gamma = 0.5  # 探索欲望
lr = 2e-5

np.random.seed(42)


@dataclass
class Buffer:
    state: np.ndarray
    action: Tuple[int, int]
    reward: float
    next_state: np.ndarray
    done: bool


def get_action() -> Tuple[int, int]:
    if np.random.random() >= gamma:
        possible_action = np.where(game.board == 0)
        random_choice = np.random.choice(len(possible_action[0]))
        return possible_action[0][random_choice], possible_action[1][random_choice]
    else:
        action = model(game.board)




def main():
    for i in range(100):

        state = game.board
        action = competitor.get_action(state)
        reward, next_state, done = game.step(action)
        buffer = Buffer(state, action, reward, next_state, done)
        buffers.append(buffer)
        if done:
            game.reset()


if __name__ == '__main__':
    main()
