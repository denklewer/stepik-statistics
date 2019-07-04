import numpy as np
import pandas as pd
from descriptive_statistics import *
import math

def stratified_avg(weights, avgs):
    weighted_list = [weight*avg for (weight,avg) in zip(weights, avgs)]
    return np.sum(weighted_list)

def stratified_variance(weights, avgs, variances):
    expected = stratified_avg(weights, avgs)
    weighted_list = [weight*(variance + (avg-expected)**2) for (weight,avg, variance) in zip(weights, avgs, variances)]
    return np.sum(weighted_list)


def get_sample_counts(n, weights, variances):
    weighted_sum = np.sum(weight*math.sqrt(variance) for (weight,variance) in zip(weights, variances))
    weighted_list = [n*weight* math.sqrt(variance)/weighted_sum for (weight,variance) in zip(weights, variances)]
    weighted_int_list = [round(x) for x in weighted_list]
    return weighted_int_list