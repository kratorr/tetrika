"""
тут конечно можно сделать через str.index('0'), но это O(n)
поэтому применил бинарный поиск сложность O(log n)

"""

def task(a: str) -> int:
    n = len(a)
    left = -1
    right = n

    while right - left > 1:
        middle = (int(left) + int(right)) // 2
        if int(a[middle]) == 0:
            right = middle
        else:
            left = middle
    return right


if __name__ == '__main__':
    a = "111111111111111111111111100000000"
    print(task(a))
