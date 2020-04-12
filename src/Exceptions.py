"""
@author: Yoosi
"""



class globalException(Exception):
    """ That class inherit from global Exception class, and build the structure for another classes who want to inherit 
        that structure for another exception class.
    """    
    def __init__(self, id_number):
        self.id_number = id_number
    
    def __str__(self):
        return "its depand on your exception"
    
    def get_id_number(self):
        return self.id_number


class Idtooshort(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_number is too short, that means the user inserted less digits for id numbers.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
    
    def __str__(self):
        return "Your id number is too short, it must be equal to 9 numbers"
    

class Id_with_zeros(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_number is too short, that means the user inserted maybe 9 digits for id numbers but 
        with zeros at the begining they are not considered with id number.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
    
    def __str__(self):
        return "Your id number is too short, it must be equal to 9 numbers, without zeros at the begining "

    
class Idtoolong(globalException):
    """ That class inherit from globalException class for raise an exception that tells us 
        the id_number is too long, that means the user inserted more digits for id numbers.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is too long, the id number must be equal to 9 numbers"


class Num_too_high(globalException):
    """ That class inherit from globalException class for raise an exception that tells us  the id_number is 
        too high, that means the user inserted a high id number  (num that is over the edge of normal id range), 
        and the user need to insert a smaller num.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is too high, you needs to insert a num smaller then  999999700 "
    
 
    
class ID_num_missing_digit(globalException):
    """ That class inherit from globalException class for raise an exception that tells us the
        id_number is not proper, that means the user inserted letters for id numbers, and the user 
        only could insert digits.
    """
    def __init__(self, id_number):
        globalException.__init__(self, id_number)
        
    def __str__(self):
        return "Your id number is not proper, you need to insert only numbers" 

