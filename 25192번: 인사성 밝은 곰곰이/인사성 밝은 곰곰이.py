#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25192                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25192                          #+#        #+#      #+#     #
#    Solved: 2024/02/02 17:20:00 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

N = int(sys.stdin.readline().rstrip())
chat = set()
count = 0

for _ in range(N):
  str = sys.stdin.readline().rstrip()
  if str == 'ENTER':
    chat.clear()
  elif str not in chat:
    chat.add(str)
    count += 1

print(count)