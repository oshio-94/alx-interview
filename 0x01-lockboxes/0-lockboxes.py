#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened."""
    sizebox = len(boxes)  # sizebox of the list of boxes.
    newbox = {}  # dictionary that will contain the boxes that can be opened.
    check = 0  # check of the box that will be checked.

    for keys in boxes:  # for each box in the list of boxes.
        if len(keys) == 0 or check == 0:
            newbox[check] = -1
        for key in keys:
            if key < sizebox and key != check:
                newbox[key] = key  # the box is added to the dictionary.
        if len(newbox) == sizebox:
            return True  # all the boxes can be opened.
        check += 1
    return False