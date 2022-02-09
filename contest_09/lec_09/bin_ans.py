"""the task about diplomas"""

n, m, k = map(int, input().split())

left = 0
right = (n + m) * k

while right - left > 1:
    middle = (right + left) // 2
    if (middle // n) * (middle // m) < k:
        left = middle
    else:
        right = middle

print(right)
