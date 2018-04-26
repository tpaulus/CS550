'''
Created on Apr 15, 2018

@author: mroch
'''

from ml_lib.learning import (DataSet, DecisionTreeLearner, NeuralNetLearner)
from std_cv import cross_validation
from random import shuffle

from copy import deepcopy

__LEARNING_METHODS = [DecisionTreeLearner, NeuralNetLearner]


def shuffle_data(dataset: DataSet):
    shuffle(dataset.examples)


def learn(dataset: DataSet):
    data = deepcopy(dataset)
    shuffle_data(data)

    for METHOD in __LEARNING_METHODS:
        print(cross_validation(METHOD, data))


def main():
    datasets = [DataSet(name="iris")]

    for dataset in datasets:
        learn(dataset)


if __name__ == '__main__':
    main()
