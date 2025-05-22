#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3190                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3190                           #+#        #+#      #+#     #
#    Solved: 2025/05/22 15:17:28 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

N = int(input())
K = int(input())
apple = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

L = int(input())
pivot = [input().split() for _ in range(L)]
pivot = [(int(t), p) for t, p in pivot]

snake = deque([(0, 0)])
time = 0

# 0(오), 1(아래), 왼(2), 3(위)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

while True:
  time += 1

  head_x, head_y = snake[-1]
  nx = head_x + dx[dir]
  ny = head_y + dy[dir]

  if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake:
    break

  snake.append((nx, ny))

  if (nx, ny) in apple:
    apple.remove((nx, ny))
  else:
    snake.popleft()

  if pivot and pivot[0][0] == time:
    dir = (dir + 1) % 4 if pivot[0][1] == 'D' else (dir - 1) % 4
    pivot.pop(0)


print(time)