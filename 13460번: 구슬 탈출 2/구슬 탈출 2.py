#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13460                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dltkdgns00 <boj.kr/u/dltkdgns00>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13460                          #+#        #+#      #+#     #
#    Solved: 2025/05/21 15:43:38 by dltkdgns00    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

# 보드를 한번 기울일 때 빨간 구슬과 파란 구슬이 이동하는데 벽이나 구멍을 만날 때 이동을 멈춤
def move(x, y, dx, dy, board):
  count = 0
  while board[x + dx][y + dy] != '#' and board[x][y] != 'O': # '#(벽)', 'O(구멍)'이 아닐 때 이동
        x += dx
        y += dy # 이동
        count += 1 # 몇번 이동 했는지 카운트
        if board[x][y] == 'O': # 구슬이 구멍에 빠지면 break
            break
  return x, y, count

def solve(board, n, m):
  # 4차원 배열 생성
  visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
  q = deque()

  # R, B 위치 찾기
  for i in range(n):
    for j in range(m):
      if board[i][j] == 'R':
        rx, ry = i, j
      elif board[i][j] == 'B':
        bx, by = i, j

  q.append((rx, ry, bx, by, 0))
  visited[rx][ry][bx][by] = True

  # 방향을 정의
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while q:
    rx, ry, bx, by, depth = q.popleft()  # 큐에서 하나씩 꺼내기
    if depth >= 10:  # 10번 넘으면 실패 조건
      break

    for i in range(4):
      nrx, nry, rc = move(rx, ry, dx[i], dy[i], board)  # 빨간 구슬 이동
      nbx, nby, bc = move(bx, by, dx[i], dy[i], board)  # 파란 구슬 이동

      # 파란 구슬이 빠지면 실패
      if board[nbx][nby] == 'O':
        continue

      # 빨간 구슬만 빠지면 성공
      if board[nrx][nry] == 'O':
        return depth + 1

      # 두 구슬이 같은 위치에 있을 경우, 더 많이 이동한 구슬을 한 칸 뒤로
      if nrx == nbx and nry == nby:
        if rc > bc:
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]

      if not visited[nrx][nry][nbx][nby]: # 방문하지 않은 위치라면
        visited[nrx][nry][nbx][nby] = True # 방문 표시하고
        q.append((nrx, nry, nbx, nby, depth + 1)) # 현재 위치를 큐에 넣음

  return -1

# 입력 처리
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
print(solve(board, n, m))