"""

Implemented models

"""

import numpy as np
from sklearn.linear_model import LinearRegression

from model.base_model import Model

class LinearRegression(Model):

    def __init__(self, *args, **kwargs):
        self.model = LinearRegression()
        super(LinearRegression, self).__init__(*args, **kwargs)

    def _train(self, X, y):
        dim_target = y.shape[1]
        dim_input = X.shape[1]

        self.experiment.add_config(dim_target, dim_input)



        param = np.matmul(np.linalg.inv(np.matmul(X.transpose(), X)),
                          np.matmul(X.transpose(), y))

    def _predict(self, X):