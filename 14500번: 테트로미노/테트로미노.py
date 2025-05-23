#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14500                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14500                          #+#        #+#      #+#     #
#    Solved: 2025/05/23 13:32:28 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
max_val = 0

# 방향: 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, depth, total):
    global max_val
    if depth == 4:
        max_val = max(max_val, total)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check_t_shape(x, y):
    global max_val
    # 중심 + 3면 덧붙인 ㅗ, ㅏ, ㅜ, ㅓ 모양들
    for shape in [
        [(0, 0), (-1, 0), (0, -1), (0, 1)],  # ㅗ
        [(0, 0), (1, 0), (0, -1), (0, 1)],   # ㅜ
        [(0, 0), (-1, 0), (1, 0), (0, 1)],   # ㅏ
        [(0, 0), (-1, 0), (1, 0), (0, -1)]   # ㅓ
    ]:
        try:
            total = sum(board[x + dx][y + dy] for dx, dy in shape)
            max_val = max(max_val, total)
        except IndexError:
            continue

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_t_shape(i, j)

print(max_val)