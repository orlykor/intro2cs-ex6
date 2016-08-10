#############################################################
# FILE : y_tree.py
# WRITER : orly koren, orlykor12
# EXERCISE : intro2cs ex6
# DESCRIPTION:
#this exercise is about drawing a tree as a symbol of recursion. of what the 
#recursion does.
#############################################################

import turtle

def draw_tree(length=200):
    """
    this func makes recursively a draw of a tree. it goes left until the 
    length is smaller then 10, then when it is, it turns to the other part of 
    the tree, when it goes backward it gets more length, then it can continue 
    until it finishes all the options.
    """
    LEFT_DEG= 30
    RIGHT_DEG= 60
    MIN_LENGTH= 10
    SHORTER_LEN= 0.6

    if length >= 10:
        turtle.forward(length)
        turtle.left(30)
        draw_tree(0.6*length)
        turtle.right(60)
        draw_tree(0.6*length)
        turtle.left(30)
        turtle.backward(length)




