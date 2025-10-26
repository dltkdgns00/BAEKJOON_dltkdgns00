#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17140                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17140                          #+#        #+#      #+#     #
#    Solved: 2025/10/22 13:21:30 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def row_oper(row):
  cnt = Counter(x for x in row if x != 0)
  pairs = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
  flat = []
  for num, t in pairs:
    flat.append(num)
    flat.append(t)
  return flat[:100]

def pad_rows(rows):
  if not rows:
    return rows
  m = 0
  for row in rows:
    if len(row) > m:
      m = len(row)
  if m > 100:
    m = 100
    rows = [row[:100] for row in rows]
  for i in range(len(rows)):
    if len(rows[i]) < m:
      rows[i] = rows[i] + [0]*(m - len(rows[i]))
  return rows

def operate_R(A):
  rows = [row_oper(row) for row in A]
  return pad_rows(rows)

def transpose(M):
  if not M or not M[0]:
    return []
  return [list(x) for x in zip(*M)]

def operate_C(A):
  T = transpose(A)
  T2 = operate_R(T)
  return transpose(T2)

time = 0
while time <= 100:
  if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
    print(time)
    break
  R, C = len(A), len(A[0]) if A and A[0] else 0
  if R >= C:
    A = operate_R(A)
  else:
    A = operate_C(A)
  time += 1
else:
  print(-1)