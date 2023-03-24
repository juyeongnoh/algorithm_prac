"""
문제제목:
큰 수의 법칙

문제설명:
- 배열의 크기 n, 숫자가 더해지는 횟수 m, 그리고 k가 주어진다.
- 그리고 n 크기의 배열을 입력받는다.
- 배열에서 가장 큰 수를 m만큼 더한 값을 반환하는데, k번 이상 연속으로 더해질 수 없다.

입력예시:
5 8 3
2 4 5 4 6

출력예시:
46
"""

n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
result = 0

first = max(data)
data.remove(first)
second = max(data)

result += first * (m - m % k)
result += second * (m % k)

print(result)

"""
# 단순하게 푸는 답안:
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
"""
