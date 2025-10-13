#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2025/10/11 12:16:21 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# d = 0, 1, 2, 3 -> 북, 동, 남, 서

count = 1

while True:
  cleaned = False
  for i in range(4):
    d = (d + 3) % 4
    ny, nx = r + dy[d], c + dx[d]
    if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] == 0:
      grid[ny][nx] = 2  
      r, c = ny, nx
      count += 1
      cleaned = True
      break
  if not cleaned:
    back = (d + 2) % 4
    br = r + dy[back]
    bc = c + dx[back]
    if grid[br][bc] == 1:
      break
    else:
      r, c = br, bc

print(count)