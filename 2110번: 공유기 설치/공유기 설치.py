#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2110                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2110                           #+#        #+#      #+#     #
#    Solved: 2024/02/22 22:47:48 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

start, end = 1, houses[-1] - houses[0]

while start <= end:
  mid = (start + end) // 2
  current = houses[0]
  count = 1

  for i in range(1, N):
    if houses[i] - current >= mid:
      count += 1
      current = houses[i]

  if count >= C:
    start = mid + 1
    result = mid
  else:
    end = mid - 1

print(result)