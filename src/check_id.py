"""
@author: Yoosi_shor
"""
import numpy as np
from check_valid_id import check_id_valid
from check_num import check_num



class IDIterator:
    """ This class gets id number and return iterator with 10 correct id numbers,
        starts from id number that you inserted and over.
    """      
    def __init__(self, id_number):  
        self._id = id_number
        self._start = 0
        self._end = 999999999
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._start < int(self._id) < self._end:
            for i in range(int(self._id), int(self._end)):
                self._id = i    
                if check_id_valid(str(self._id)):
                    if check_num(str(self._id)):
                        self._id += 1    
                        return self._id - 1 


def id_generator(id_num):
    """ This generator function takes your impropre 9 digits id number and generat
        from that number a proper id number until it we get to 999999999.
        :param id_number: id_number value
        :type id_number: str
        :return: The next proper id number.
        :rtype: int 
    """
    for num in range(int(id_num), 999999999):
        id_num = num
        if check_id_valid(str(id_num)):
            if check_num(str(id_num)):
                yield id_num

 
def main():
    """ That is the main function, here we controll to all functions, at the beginig the user need to insert
        id number and the function runs over and over again if the id number not normal/proper (if the length
        of id_number is less from 9 digits or bigger from 9 or if its not digits) until the user insert exactly
        9 digits, and then the function check if its proper id number (if the id number contains all the conditions
        for being a proper), if the id number is proper the function will tells you that is good id number.
        :raise: StopIteretion if the function display 10 possible id proper option stop the iteration.
        :return: True if the id number is proper, else the function display to you 10 proper 
        id number options from the iterator, and 10 proper id number from generator.
        :rtype: bool 
    """
    id_number = ''
    while id_number == '':
        try:
            id_number = input("please enter the id_number : ")
            if check_id_valid(id_number):
                if check_num(id_number):
                    print("Your id number is proper")
                    raise StopIteration(id_number)
                print(" ")
                print("This 10 options for new proper id_number from iterator")
                for index, iterator in enumerate(IDIterator(id_number)):
                    if index >= 10:
                        print(" ")
                        break
                    print(iterator)
                print("This 10 options for new proper id_number from generator")
                for index_generator, generator_num in enumerate(id_generator(id_number)):
                    if index_generator >= 10:
                        raise StopIteration()
                    print(generator_num)
            main()
        except StopIteration:
            return

if __name__ == "__main__":
    main()



