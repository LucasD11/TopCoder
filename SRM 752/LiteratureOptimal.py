# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class LiteratureOptimal:
    def minTurns(self, N, Teja, history):
        known = [False for _ in range(3 * N)]
        Teja = [i - 1 for i in Teja]
        Vinay = set()
        Sohail = set()
        history = [i - 1 for i in history]

        for c in Teja:
            known[c] = True

        for index, c in enumerate(history):
            if index % 3 == 0:
                continue
            if known[c]:
                continue

            known[c] = True
            if index % 3 == 1:
                Sohail.add(c)
            else:
                Vinay.add(c)

        Vinay_left = N - len(Vinay)
        Sohail_left = N - len(Sohail)

        if Vinay_left == 0 or Sohail_left == 0:
            return 0

        result = []
        l = len(history) % 3
        return min(
            3 * (Vinay_left - 1) + 3 - l,
            3 * (Sohail_left - 1) + ((2 - l) if (2 - l) % 3 else 3)
        )


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

def do_test(N, Teja, history, __expected):
    startTime = time.time()
    instance = LiteratureOptimal()
    exception = None
    try:
        __result = instance.minTurns(N, Teja, history);
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
    sys.stdout.write("LiteratureOptimal (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LiteratureOptimal.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            Teja = []
            for i in range(0, int(f.readline())):
                Teja.append(int(f.readline().rstrip()))
            Teja = tuple(Teja)
            history = []
            for i in range(0, int(f.readline())):
                history.append(int(f.readline().rstrip()))
            history = tuple(history)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, Teja, history, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1551913095
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
