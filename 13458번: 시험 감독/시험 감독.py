#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13458                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13458                          #+#        #+#      #+#     #
#    Solved: 2025/05/22 13:34:42 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = N

for i in range(len(A)):
  if A[i] <= B:
    continue
  else:
    result += (A[i] - B + C - 1) // C

print(int(result))