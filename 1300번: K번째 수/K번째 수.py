#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1300                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1300                           #+#        #+#      #+#     #
#    Solved: 2024/02/23 13:48:18 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

start, end = 1, N * N

while start <= end:
  mid = (start + end) // 2
  count = sum(min(mid // i, N) for i in range(1, N+1))

  if count >= k:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)