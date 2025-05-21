#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12100                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12100                          #+#        #+#      #+#     #
#    Solved: 2025/05/21 18:18:42 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import copy

def move(board, dir):
  # 2차원 배열 생성
  new_board = [[0]*N for _ in range(N)]
  # dir이 0(왼), 1(오)일 땐 행 기준으로
  # dir이 2(위), 3(아래)일 땐 열 기준으로
  # val != 0이면 빈 칸이 아니므로 temp에 저장
  for i in range(N):
    temp = []
    for j in range(N):
      x, y = (i, j) if dir in [0, 1] else (j, i) # 0(왼), 1(오)일 경우 (i, j) else (j, i)
      val = board[x][y] if dir % 2 == 0 else board[y][x] # 
      if val != 0:
          temp.append(val)
    if dir in [1, 3]: # 1(오), 3(아래)일 경우 reverse
      temp.reverse()

    # 같은 숫자가 붙어 있으면 두 개 합쳐서 넣고 한 칸 건너뜀
    merged = []
    idx = 0
    while idx < len(temp):
      if idx + 1 < len(temp) and temp[idx] == temp[idx + 1]:
        merged.append(temp[idx] * 2)
        idx += 2
      else:
        merged.append(temp[idx])
        idx += 1

    if dir in [1, 3]:
      merged += [0] * (N - len(merged))
      merged.reverse()
    else:
      merged += [0] * (N - len(merged))

    for j in range(N):
      if dir == 0: new_board[i][j] = merged[j]         # 왼쪽
      elif dir == 1: new_board[i][j] = merged[j]       # 오른쪽
      elif dir == 2: new_board[j][i] = merged[j]       # 위
      else: new_board[j][i] = merged[j]                # 아래

  return new_board

def dfs(board, cnt):
  global result
  if cnt == 5:
    for i in range(N):
      result = max(result, max(board[i]))
    return
  for d in range(4):
    next_board = move(copy.deepcopy(board), d)
    dfs(next_board, cnt + 1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

dfs(board, 0)
print(result)