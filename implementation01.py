"""
문제제목:
상하좌우

문제설명:
- 정사각형 (N * N) 크기의 공간 위에 있다.
- 각 사각형의 크기는 (1 * 1) 사이즈이다.
- 마지막 사각형의 좌표는 (N, N)이다.
- 처음 시작 위치는 (1, 1)이다.
- 사각형의 크기 N과 L, R, U, D로 이루어진 문자열을 입력받는다.
- L이면 왼쪽, R이면 오른쪽, U이면 위쪽, D이면 아래쪽으로 이동하는데 좌표를 벗어나면 안된다. (1, 1) ~ (N, N)

입력예시:
5
R R R U D D

출력예시:
3 4
"""

map_size = int(input())
command = input().split()
current_location = [1, 1]

for c in command:
    if c == "L":
        if 0 < current_location[1] - 1 < map_size:
            current_location[1] -= 1
    elif c == "R":
        if 0 < current_location[1] + 1 < map_size:
            current_location[1] += 1
    elif c == "U":
        if 0 < current_location[0] - 1 < map_size:
            current_location[0] -= 1
    elif c == "D":
        if 0 < current_location[0] + 1 < map_size:
            current_location[0] += 1
    print(current_location)

print(current_location[0], current_location[1])

"""
답안 예시:
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

print(x, y)
"""
