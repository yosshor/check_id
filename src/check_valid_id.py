"""
@author: Yoosi
"""

from Exceptions import ID_num_missing_digit, Id_with_zeros, Idtoolong, Idtooshort, Num_too_high

def check_id_valid(id_number):
    """ That function checks if the id_number is correct or proper, checks if the id number have zeros at the
        beginig, and checks if your id number is not contains only digits (for example if you have letters 
        or punctuation in your id number), and ofcourse if the length of the id number is bigger then 9 or less from 9.
        :param id_number: id_number value.
        :type id_number: str 
        :raise: Num_too_high if the id number tallest then  999999700
        :raise: Idtooshort if id_number is less then 9 digits.
        :raise: Idtoolong if id_number is more then 9 digits.
        :raise: ID_num_missing_digit if id_number not contains oonly digits.
        :raise: Id_with_zeros if id number contains zeros at the beginig.
        :return: True if the id_number contains 9 real correct digits, else raise an error and False.
        :rtype: bool 
    """
    try :
        if not id_number.isdigit():
            raise ID_num_missing_digit(id_number)  
        if str(id_number)[0] == '0':
             if len(str(int(id_number))) < 9:
                 raise Id_with_zeros(id_number)   
        if len(str(int(id_number))) < 9:
            raise Idtooshort(id_number)
        if len(str(int(id_number))) > 9:
            raise Idtoolong(id_number)
        if int(id_number) >= 999999700:
            raise Num_too_high(id_number)
            
    except Idtooshort:
        print(Idtooshort.__str__(id_number))
        return False
    except Idtoolong:
        print(Idtoolong.__str__(id_number))
        return False
    except ID_num_missing_digit:
        print(ID_num_missing_digit.__str__(id_number))
        return False
    except Id_with_zeros:
        print(Id_with_zeros.__str__(id_number))
        return False
    except Num_too_high:
        print(Num_too_high.__str__(id_number))
        return False
    else:
        return True