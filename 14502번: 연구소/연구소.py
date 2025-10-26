#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14502                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14502                          #+#        #+#      #+#     #
#    Solved: 2025/10/23 15:49:40 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

empties = []
viruses = []
for i in range(N):
    for j in range(M):
        if A[i][j] == 0:
            empties.append((i, j))
        elif A[i][j] == 2:
            viruses.append((i, j))

def simulate(walls):
    B = [row[:] for row in A]
    for x, y in walls:
        B[x][y] = 1
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and B[nx][ny] == 0:
                B[nx][ny] = 2
                q.append((nx, ny))
    s = 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 0:
                s += 1
    return s

ans = 0
for walls in combinations(empties, 3):
    v = simulate(walls)
    if v > ans:
        ans = v

print(ans)