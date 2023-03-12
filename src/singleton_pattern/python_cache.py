from functools import cache, lru_cache


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=128)
def cached_fibonacci(n):
    if n < 2:
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


if __name__ == "__main__":
    import time

    start = time.time()
    fibonacci(30)
    print(f"fibonacci(30) took {time.time() - start} seconds")

    start = time.time()
    cached_fibonacci(30)
    print(f"cached_fibonacci(30) took {time.time() - start} seconds")

    print(cached_fibonacci.cache_info())
