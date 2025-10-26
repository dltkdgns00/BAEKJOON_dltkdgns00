#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20055                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20055                          #+#        #+#      #+#     #
#    Solved: 2025/10/21 20:52:10 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

robots = deque([0] * (2 * N))
belt = deque(map(int, input().split()))

count = 0

def belt_move():
  # move = belt.pop()
  # belt.appendleft(move)
  belt.rotate()
  # move = robots.pop()
  # robots.appendleft(move)
  robots.rotate()
  robots[N-1] = 0 


def robot_move(idx):
  if belt[idx + 1] > 0 and robots[idx + 1] == 0:
    robots[idx] = 0
    robots[idx + 1] = 1
    belt[idx + 1] -= 1
  robots[N-1] = 0 


while True:
  belt_move()
  for idx in range(N-2, -1, -1):
    if robots[idx] == 1:
      robot_move(idx)

  if belt[0] > 0 and robots[0] == 0:
    robots[0] = 1
    belt[0] -= 1

  count += 1
  if belt.count(0) >= K:
    break

print(count)