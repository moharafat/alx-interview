#!/usr/bin/python3
"""Unlock boxes"""

def canUnlockAll(boxes):
    """Determine if all the boxes can be opened"""
    # Initialize variables
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # Start by unlocking the first box
    keys = boxes[0]  # Start with the keys from the first box
    queue = keys[:]  # Initialize the queue with keys from the first box

    while queue:
        key = queue.pop(0)  # Get the next key to process
        if key < n and not unlocked[key]:  # Check if the box can be unlocked
            unlocked[key] = True  # Mark the box as unlocked
            queue.extend(boxes[key])  # Add new keys to the queue

    return all(unlocked)  # Return True if all boxes are unlocked, otherwise False
