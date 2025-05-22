#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14499                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14499                          #+#        #+#      #+#     #
#    Solved: 2025/05/22 16:52:09 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주사위 정의하고 6의 배열? 반대 편의 수를 어떻게 알것인가? 미리 정의를 해두면 됨 알고보니 그냥 역순이었음

''' 주사위 인덱스
문제:  2      정의:  1      방향:  북
    4 1 3        3 0 2       서 위 동
      5            4           남
      6            5           밑
'''
dice = [0] * 6

N, M, x, y, K = map(int, input().split())

board = [[0] * M for _ in range(N)]

for i in range(N):
  board[i] = list(map(int, input().split()))

order = list(map(int, input().split()))

# 1(동), 2(서), 3(북), 4(남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll_east():
  temp = dice[:]
  dice[0] = temp[3]  # top ← west
  dice[2] = temp[0]  # east ← top
  dice[5] = temp[2]  # bottom ← east
  dice[3] = temp[5]  # west ← bottom

def roll_west():
  temp = dice[:]
  dice[0] = temp[2]  # top ← east
  dice[2] = temp[5]  # east ← bottom
  dice[5] = temp[3]  # bottom ← west
  dice[3] = temp[0]  # west ← top

def roll_north():
  temp = dice[:]
  dice[0] = temp[4]  # top ← south
  dice[1] = temp[0]  # north ← top
  dice[5] = temp[1]  # bottom ← north
  dice[4] = temp[5]  # south ← bottom

def roll_south():
  temp = dice[:]
  dice[0] = temp[1]  # top ← north
  dice[1] = temp[5]  # north ← bottom
  dice[5] = temp[4]  # bottom ← south
  dice[4] = temp[0]  # south ← top

for i in range(K):

  dir = order[i]

  x += dx[dir - 1]
  y += dy[dir - 1]

  if not (0 <= x < N and 0 <= y < M):
    x -= dx[dir - 1]
    y -= dy[dir - 1]
    continue

  if dir == 1:
    roll_east()
  elif dir == 2:
    roll_west()
  elif dir == 3:
    roll_north()
  elif dir == 4:
    roll_south()
 
  if board[x][y] == 0:
    board[x][y] = dice[5]
  else:
    dice[5] = board[x][y]
    board[x][y] = 0
  
  print(dice[0])