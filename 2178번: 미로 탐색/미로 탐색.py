#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 02:10:05 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

grid = [list(map(int, list(input().strip()))) for _ in range(N)]

dq = deque()
dist = [[0]*M for _ in range(N)]

dist[0][0] = 1
dq.append((0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and dist[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            dq.append((nx, ny))

print(dist[N-1][M-1])