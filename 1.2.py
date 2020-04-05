# return the index of the smallest window to be sorted
# for example give [3,7,5,6,9] should return (1,3)

ray = [1, 2, 3, 5, 4, 6, 7]


def window(array):
    left, right = None, None
    s = sorted(array)
    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i
    return left, right


print(window(ray))


def windows(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float('inf'), float('inf')

    for i in range(n):
        max_seen = max(max_seen, array[i])
        print(max_seen)
        if array[i] < max_seen:
            print(array[i])
            right = i
    #
    # for i in range(n-1,-1,-1):
    #     min_seen = min(min_seen,array[i])
    #     if(array[i]>min_seen):
    #         left = i

windows(ray)
