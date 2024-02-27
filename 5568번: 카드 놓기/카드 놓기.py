#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5568                           #+#        #+#      #+#     #
#    Solved: 2024/02/27 16:21:00 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().rstrip() for _ in range(n)]
visited = [False] * n
chosen = set()

def dfs(depth, number):
  if depth == k:
    chosen.add(number)
    return
  
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      dfs(depth + 1, number + cards[i])
      visited[i] = False

dfs(0, "")

print(len(chosen))