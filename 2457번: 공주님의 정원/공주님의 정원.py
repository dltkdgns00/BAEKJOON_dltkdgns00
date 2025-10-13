#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2457                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2457                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 01:03:17 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

flowers = []

for _ in range(N):
  sm, sd, em, ed = map(int, input().split())
  flowers.append((sm*100+sd,em*100+ed))

flowers.sort(key= lambda x: (x[0], -x[1]))

TARGET_START, TARGET_END = 301, 1130

target = TARGET_START

idx = 0
count = 0

while target <= TARGET_END:
  found = False
  max_end = target
  while idx < N and flowers[idx][0] <= target:
    found = True
    max_end = max(flowers[idx][1], max_end)
    idx += 1
  
  if not found:
    print(0)
    sys.exit(0)
  else:
    count += 1
    target = max_end
  
  if target > TARGET_END:
    print(count)
    sys.exit(0)

print(0)