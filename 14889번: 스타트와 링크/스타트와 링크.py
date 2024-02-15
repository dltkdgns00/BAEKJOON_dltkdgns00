#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14889                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14889                          #+#        #+#      #+#     #
#    Solved: 2024/02/15 17:16:41 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())
ability_board = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')

def calculate_diff(start_team):
    global min_diff
    link_team = [i for i in range(N) if i not in start_team]
    start_ability, link_ability = 0, 0

    for i in start_team:
        for j in start_team:
            start_ability += ability_board[i][j]
    for i in link_team:
        for j in link_team:
            link_ability += ability_board[i][j]

    diff = abs(start_ability - link_ability)
    min_diff = min(min_diff, diff)

def divide_teams(idx, start_team):
    if len(start_team) == N // 2:
        calculate_diff(start_team)
        return

    for i in range(idx, N):
        if i not in start_team:
            start_team.append(i)
            divide_teams(i+1, start_team)
            start_team.pop()

divide_teams(0, [])
print(min_diff)