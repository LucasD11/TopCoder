# def cnk_generator(max_n):
#     result = [0 for _]

def cnk(k, n):
    """
    Get cnk by cnk(k, n)
    """
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    for i in range(1, k+1):
        result = result // i
    return result


def gen_cnk(max_n):
    """
    Get cnk by gen_cnk()[n][k]
    """
    nk = [[0 for _ in range(max_n+1)] for _ in range(max_n+1)]
    nk[0][0] = 1
    for n in range(1, max_n+1):
        nk[n][0] = 1
        for k in range(1, n+1):
            nk[n][k] = nk[n-1][k-1] + nk[n-1][k]
    return nk


def test():
    for k, n in [
            (1, 3),
            (2, 3),
            (1, 4),
            (2, 4),
            (3, 4),
            (4, 4)
    ]:
        print(k, n, cnk(k, n), gen_cnk(5)[n][k])


if __name__ == '__main__':
    test()
