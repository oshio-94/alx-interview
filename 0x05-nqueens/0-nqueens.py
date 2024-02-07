#!/usr/bin/python3
"""
N Queens.
"""
import sys

def solveNQueens(n):
    """Program that solves the N queens problem"""
    new_board = []
    queens = [-1] * n

    def solution(index):
        """Recursively resolves the N queens problem"""
        if index == len(queens):  # n queens have been placed correctly
            new_board.append(queens[:])
            return  # backtracking
        for i in range(len(queens)):
            queens[index] = i
            if valid(index):  # pruning
                solution(index + 1)

    # check whether nth queens can be placed
    def valid(n):
        """Method that checks if a position in the board is valid"""
        for i in range(n):
            if abs(queens[i] - queens[n]) == n - i:  # same diagonal
                return False
            if queens[i] == queens[n]:  # same column
                return False
        return True

    def make_all_boards(new_board):
        """Method that builts the List that be returned"""
        result_board = []
        for queens in new_board:
            board = []
            for row, col in enumerate(queens):
                board.append([row, col])
            result_board.append(board)
        return result_board

    solution(0)
    return make_all_boards(new_board)

if __name__ == "__main__":
    if len(argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)
    else:
        result = solveNQueens(n)
        for row in result:
            print(row)