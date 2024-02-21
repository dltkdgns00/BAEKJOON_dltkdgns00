#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6550                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6550                           #+#        #+#      #+#     #
#    Solved: 2024/02/21 23:08:52 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

while True:
  strings = input().rstrip()
  if not strings:
    break
  str1, str2 = strings.split()
  i1, i2 = 0, 0
  while i1 < len(str1) and i2 < len(str2):
    if str1[i1] == str2[i2]:
        i1 += 1
    i2 += 1
  if i1 == len(str1):
    print("Yes")
  else:
    print("No")