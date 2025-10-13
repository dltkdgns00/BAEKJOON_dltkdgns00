#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 11:56:17 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

apt = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

size = []

def bfs(sy, sx):
  cnt = 1
  q = deque([(sy, sx)])
  visited[sy][sx] = True
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < N and 0 <= nx < N:
        if not visited[ny][nx] and apt[ny][nx] == 1:
          visited[ny][nx] = True
          q.append((ny,nx))
          cnt += 1
  size.append(cnt)

for y in range(N):
  for x in range(N):
    if apt[y][x] == 1 and not visited[y][x]:
      bfs(y,x)

size.sort()
print(len(size))
for i in size:
  print(i)