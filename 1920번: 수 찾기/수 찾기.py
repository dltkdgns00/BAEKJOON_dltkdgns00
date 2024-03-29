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

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
  start, end = 0, len(A) - 1
  found = False
  
  while start <= end:
    mid = (start + end) // 2

    if A[mid] == target:
      print('1')
      found = True
      break
    elif A[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  if not found:
    print('0')