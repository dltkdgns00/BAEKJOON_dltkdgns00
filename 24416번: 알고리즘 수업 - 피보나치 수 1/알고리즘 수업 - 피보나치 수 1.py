#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24416                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24416                          #+#        #+#      #+#     #
#    Solved: 2024/02/18 22:50:56 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())
f = [0] * (n + 1)

count1 = 0
count2 = 0

def fib(n):
  global count1
  if n == 1 or n == 2:
    count1 += 1
    return 1
  else:
    return (fib(n-1) + fib(n-2))
  
def fibonacci(n):
  global count2
  f[0], f[1]= 1, 1
  for i in range(2,n):
    f[i] = f[i-1] + f[i-2]
    count2 += 1
  return f[n]

fib(n)
fibonacci(n)

print(count1,count2)