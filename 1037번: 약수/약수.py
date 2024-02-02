#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1037                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1037                           #+#        #+#      #+#     #
#    Solved: 2024/02/02 16:10:46 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
divisors = list(map(int,input().split()))

divisors.sort()

print(divisors[0] * divisors[len(divisors) - 1])