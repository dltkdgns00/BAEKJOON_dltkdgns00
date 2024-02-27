#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15686                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15686                          #+#        #+#      #+#     #
#    Solved: 2024/02/26 14:37:05 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
chickens = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]

min_distance = float('inf')

def get_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

def get_total_distance(chosen_chickens):
    total = 0
    for house in houses:
        distance = min(get_distance(house, chicken) for chicken in chosen_chickens)
        total += distance
    return total

def dfs(start, chosen):
  global min_distance

  if len(chosen) == M:
    min_distance = min(min_distance, get_total_distance(chosen))
    return
  for i in range(start, len(chickens)):
    dfs(i + 1, chosen + [chickens[i]])

dfs(0, [])

print(min_distance)