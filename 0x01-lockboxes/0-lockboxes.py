#!/usr/bin/python3
""" method to determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """ method to determines if all the boxes can be opened."""
    sizebox = len(boxes) 
    newbox = {} 
    check = 0  

    for keys in boxes: 
        if len(keys) == 0 or check == 0:
            newbox[check] = -1
        for key in keys:
            if key < sizebox and key != check:
                newbox[key] = key 
        if len(newbox) == sizebox:
            return True  
        check += 1
    return False