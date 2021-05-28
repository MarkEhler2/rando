from math import sqrt

test_list = [1, 2, 3]


class GetStats(object):
    def __init__(self, input_list):
        self._input_list = input_list
        self._len = len(self._input_list)
        self._min = min(self._input_list)
        self._max = max(self._input_list)

    def get_mean(self):
        sum = 0
        for i in self._input_list:
            sum += i
        mean = sum / self._len
        return mean  # sum is computed but not yet needed

    def get_std(self):
        dist_from_mean = 0
        for i in self._input_list:
            dist_from_mean += (i-self.get_mean())**2
        std = sqrt(dist_from_mean / self._len)
        return std

    pass
