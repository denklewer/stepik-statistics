import numpy as np
import pandas as pd

def get_order_statistic(arr, n):
    """
    Get n-th smallest element in array. 1-based.
    :param arr: input array of values
    :param n: number of element which should be selected
    :return:
    """
    partitioned = np.partition(arr, n-1)
    return partitioned[n-1]


def get_statiscic_series(arr):
    uniques, counts = np.unique(arr, return_counts=True)
    freqs = counts/len(arr)
    cum_sums = np.cumsum(freqs)
    result = {idx: (cnt, freq, c_sum) for idx, cnt, freq, c_sum in zip(uniques, counts, freqs, cum_sums)}
    return result


def get_statistic_series_pandas(arr, bins=0):
    if bins != 0:
        counts = pd.Series(arr, name="counts").value_counts()
    else:
        counts = pd.Series(arr, name="counts").value_counts(bins=bins)

    freqs = pd.Series(arr, name="freqs").value_counts(normalize=True)
    cumsums = freqs.cumsum().rename("cumsum")
    result = pd.concat([counts, freqs, cumsums], axis=1 )
    result.index.names = ["value"]
    return result


def get_histogram(arr):
    histogram = np.histogram(arr, bins=8, range=(15, 21))
    return histogram[0]/len(arr)

