#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1912                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1912                           #+#        #+#      #+#     #
#    Solved: 2024/02/21 20:46:57 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
  dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))