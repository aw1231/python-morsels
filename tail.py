def tail(input: list, n: int) -> list:
    if n <= 0:
        return []
    else:
        return list(input[-n:])
