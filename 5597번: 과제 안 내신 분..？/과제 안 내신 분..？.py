#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5597                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5597                           #+#        #+#      #+#     #
#    Solved: 2024/02/01 15:45:11 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

students = list(range(1, 31))

for i in range(28):
  students.remove(int(input()))

for i in students:
  print(i)