def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    return int(7/2)


def float_multiplication():
   
    
    return float(3*2)
    


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    x=float_multiplication()
   
    y=int_division()
    return float(x+y)


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string='Python is awesome!'
    string=string.strip().split()
    word=string[2]
    word=word.replace("!","")
    return word


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string='Python is awesome!'
    string=string.lower()
    return string

def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    count=0
    string='Python is awesome!'
    for i in string:
        if "o" in i:
            count+=1
    return count



def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    pass

print(combine_operations())