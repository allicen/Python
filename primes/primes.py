def primes():
    a = 2
    while True:
        count = a-1
        simple = True
        while count > 1:
            if a % count == 0:
                simple = False
            count -= 1
        if simple:
            yield a
        a += 1