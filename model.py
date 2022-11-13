import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import flatten, from_numpy
import numpy as np


class Model(nn.Module):
    def __init__(self, size: int = 10):
        super(Model, self).__init__()
        self.size = size
        self.model = nn.Sequential(
            nn.Linear(self.size ** 2, self.size ** 2),
            nn.ReLU(),
            nn.Linear(self.size ** 2, self.size ** 2),
            nn.ReLU(),
            nn.Linear(self.size ** 2, self.size ** 2)
        )

    def forward(self, x):
        x = flatten(x).float()
        x = self.model(x) - torch.abs(x * 10.0e10)
        pos = torch.argmax(x)
        return torch.div(pos + 1, self.size, rounding_mode='floor'), (pos + 1) % self.size - 1 + self.size if (pos + 1) % self.size - 1 < 0 else (pos + 1) % self.size - 1


if __name__ == '__main__':
    model = Model()
    x = from_numpy(np.zeros(shape=(10, 10), dtype=np.int8))
    y = model(x)
    a = int(y[0])
    b = int(y[1])
    print(y)

