#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2024/02/15 15:02:55 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, mul, div):
  global maximum
  global minimum

  if depth == N:
    maximum = max(total, maximum)
    minimum = min(total, minimum)
    return
  
  if plus:
    dfs(depth + 1, total + numbers[depth], plus - 1, minus, mul, div)
  if minus:
    dfs(depth + 1, total - numbers[depth], plus, minus - 1, mul, div)
  if mul:
    dfs(depth + 1, total * numbers[depth], plus, minus, mul - 1, div)
  if div:
    dfs(depth + 1, int(total / numbers[depth]), plus, minus, mul, div - 1)

dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(maximum)
print(minimum)