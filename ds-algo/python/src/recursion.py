def fib(position):
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return position
    return fib(position - 1) + fib(position - 2)


def test():
    seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    assert fib(9) == seq[9]
    assert fib(11) == seq[11]
    assert fib(0) == seq[0]
    assert fib(12) == 144
    assert fib(-3) == -1

    print("All tests passed.")


if __name__ == "__main__":
    test()