#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2025/10/11 07:52:05 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in graph:
  graph[i].sort()

visited = set()

def dfs(node):
  visited.add(node)
  print(node, end=' ')
  for nxt in graph[node]:
    if nxt not in visited:
      dfs(nxt)

def bfs(start):
  q = deque([start])
  visited = set([start])
  while q:
    cur = q.popleft()
    print(cur, end=' ')
    for nxt in graph[cur]:
      if nxt not in visited:
        visited.add(nxt)
        q.append(nxt)

dfs(V)
print()
bfs(V)