#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2805                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2805                           #+#        #+#      #+#     #
#    Solved: 2024/02/22 22:13:11 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, M = map(int,input().split())
woods = list(map(int, input().split()))

start, end = 1, max(woods)

while start <= end:
  mid = (start + end) // 2
  woodLength = sum(wood - mid if wood > mid else 0 for wood in woods)

  if woodLength >= M:
    start = mid + 1
  else:
    end = mid - 1

print(end)