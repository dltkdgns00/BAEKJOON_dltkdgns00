#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 26069                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/26069                          #+#        #+#      #+#     #
#    Solved: 2024/02/02 18:00:07 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())
dancing = {'ChongChong'}

for _ in range(N):
  A, B = sys.stdin.readline().rstrip().split()
  if A in dancing:
    dancing.add(B)
  if B in dancing:
    dancing.add(A)

print(len(dancing))