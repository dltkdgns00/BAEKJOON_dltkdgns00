#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9461                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9461                           #+#        #+#      #+#     #
#    Solved: 2024/02/21 12:23:41 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

P = [0] * 101

P[1], P[2], P[3]= 1, 1, 1
for i in range(4,101):
  P[i] = P[i-3] + P[i-2]

T = int(input())

for _ in range(T):
  N = int(input())
  print(P[N])