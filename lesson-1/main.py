from functools import lru_cache

@lru_cache
def f(i, m):
    if i > m:
        return 100000
    if i == m:
        return arr[i]
    return min(f(i+1, m), f(i+2, m)) + arr[i]


n = int(input())
arr = list(map(int, input().split()))
print(min(f(0, n-1), f(1, n-1)))
