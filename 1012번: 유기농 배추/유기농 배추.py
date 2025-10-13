#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1012                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 08:17:17 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
  q = deque()
  q.append((y, x))
  field[y][x] = 0  # 방문 표시: 배추를 0으로 바꿔 재방문 방지 (visited 배열 제거)
  while q:
    cy, cx = q.popleft()
    for i in range(4):
      ny, nx = cy + dy[i], cx + dx[i]
      if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 1:
        field[ny][nx] = 0
        q.append((ny, nx))

for _ in range(T):
  M, N, K = map(int, input().split())
  field = [[0]*M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    field[y][x] = 1

  count = 0
  for y in range(N):
    for x in range(M):
      if field[y][x] == 1:
        bfs(y, x)
        count += 1

  print(count)