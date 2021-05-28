import numpy
from scipy.stats import skewnorm


class RandomData(object):
    def __init__(self, len_data, input_mean, input_std):
        self._len_data = len_data
        self._input_std = input_std
        self._input_mean = input_mean

    def init_random_generator(self, spread=0, skew=0):
        """
        Generates new random numbers with normal distribution.
        Spread and skew can be adjusted using optional args.
        spread: The percentage to adjusted the input std to be expressed as a float can be pos/neg.
        skew:   The amount to adjust the distribution of output expressed as a range from -20 to 20
                neg for left, pos for right.
        """
        numpy.random.seed(1)
        output_std = (1 + spread) * self._input_std
        if skew == 0:
            return numpy.random.normal(self._input_mean, output_std, self._len_data)
        else:
            # normalize around 0
            # * by std to achieve proper spread
            # - by mean to recenter over 0 (option) current build
            # +  target mean to achieve proper y intercept
            return skewnorm.rvs(skew, loc=self._input_mean, scale=output_std, size=self._len_data)

