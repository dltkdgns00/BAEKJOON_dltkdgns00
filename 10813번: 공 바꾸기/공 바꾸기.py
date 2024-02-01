#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10813                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10813                          #+#        #+#      #+#     #
#    Solved: 2024/02/01 15:35:45 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
basket = []

for i in range(1, N + 1):
  basket.append(i)

for _ in range(M):
  i, j = map(int, input().split())
  temp = basket[i - 1]
  basket[i - 1] = basket[j - 1]
  basket[j - 1] = temp

for i in range(N):
  print(basket[i], end=" ")