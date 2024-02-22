#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2024/02/22 14:46:30 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
  index = bisect.bisect_left(A, target)
  if index < N and A[index] == target:
      print(1)
  else:
      print(0)