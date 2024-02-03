#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2024/02/03 09:33:19 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
words = {}

for _ in range(N):
  word = sys.stdin.readline().rstrip()
  if len(word) >= M:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

voca = sorted(words, key= lambda x: (-words[x], -len(x), x))

for i in voca:
  print(i)