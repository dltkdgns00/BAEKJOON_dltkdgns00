#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16236                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16236                          #+#        #+#      #+#     #
#    Solved: 2025/10/11 02:41:10 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 🦈 상어의 시작 위치 찾기
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            sy, sx = i, j
            grid[i][j] = 0  # 시작 칸은 빈 칸으로 변경
            break
    else:
        continue
    break

# 초기 상태 변수
size = 2        # 상어의 크기
eat = 0         # 현재 먹은 물고기 수
time = 0        # 총 이동 시간

# BFS로 가장 가까운 먹을 물고기 탐색
def bfs(sy, sx, size):
    q = deque()
    q.append((sy, sx))
    dist = [[-1]*N for _ in range(N)]
    dist[sy][sx] = 0
    fishes = []  # 먹을 수 있는 물고기 후보 (거리, 행, 열)

    while q:
        y, x = q.popleft()
        for dy, dx in [(-1,0),(0,-1),(0,1),(1,0)]:  # 위, 왼, 오른, 아래
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and dist[ny][nx] == -1:
                # 지나갈 수 있는지 확인 (상어보다 크면 못 지나감)
                if grid[ny][nx] <= size:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                    # 먹을 수 있는 물고기라면 후보 추가
                    if 0 < grid[ny][nx] < size:
                        fishes.append((dist[ny][nx], ny, nx))

    # 후보가 있으면 거리, 행, 열 순으로 정렬 후 첫 번째 반환
    if not fishes:
        return None
    fishes.sort()
    return fishes[0]  # (거리, y, x)

# 시뮬레이션
while True:
    result = bfs(sy, sx, size)
    if result is None:
        break
    dist, ny, nx = result
    time += dist       # 이동 거리만큼 시간 추가
    eat += 1           # 물고기 한 마리 먹음
    grid[ny][nx] = 0   # 먹은 자리 비우기
    sy, sx = ny, nx    # 상어 위치 갱신

    # 성장 조건
    if eat == size:
        size += 1
        eat = 0

print(time)