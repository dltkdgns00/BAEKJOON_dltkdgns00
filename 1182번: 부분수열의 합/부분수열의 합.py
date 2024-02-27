#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1182                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1182                           #+#        #+#      #+#     #
#    Solved: 2024/02/26 18:08:23 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))
count = 0

def dfs(i, sum):
  global count
  if i >= N:
    return
  
  sum += lst[i]
  if sum == S:
    count += 1
  dfs(i+1, sum - lst[i])
  dfs(i+1, sum)

dfs(0,0)
print(count)