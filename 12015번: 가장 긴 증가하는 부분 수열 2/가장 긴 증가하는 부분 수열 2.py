#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12015                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12015                          #+#        #+#      #+#     #
#    Solved: 2024/02/23 15:00:43 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

lis = []

for num in A:
  if not lis or num > lis[-1]:
    lis.append(num)
  else:
    index = bisect_left(lis, num)
    lis[index] = num

print(len(lis))