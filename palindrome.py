#############################################################
# FILE : palindrome.py
# WRITER : orly koren, orlykor12
# EXERCISE : intro2cs ex6
# DESCRIPTION:
#those are two functions that check if the string given is in the
# form of A palindrome or not. the first one is for the whole word,
#the second one is for a certain input index.
#############################################################

def is_palindrome_1(s):
    '''
    this func checks if the string given is a palindrome or not.
    it goes recursivly from the inside outside and checks each two 
    characters if they are the same or not, if they are it continues until 
    there are only less then 2 characters, then its true if not return false.
    '''
    length = len(s)
    NO_LENGTH = 0
    MIN_LENGTH = 2
    NOT_PALI_LENGTH = 1
    BALANCED = True
    NOT_BALANCED = False

    if 0 <= length < 2:
        return True
    elif length < 1:
        return False
    elif s[0] == s[length-1]:
        return is_palindrome_1(s[1:length-1])        
    else:
        return False




def is_palindrome_2(s,i,j):
    '''
    this func checks if the string in the given indexes is a palindrome or not.
    if the characters in the string, with the given indexes are the same, then 
    it goes recursivly and checks the next two characters, now with new 
    indexes, until the two indexes are equal. if all characters are equal it
    returns true, if at any time it wasnt equal it returns false. 
    '''
    OFFSET= 1
    BALANCED = True
    NOT_BALANCED = False

    if i == j or i == j + 1:       
        return True
        
    elif i > j:
        return False
    elif s[i] == s[j]:
        return is_palindrome_2(s,i + 1,j - 1)
    else:
        return False





