#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11047                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11047                          #+#        #+#      #+#     #
#    Solved: 2024/02/23 18:29:00 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
count = 0
temp = N-1

while K > 0 and temp >= 0:
  coin = lst[temp]
  if coin <= K:
    count += K // coin
    K %= coin
  temp -= 1

print(count)