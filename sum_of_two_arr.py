def sum_arrays(a, b):
    if not a:
        return b
    if not b:
        return a

    a = int("".join([str(x) for x in a]))
    b = int("".join([str(x) for x in b]))
    sum = a+b
    if sum < 0:
        sum = - sum
        sum = [int(x) for x in str(sum)]
        sum[0] *= -1
    else:
        sum = [int(x) for x in str(sum)]
    return sum
