#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14501                          #+#        #+#      #+#     #
#    Solved: 2025/05/22 14:22:30 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())

T, P = [], []

for i in range(N):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

dp = [0] * (N + 1)

# 뒤에서부터 확인 (퇴사일에 가까운 날부터)
for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])