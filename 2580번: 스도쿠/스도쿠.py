#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2580                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2580                           #+#        #+#      #+#     #
#    Solved: 2024/02/11 14:10:03 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
  for j in range(9):
    if sudoku[i][j] == 0:
      blank.append([i,j])

def condition(y, x, n):
    for i in range(9):
        if n == sudoku[y][i]:
            return False
        
    for i in range(9):
      if n == sudoku[i][x]:
          return False

    for i in range(3):
      for j in range(3):
        if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]:
          return False

    return True

def dfs(n):
  if n == len(blank):
    for i in sudoku:
      print(*i)
    exit()

  for i in range(1, 10):
    y = blank[n][0]
    x = blank[n][1]
    if condition(y,x,i):
      sudoku[y][x] = i
      dfs(n + 1)
      sudoku[y][x] = 0

dfs(0)