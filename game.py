import os
import time

k="⬜"
board=[
  [k,k,k],
  [k,k,k],
  [k,k,k]
]


def printer():
  #os.system("clear")
  print("\n\n")
  
  for i in range(3):
    print("\t\t\t\t",end="")
    
    for k in board[i]:
      print(f"{k}\t",end="")
    print ("\n")

# PLAYER SYMBOLS ADDER

def addx(row, column):
  board[int(row)-1][int(column)-1]="❌"

def addo(row, column):
  board[int(row)-1][int(column)-1]="⭕"



  