def funk(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return funk(n - 1, k) + funk(n - 1, k - 1)


n, k = map(int, input().split())
print(funk(n, k))
