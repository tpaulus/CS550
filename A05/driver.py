'''
Created on Apr 15, 2018

@author: mroch
'''

from ml_lib.learning import (DataSet, DecisionTreeLearner, NeuralNetLearner)
from std_cv import cross_validation
from random import shuffle

from copy import deepcopy


def shuffle_data(dataset: DataSet):
    shuffle(dataset.examples)


def learn(dataset: DataSet):
    raise NotImplemented


def main():
    raise NotImplemented


if __name__ == '__main__':
    main()
