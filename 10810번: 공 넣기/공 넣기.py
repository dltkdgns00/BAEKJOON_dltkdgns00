#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10810                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10810                          #+#        #+#      #+#     #
#    Solved: 2024/02/01 14:46:47 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
basket = [0] * N

for _ in range(M):
  i, j, k = map(int, input().split())
  while i <= j:
    basket[i - 1] = k
    i += 1

for idx in range(0, N):
  print(basket[idx], end=" ")