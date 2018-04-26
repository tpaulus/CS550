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
    data = deepcopy(dataset)
    shuffle_data(data)

    print(cross_validation(DecisionTreeLearner, data))
    # Neural Net Needs the Numbers like the Cookie Monster needs Cookies
    data.classes_to_numbers()
    print(cross_validation(NeuralNetLearner, data))


def main():
    datasets = [DataSet(name="iris"), DataSet(name="orings")]

    for dataset in datasets:
        learn(dataset)


if __name__ == '__main__':
    main()
