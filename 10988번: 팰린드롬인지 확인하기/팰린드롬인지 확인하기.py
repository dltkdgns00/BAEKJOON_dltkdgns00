#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10988                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10988                          #+#        #+#      #+#     #
#    Solved: 2024/02/01 17:06:06 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

str = list(input())

if list(reversed(str)) == str:
  print(1)
else:
  print(0)