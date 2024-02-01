#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25206                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25206                          #+#        #+#      #+#     #
#    Solved: 2024/02/01 18:28:21 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

sum = float(0)
score = float(0)
credit = int(0)

for _ in range(20):
  _list = list(input().split())
  match _list[2]:
    case 'A+':
      score = 4.5
    case 'A0':
      score = 4.0
    case 'B+':
      score = 3.5
    case 'B0':
      score = 3.0
    case 'C+':
      score = 2.5
    case 'C0':
      score = 2.0
    case 'D+':
      score = 1.5
    case 'D0':
      score = 1.0
    case 'F':
      score = 0.0
    case 'P':
      continue

  sum += score * float(_list[1])
  credit += float(_list[1])

print(sum / credit)