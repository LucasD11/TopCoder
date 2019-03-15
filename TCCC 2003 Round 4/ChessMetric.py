# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ChessMetric:
    def howMany(self, size, start, end, numMoves):
        board = [[0 for _ in range(size)] for _ in range(size)]
        board[start[0]][start[1]] = 1
        new_board = [[0 for _ in range(size)] for _ in range(size)]
        for _ in range(numMoves):
            for i in range(size):
                for j in range(size):
                    new_board[i][j] = sum(
                        board[x][y] for x, y in (
                            (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1),
                            (i+1, j-1), (i+1, j), (i+1, j+1),
                            (i-1, j+2), (i-1, j-2), (i+1, j-2), (i+1, j+2),
                            (i+2, j-1), (i-2, j-1), (i+2, j+1), (i-2, j+1))
                        if (x >= 0 and y >= 0 and x < size and y < size)
                    )
            board, new_board = new_board, board
        return board[end[0]][end[1]]


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

def do_test(size, start, end, numMoves, __expected):
    startTime = time.time()
    instance = ChessMetric()
    exception = None
    try:
        __result = instance.howMany(size, start, end, numMoves);
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
    sys.stdout.write("ChessMetric (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ChessMetric.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            size = int(f.readline().rstrip())
            start = []
            for i in range(0, int(f.readline())):
                start.append(int(f.readline().rstrip()))
            start = tuple(start)
            end = []
            for i in range(0, int(f.readline())):
                end.append(int(f.readline().rstrip()))
            end = tuple(end)
            numMoves = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(size, start, end, numMoves, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1552610081
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
