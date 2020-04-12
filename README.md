# check if ID number is valid
 ### you need to enter your id num and it check if your id is valid according to the rules http://halemo.net/info/idcard/
At the beginig the user needs to insert id number and the ```check_id```  runs over and over again
to check if the id number not proper (if the length of id_number is less from 9 digits or 
bigger from 9 or if its not digits) until the user insert exactly 9 digits, and then the ```check_id``` 
 checks if its proper id number (if the id number contains all the conditions for being a proper)
 if the id number is proper the  ```check_id```  will tell you that is good id number.
if StopIteretion raise the ```check_id```  display 10 possible id proper option and stop the iteration.
The ```check_id``` return True if the id number is proper, else the it display to you 10 proper id number options from the iterator, and more 10 proper id number from generator.

## how to run

    # no inputs
    python check_id.py
