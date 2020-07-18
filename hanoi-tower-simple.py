def hanoi(n, a, b, c):
    global stepCount
    if n > 0:
        hanoi(n-1, a, c, b)
        stepCount += 1
        print('stepCount: {}'.format(stepCount))
        print('{} --> {}'.format(a, c))
        hanoi(n-1, b, a, c)


stepCount = 0
hanoi(2, 'A', 'B', 'C')