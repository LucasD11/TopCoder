# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class CCChecker2:
    def check(self, n, startRow, startCol, destRow, destCol, moveStartRow, moveStartCol, moveDestRow, moveDestCol):
        board = [[None for _ in range(n)] for _ in range(n)]
        for i, j, di, dj in zip(startRow, startCol, destRow, destCol):
            i, j, di, dj = i-1, j-1, di-1, dj-1
            if board[i][j] is not None:
                return 'invalid'
            board[i][j] = (di, dj)

        for i, j, di, dj in zip(moveStartRow, moveStartCol, moveDestRow, moveDestCol):
            i, j, di, dj = i-1, j-1, di-1, dj-1
            for v in (i, j, di, dj):
                if v < 0 or v >= n:
                    return 'invalid'
            if board[i][j] is None:
                return 'invalid'
            if board[di][dj] is not None:
                return 'invalid'
            if abs(i - di) + abs(j - dj) != 1:
                return 'invalid'
            board[di][dj] = board[i][j]
            board[i][j] = None

        for i in range(n):
            for j in range(n):
                if board[i][j] is None:
                    continue
                if board[i][j] != (i, j):
                    return 'invalid'
        return 'valid'

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(n, startRow, startCol, destRow, destCol, moveStartRow, moveStartCol, moveDestRow, moveDestCol, __expected):
    startTime = time.time()
    instance = CCChecker2()
    exception = None
    try:
        __result = instance.check(n, startRow, startCol, destRow, destCol, moveStartRow, moveStartCol, moveDestRow, moveDestCol);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("CCChecker2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CCChecker2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            n = int(f.readline().rstrip())
            startRow = []
            for i in range(0, int(f.readline())):
                startRow.append(int(f.readline().rstrip()))
            startRow = tuple(startRow)
            startCol = []
            for i in range(0, int(f.readline())):
                startCol.append(int(f.readline().rstrip()))
            startCol = tuple(startCol)
            destRow = []
            for i in range(0, int(f.readline())):
                destRow.append(int(f.readline().rstrip()))
            destRow = tuple(destRow)
            destCol = []
            for i in range(0, int(f.readline())):
                destCol.append(int(f.readline().rstrip()))
            destCol = tuple(destCol)
            moveStartRow = []
            for i in range(0, int(f.readline())):
                moveStartRow.append(int(f.readline().rstrip()))
            moveStartRow = tuple(moveStartRow)
            moveStartCol = []
            for i in range(0, int(f.readline())):
                moveStartCol.append(int(f.readline().rstrip()))
            moveStartCol = tuple(moveStartCol)
            moveDestRow = []
            for i in range(0, int(f.readline())):
                moveDestRow.append(int(f.readline().rstrip()))
            moveDestRow = tuple(moveDestRow)
            moveDestCol = []
            for i in range(0, int(f.readline())):
                moveDestCol.append(int(f.readline().rstrip()))
            moveDestCol = tuple(moveDestCol)
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(n, startRow, startCol, destRow, destCol, moveStartRow, moveStartCol, moveDestRow, moveDestCol, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1553094320
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
