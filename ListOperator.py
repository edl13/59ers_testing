"""
Module for performing several basic operations on lists of integers.
"""


def import_modules():
    """Imports necessary modules into global context

    :raises ImportError: Could not import numpy
    :raises ImportError: Could not import logging
    :raises ImportError: Could not import logging_config
    """

    global np
    global logging
    global config
    try:
        import numpy as np
    except (ModuleNotFoundError, ImportError) as error:
        raise ImportError(
            '''Could not import numpy. Please make sure to have the package installed''')

    try:
        import logging
    except (ModuleNotFoundError, ImportError) as error:
        raise ImportError(
            '''Could not import logging. Please make sure to have the package
            installed'''
        )

    try:
        from logging_config import config
    except (ModuleNotFoundError, ImportError) as error:
        raise ImportError(
            '''Could not import logging_config. Please make sure to have the
            package installed'''
        )


import_modules()


class BadNumbersException(Exception):
    pass


class ListOperator(object):
    """Class performs summing, min, max, and max difference of a list of
    integers
    """

    def __init__(self, nums):
        """Initialize ListOperator object

        :param nums: Input number list
        """
        logging.basicConfig(**config)
        self.logger = logging.getLogger(__name__)

        # Initialize variables
        self.nums = nums
        self.sum = None
        self.min = None
        self.max = None
        self.maxdiff = None

    @property
    def nums(self):
        """Define private variable nums
        """
        return self.__nums

    @nums.setter
    def nums(self, nums):
        """Setter for nums

        :params nums: Input number list
        """
        self.check_inputs(nums)
        self.__nums = nums

    @property
    def sum(self):
        """Define private variable sum
        """
        return self.__sum

    @sum.setter
    def sum(self, sum):
        """Setter for sum

        :params sum: sum value to set to
        """
        self.__sum = sum

    @property
    def min(self):
        """Define private variable min
        """
        return self.__min

    @min.setter
    def min(self, min):
        """Setter for min

        :params min: min value to set to
        """
        self.__min = min

    @property
    def max(self):
        """Define private variable max
        """
        return self.__max

    @max.setter
    def max(self, max):
        """Setter for max

        :params max: max value to set to
        """
        self.__max = max

    @property
    def maxdiff(self):
        """Define private variable maxdiff
        """
        return self.__maxdiff

    @maxdiff.setter
    def maxdiff(self, maxdiff):
        """Setter for maxdiff

        :params maxdiff: maxdiff value to set to
        """
        self.__maxdiff = maxdiff

    def get_sum(self):
        """ Returns the sum of a list

        :param input_list: list of n integers between -9,000 and 9,000
        :returns: sum of all the n integers in the list
        """
        self.logger.info('Calculating sum of the list')
        self.logger.debug('Input list: %s', str(self.nums))
        calc_sum = sum(self.nums)
        self.logger.debug('Output: %s', calc_sum)
        self.sum = calc_sum
        return calc_sum

    def get_min_max(self):
        """ Returns min and max in a list

        :param input_list: (int) list to get min and max of
        :returns: min and max of list in a tuple
        """
        self.logger.info('Obtaining min and max of list')
        self.logger.debug('Input list: %s', str(self.nums))
        min_max = (np.amin(self.nums), np.amax(self.nums))
        self.min = min_max[0]
        self.max = min_max[1]
        self.logger.debug('Output: %s', str(min_max))
        return min_max

    def get_max_diff(self):
        """ Returns maximum difference between consecutive elements in input list

        :param input_list: list of n integers between -9,000 and 9,000
        :returns: maximum difference d defined by d = input_list[i+1] - input_list[i] for i = 0 to n-1
        """
        self.logger.info('Calculating maximum difference in the list')
        self.logger.debug('Input list: %s', str(self.nums))
        diff_arr = np.diff(self.nums)
        max_diff = np.max(diff_arr)
        self.maxdiff = max_diff
        self.logger.debug('Output: %s', str(max_diff))
        return max_diff

    def check_inputs(self, input_list):
        """ Checks if input list fits desired format

        :param input_list: list of n integers between -9,000 and 9,000
        :raises TypeError: Input must be lists
        :raises TypeError: Input elements must be integers
        :raises ValueError: All input elements must be between -9,000 and 9,000 (inclusive)
        :raises BadNumbersException: Numbers 123 and 321 cannot be in same list
        """
        if(not type(input_list) is list):
            raise TypeError('Input must be a list')
            self.logger.error("Input must be list of integers")
        if(not all([type(num) is int for num in input_list])):
            raise TypeError('All inputs in list must be integers.')
            self.logger.error('All inputs in list must be integers.')
        if(any([abs(num) > 9000 for num in input_list])):
            raise ValueError('All inputs must be between -9,000 and 9,000 (inclusive)')
            self.logger.error('All inputs must be between -9,000 and 9,000 (inclusive)')
        elif (any([abs(num) > 8500 for num in input_list])):
            self.logger.warning('Some of your inputs are very close to 9000. Be careful to not exceed 9000!')
        elif (any([abs(num) > 7000 for num in input_list])):
            self.logger.warning('Some of your inputs are somewhat close to 9000. Be careful to not exceed 9000!')

        if(123 in input_list and 321 in input_list):
            raise BadNumbersException('List cannot contain both 123 and 321')
