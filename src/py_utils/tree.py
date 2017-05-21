#!/usr/bin/env python
"""Helper module for using trees."""

from collections import deque
from functools import partial


class Found(Exception):
    """Signal raised when an item is found."""
    def __init__(self, val=None):
        self.val = val
        super().__init__()


class Node(object):
    """A node in a tree has a value and may contain a parent and/or multiple
    children."""
    def __init__(self, val, children=None, parent=None):
        self.val = val
        if children:
            self.children = children
        else:
            self.children = []
        self.parent = parent

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return (child for child in self.children)

    def insert(self, value):
        """Adds a single child to this node."""
        child = Node(value, parent=self)
        self.children.append(child)
        return child

    def insert_multiple(self, values):
        """Add multiple children to this node."""
        for val in values:
            self.insert(val)


def traverse_dfs(node, stack=None, callback=None):
    """Perform a depth first search, with optional callback applied to each
    node."""
    continue_searching = True

    if callback:
        continue_searching = callback(node, stack)

    if continue_searching:
        if stack is not None:
            stack.append(node)

        for child in node.children:
            traverse_dfs(child, stack, callback)

        if stack is not None:
            stack.pop()


def traverse_bfs(node, fringe=None, callback=None):
    """Perform a breadth first search, with optional callback applied to each
    node."""
    if fringe is None:
        fringe = deque(node)

    while fringe:
        node = fringe.pop()

        if callback:
            callback(node, fringe)

        # Collect all nodes on this fringe.
        for child in node:
            fringe.appendleft(child)


def traverse_a(node, cost):
    """Search the tree using the A* algorithm, using a provided cost function."""
    depth = 0
    node.cost = cost(node)
    node.depth = depth
    fringe = [node]
    solution = []

    while fringe:
        # Explore the next state with the lowest cost.
        current = fringe.pop()

        if current.cost == 0:
            # Solution found! Walk backwards from leaf back to parent
            print("Solution found")
            solution = deque()
            while current:
                solution.appendleft(current)
                current = current.parent

            return solution

        # Collect all nodes on the fringe.
        for child in current.children:
            child.cost = cost(child)
            child.depth = current.depth + 1
            fringe.append(child)

        fringe.sort(key=lambda x: x.cost + x.depth, reverse=True)


def lookup(val, node, _):
    """Sample callback function to find a given value in a tree."""
    if node.val == val:
        raise Found(val)

    return True

