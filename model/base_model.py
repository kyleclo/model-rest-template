"""

Base model

"""

from collections import defaultdict

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class Model(object):
    def __init__(self, *args, **kwargs):
        self.recent_config = None
        self.recent_params = None
        self.experiment = Experiment()

    def train(self, X, y):
        pass

    def predict(self, X, y):
        pass

    def _train(self, X, y):
        raise NotImplementedError

    def _predict(self, X):
        raise NotImplementedError


class Experiment(object):
    def __init__(self):
        self.history = defaultdict()

    def add_config(self, **kwargs):
        self.history[]
