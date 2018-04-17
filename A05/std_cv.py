
from statistics import (stdev, mean)
from ml_lib.learning import (err_ratio, train_and_test)


def cross_validation(learner, dataset, k=10):
    """Perform k-fold cross_validation
    Run k trials where each trial has a different (k-1)/k percentage
    of the data as training data and 1/k as test data.
    
    Returns tuple (mean_err, std_err, fold_errors, models)
    """

    raise NotImplemented
