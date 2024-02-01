#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10811                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10811                          #+#        #+#      #+#     #
#    Solved: 2024/02/01 16:04:12 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())
basket = list(range(1, N + 1))

for _ in range(M):
  i, j = map(int, input().split())
  temp = basket[i - 1 : j]
  temp.reverse()
  basket[i - 1 : j] = temp

for n in basket:
  print(n, end=" ")