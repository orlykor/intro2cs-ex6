#############################################################
# FILE : balanced_brackets.py
# WRITER : orly koren, orlykor12
# EXERCISE : intro2cs ex6
# DESCRIPTION:
#those funcs check if the strings have balanced brackets. 
#############################################################


def is_balanced(s):
    '''
    this func checks if the number of '(' is equal to the number of')' if the
    string is balanced or not.
    '''
    counter = 0    
    i = 0
    BALANCED = True
    NOT_BALANCED = False

    while i < len(s):
        if s[i] == "(" :
            counter += 1            
        elif s[i] == ")":
            counter -= 1                
        if counter < 0: 
            return False        
        i += 1
    if counter > 0:
        return False
    else:
        
        return True



def violated_balanced(s):
    '''
    this func checks if the amount of "(" is equal to the amount of ")". 
    if it is then it returns -1, if not it checks recursivley in another 
    function wheter the counter is negetive or not. the counter counts 
    for ")" minus 1 and plus 1 for the other. if the counter is negetive, then 
    stop and start returning -1 and we add 1 until we get the index we 
    found the problem in. 
    every step in the recursia we make a new list without the s of the old
    one, we go that way until we get that the lenght is 0, then we start 
    returning 0 and we add 1 to get the lengh of the string.    
    '''
    counter = 0  
    i = 0
    OFFSET = 1 
    RETURN_INDEX = -1
    RETURN_LENGTH = 0

    while i < len(s):
        if s[i] == "(" :
            counter += 1            
        elif s[i] == ")":
            counter -= 1                
        if counter < 0: 
            break
        i += 1
    if counter > 0 or counter < 0:        
        counter = 0
    else:        
        return -1    
    def find_violated(s,counter):
        if counter < 0:            
            return -1
        elif len(s) == 0:
            return 0
        if s[0] == "(":
            counter += 1
        elif s[0] == ")":
            counter -= 1
            
        return find_violated(s[1:len(s)],counter) + 1

    condition= find_violated(s,counter)
    return condition




def match_brackets(s):
    '''         
    this func checks if the string is balanced or not, if not it returns an 
    empty list, if it is then it goes into the inside func. the inside func 
    checks for matched brackets between '(' and its matched ')' recursivly.
    when it finds the matched ')' it replace the bracket's place for the 
    distance between them. for ')' it puts it with negetive num.
    if there's none of them it replacs the value with the value '0'.
    when it finishes recursivly it returns the new string with the changes.       
    ''' 
    counter = 0  
    i = 0
    lst1 = list(s)
    lst = []
    NOT_BRACKETS = 0
  
    while i < len(s):
        if lst1[i] == "(" :
            counter += 1            
        elif lst1[i] == ")":
            counter -= 1
        else:
            lst1[i] = 0                
        if counter < 0: 
            return lst
        i += 1
    if counter > 0 or counter < 0:        
        return lst 
    else:                        
        lst = lst1

    def helper(lst):        
        counter = 0        
        for i in range(len(lst)):
            if lst[i] == "(":
                c_open = i
            else:
                if lst[i] != "(" and lst[i] != ")":
                    counter += 1
        if counter == len(lst):
            return lst
        c_close = c_open
        for j in lst[c_open:]: #goes from where we found the last "("
            if j == ")":                
                lst[c_open] = c_close - c_open
                lst[c_close] = c_open - c_close
                break
            else:
                c_close += 1           
        return helper(lst)

    new_list = helper(lst)
    return new_list     




