"""
@author: Yoosi
"""
import numpy as np

def check_num(id_number):
    """ This function take the correct 9 digits of id number and makes on him some manipulations, that
        means that function check if after the manipulation if the id number % 10 == 0, if yes its means 
        that id number is proper.
        :param id_number: id_number value
        :type id_number: str
        :return: True if after manipulation the id number % 10 == 0, else False.
        :rtype: bool
    """
    first = [int(j) * 2  if (i + 1) % 2 == 0 else int(j) for i, j in enumerate(str(id_number))]
    first = [str(i) for i in first]
    second = [(int(num[0]) + int(num[1]))  if int(num) > 9 else num for i, num in enumerate(first)]
    the_sum = np.sum(np.array(second, dtype = int))  # I can do it with loop and one total variable that aggregate all i in loop to the total variable
    if the_sum % 10 == 0:
        return True
    return False
