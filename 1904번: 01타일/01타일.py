#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1904                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1904                           #+#        #+#      #+#     #
#    Solved: 2024/02/21 11:58:19 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
  if i == 1:
    dp[i] = 1
  elif i == 2:
    dp[i] = 2
  else:
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])