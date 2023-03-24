"""
문제제목:
1이 될 때까지

문제설명:
- 수 n, k를 입력받는다.
- n이 1이 될 때까지 다음 두 과정 중 하나를 반복한다.
    1. N에서 1을 뺀다.
    2. N을 K로 나눈다. (N이 K로 나누어 떨어질 때만 선택 가능)
- N이 1이 될 때까지 반복하고, 반복한 횟수를 출력한다.

입력예시:
25 5

출력예시:
2
"""

n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n /= k
        count += 1

print(count)

"""
답안 예시:
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    n // k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
"""
