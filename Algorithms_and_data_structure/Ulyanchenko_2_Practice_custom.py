to_count = 100


def countdown(n):
    if n >= 0:
        print(n)
        n -= 1
        countdown(n)


countdown(to_count)
