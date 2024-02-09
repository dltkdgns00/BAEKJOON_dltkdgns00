#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9663                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9663                           #+#        #+#      #+#     #
#    Solved: 2024/02/07 21:46:57 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N = int(input())

visited = {idx : False for idx in range(N)}
arr = {idx : 0 for idx in range(N)}
count = 0

def isDigonal(k):
  i = k - 1
  while i >= 0:
    if abs(k - i) == abs(arr[k] - arr[i]):
      return True
    i -= 1
  return False

def queen(k):
  global count

  if k == N:
    count += 1
    return

  for i in range(N):
    if not visited[i]:
      visited[i] = True
      arr[k] = i
      if not isDigonal(k):
        queen(k + 1)
      visited[i] = False

queen(0)

print(count)