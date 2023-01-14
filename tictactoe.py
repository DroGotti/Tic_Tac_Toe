#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:03:02 2022

@author: drogotti
"""

# initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# player 1 is 'X' and player 2 is 'O'
players = ['X', 'O']

# current player
player = 0

# keep track of the number of moves made
moves_made = 0

# function to print the current state of the board
def print_board():
  for row in board:
    print(' '.join(row))

# main game loop
while True:
  # print the current state of the board
  print_board()

  # get the row and column from the player
  row = int(input("Enter row (0, 1, 2): "))
  col = int(input("Enter column (0, 1, 2): "))

  # check if the selected position is empty
  if board[row][col] == ' ':
    # make the move
    board[row][col] = players[player]

    # switch to the other player
    player = (player + 1) % 2

    # increase the number of moves made
    moves_made += 1
  else:
    # the selected position is not empty, ask the player to try again
    print("That position is already occupied, try again")

  # check if the game is over
  if moves_made >= 5:
    # check if one of the players has won
    for player in players:
      # check rows
      for row in board:
        if row == [player, player, player]:
          print(f"Player {player} wins!")
          exit()

      # check columns
      for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
          print(f"Player {player} wins!")
          exit()

      # check diagonals
      if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(f"Player {player} wins!")
        exit()
      if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"Player {player} wins!")
        exit()

  # check if the board is full
  if moves_made == 9:
    print("It's a draw!")
    exit()
