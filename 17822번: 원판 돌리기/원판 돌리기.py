#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17822                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17822                          #+#        #+#      #+#     #
#    Solved: 2025/10/22 17:27:14 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(N)]
rt = [list(map(int, input().split())) for _ in range(T)] # x, d, k

def compare_near(i, j):
    v = circles[i][j]
    if v == 0:
        return set()
    res = set()
    jl = (j - 1) % M
    jr = (j + 1) % M
    if circles[i][jl] == v:
        res.add((i, j)); res.add((i, jl))
    if circles[i][jr] == v:
        res.add((i, j)); res.add((i, jr))
    if i > 0 and circles[i - 1][j] == v:
        res.add((i, j)); res.add((i - 1, j))
    if i < N - 1 and circles[i + 1][j] == v:
        res.add((i, j)); res.add((i + 1, j))
    return res


for x, d, k in rt:
    for i in range(N):
        if (i + 1) % x == 0:
            circles[i].rotate(k if d == 0 else -k)

    to_del = set()
    for i in range(N):
        for j in range(M):
            to_del |= compare_near(i, j)

    if to_del:
        for a, b in to_del:
            circles[a][b] = 0
    else:
        s = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                v = circles[i][j]
                if v != 0:
                    s += v
                    cnt += 1
        if cnt > 0:
            avg = s / cnt
            for i in range(N):
                for j in range(M):
                    v = circles[i][j]
                    if v == 0:
                        continue
                    if v > avg:
                        circles[i][j] = v - 1
                    elif v < avg:
                        circles[i][j] = v + 1

print(sum(map(sum, circles)))