#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11000                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11000                          #+#        #+#      #+#     #
#    Solved: 2025/10/10 23:53:32 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys, heapq

input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int,input().split())) for _ in range(N)]

lectures.sort()

pq = []

for start, end in lectures:
  if pq and pq[0] <= start:
    heapq.heappop(pq)
  heapq.heappush(pq, end)

print(len(pq))