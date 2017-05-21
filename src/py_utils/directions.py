#!/usr/bin/env python
"""Provides functions to help with navigating number grids."""


def right(i, j):
    """Move right in a grid"""
    i += 1
    return i, j


def right_down(i, j):
    """Move right-down in a grid"""
    i += 1
    j += 1
    return i, j


def down(i, j):
    """Move down in a grid"""
    j += 1
    return i, j


def left_down(i, j):
    """Move left-down in a grid"""
    i -= 1
    j += 1
    return i, j


def left(i, j):
    """Move left in a grid"""
    i -= 1
    return i, j


def left_up(i, j):
    """Move left-up in a grid"""
    i -= 1
    j -= 1
    return i, j

def up(i, j):
    """Move up in a grid"""
    j -= 1
    return i, j


def right_up(i, j):
    """Move right-up in a grid"""
    i += 1
    j -= 1
    return i, j

