#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1654                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1654                           #+#        #+#      #+#     #
#    Solved: 2024/02/22 17:04:26 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import bisect

input = sys.stdin.readline

K, N = map(int, input().split())
lanCables = [int(input()) for _ in range(K)]

start, end = 1, max(lanCables)

while start <= end:
  mid = (start + end) // 2
  count = sum(cable // mid for cable in lanCables)

  if count >= N:
    start = mid + 1
  else:
    end = mid - 1

print(end)