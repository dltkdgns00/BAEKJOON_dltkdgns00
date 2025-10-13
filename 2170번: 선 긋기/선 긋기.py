#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2170                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2170                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 00:35:46 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]

lines.sort()

curL, curR = lines[0]

total = 0

for start, end in lines[1:]:
  if start > curR:
    total += curR - curL
    curL, curR = start, end
  else:
    curR = max(curR, end)

total += curR - curL


print(total)