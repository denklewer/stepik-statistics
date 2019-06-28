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


def get_avg(arr):
    return np.average(arr)


def get_variance(arr):

    avg = get_avg(arr)
    n = len(arr)
    new_arr = [(x - avg)**2 for x in arr]
    sum = np.sum(new_arr)/n
    return sum

def get_central_moment(arr, r):

    avg = get_avg(arr)
    n = len(arr)
    new_arr = [(x - avg)**r/n for x in arr]
    sum = np.sum(new_arr)
    return sum


def get_moment(arr, r):

    n = len(arr)
    new_arr = [(x)**r/n for x in arr]
    sum = np.sum(new_arr)
    return sum

def Kurtosis(arr):
    central_momentum = get_central_moment(arr, 4)
    std = np.sqrt(get_variance(arr))

    return central_momentum/(std**4) -3

def Skewness(arr):
    central_momentum = get_central_moment(arr, 3)
    std = np.sqrt(get_variance(arr))

    return central_momentum/(std**3)


def get_quantile(arr, p):
    n = len(arr)
    i = int(p*n)
    partitioned = np.partition(arr, i)
    return partitioned[i]

def get_mean(arr):
    arr = np.sort(arr)
    n = len(arr)
    if n % 2 == 0:
        k = n//2
        result = (arr[k-1]+arr[k])/2
    else:
        k = (n-1)//2
        result = arr[k]
    return result

def correlation_coeff(arr):
    list1 = [x for (x,y) in arr]
    list2 = [y for (x,y) in arr]
    avg1 = get_avg(list1)
    avg2 = get_avg(list2)
    var1= get_variance(list1)
    var2 = get_variance(list2)

    mutual_shift = [x*y for (x,y) in arr]
    mutual_shift = np.sum(mutual_shift)
    result = mutual_shift/len(arr) - avg1*avg2
    result = result / (np.sqrt(var1)*np.sqrt(var2))

    return result


print(get_avg([23, 24, 21, 23, 22, 21, 20, 21, 28, 25, 22, 22, 25, 21 ]))
print(get_variance([23, 24, 21, 23, 22, 21, 20, 21, 28, 25, 22, 22, 25, 21]))
print(get_mean([23, 24, 21, 23, 22, 21, 20, 21, 28, 25, 22, 22, 25, 21 ]))
print(get_quantile([23, 24, 21, 23, 22, 21, 20, 21, 28, 25, 22, 22, 25, 21 ],0.25))
print(get_quantile([23, 24, 21, 23, 22, 21, 20, 21, 28, 25, 22, 22, 25, 21 ],0.75))

print(correlation_coeff([(170, 66), (182, 74),  (183, 77),  (180, 72), (175, 67), (181, 77), (187, 76), (181, 77), (178, 72), (187, 76)]))