#!/usr/bin/env python3
"""Coin sums"""
import numpy as np

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
TARGET = 200


def main():
    """Find all possible combinations of COINS to form TARGET."""
    combinations = np.matrix([[None for _ in range(len(COINS))]
                             for _ in range(TARGET + 1)])
    set_1p_column(combinations)
    add_other_combinations(combinations)
    return combinations[TARGET, len(COINS) - 1]


def set_1p_column(combo_matrix):
    """
    Set the 1p column to 1 t reflect that there is only one way of reaching
    any target with 1ps. This mutates combo_matrix.
    """
    for i in range(TARGET + 1):
        combo_matrix[i, 0] = 1


def add_other_combinations(combo_matrix):
    """
    Add other coin combinations to the matrix. This mutates combo_matrix.
    """
    for value in range(TARGET + 1):
        for coin in range(1, len(COINS)):
            if value >= COINS[coin]:
                # ways to form value using smaller coins
                combo_matrix[value, coin] = combo_matrix[value, coin - 1]
                # ways to form value using a new coin
                combo_matrix[value, coin] += combo_matrix[
                    value - COINS[coin], coin
                ]
            else:
                # copy ways to use smaller coins
                combo_matrix[value, coin] = combo_matrix[value, coin - 1]


if __name__ == '__main__':
    print(main())
