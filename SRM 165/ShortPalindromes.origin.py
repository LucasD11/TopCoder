# -*- coding: utf-8 -*-
#
# Author: Lucas Dai <yuanzhendai@gmail.com>
#
import string, copy

class ShortPalindromes:
    def shortest(self, base):
        length = [[0] * 50 for _ in range(50)]
        pad = [[0] * 50 for _ in range(50)]
        n = len(base)

        for i in range(n):
            length[i][i] = 1
            length[i+1][i] = 0

        for l in range(2, n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                h, t = base[i], base[j]

                if h == t:
                    length[i][j] = length[i+1][j-1] + 2
                    pad[i][j] = 3
                    continue

                if length[i+1][j] < length[i][j-1]:
                    length[i][j] = length[i+1][j] + 2
                    pad[i][j] = 1
                elif length[i+1][j] > length[i][j-1]:
                    length[i][j] = length[i][j-1] + 2
                    pad[i][j] = 2
                else:
                    if h < t:
                        length[i][j] = length[i+1][j] + 2
                        pad[i][j] = 1
                    else:
                        length[i][j] = length[i][j-1] + 2
                        pad[i][j] = 2

        # Backtracking to get answer
        ans = ""
        i, j, l = 0, n-1, 0
        while i < j:
            v = pad[i][j]
            if v == 1:
                ans += base[i]
                i += 1
            elif v == 2:
                ans += base[j]
                j -= 1
            elif v == 3:
                ans += base[i]
                i += 1
                j -= 1
            l += 1

        if i == j:
            ans += base[i]

        return ans[:-1] + ans[::-1]


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

def do_test(base, __expected):
    startTime = time.time()
    instance = ShortPalindromes()
    exception = None
    try:
        __result = instance.shortest(base);
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
    sys.stdout.write("ShortPalindromes (1150 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ShortPalindromes.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            base = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(base, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1554297444
    PT, TT = (T / 60.0, 75.0)
    points = 1150 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
