#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2206                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2206                           #+#        #+#      #+#     #
#    Solved: 2025/10/24 15:18:32 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
field = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0, 0] for _ in range(M)] for __ in range(N)]

def bfs():
  q = deque()
  q.append((0, 0, 0))
  visited[0][0][0] = 1

  dy = (-1, 1, 0, 0)
  dx = (0, 0, -1, 1)

  while q:
    y, x, w = q.popleft()
    if y == N - 1 and x == M - 1:
      return visited[y][x][w]

    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < M:
        
        if field[ny][nx] == 0 and visited[ny][nx][w] == 0:
          visited[ny][nx][w] = visited[y][x][w] + 1
          q.append((ny, nx, w))
        
        elif field[ny][nx] == 1 and w == 0 and visited[ny][nx][1] == 0:
          visited[ny][nx][1] = visited[y][x][w] + 1
          q.append((ny, nx, 1))

  return -1

print(bfs())