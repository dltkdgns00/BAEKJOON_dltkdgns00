#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3055                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3055                           #+#        #+#      #+#     #
#    Solved: 2025/10/26 10:37:51 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

water_q = deque()
hog_q = deque()
visited = [[False] * C for _ in range(R)]

for y in range(R):
  for x in range(C):
    if forest[y][x] == '*':
      water_q.append((y, x))
    elif forest[y][x] == 'S':
      hog_q.append((y, x))
      visited[y][x] = True

time = 0

while hog_q:
  for _ in range(len(water_q)):
    water_y, water_x = water_q.popleft()
    for i in range(4):
      water_ny, water_nx = water_y + dy[i], water_x + dx[i]
      if 0 <= water_ny < R and 0 <= water_nx < C and forest[water_ny][water_nx] == '.':
        water_q.append((water_ny, water_nx))
        forest[water_ny][water_nx] = '*'

  moved = False
  for _ in range(len(hog_q)):
    hog_y, hog_x = hog_q.popleft()
    for i in range(4):
      hog_ny, hog_nx = hog_y + dy[i], hog_x + dx[i]
      if 0 <= hog_ny < R and 0 <= hog_nx < C and not visited[hog_ny][hog_nx]:
        if forest[hog_ny][hog_nx] == 'D':
          print(time + 1)
          exit(0)
        if forest[hog_ny][hog_nx] == '.':
          hog_q.append((hog_ny, hog_nx))
          visited[hog_ny][hog_nx] = True
          moved = True

  time += 1

print("KAKTUS")