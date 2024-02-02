#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2108                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2108                           #+#        #+#      #+#     #
#    Solved: 2024/02/02 19:59:38 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input=sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
  number = int(input())
  numbers.append(number)

numbers.sort()

print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])

dic=dict()
for i in numbers:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

max_number=max(dic.values())
max_dic=[]

for i in dic:
    if max_number==dic[i]:
        max_dic.append(i)

if len(max_dic)>1:
    print(max_dic[1])
else:
    print(max_dic[0])

print(max(numbers) - min(numbers))