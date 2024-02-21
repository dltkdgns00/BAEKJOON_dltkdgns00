#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2225                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2225                           #+#        #+#      #+#     #
#    Solved: 2024/02/21 15:52:40 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (N+1) for _ in range(K+1)]
mod = 1000000000

for i in range(K+1):
  dp[i][0] = 1
for i in range(1, K+1):
  for j in range(1, N+1):
    dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % mod

print(dp[K][N])