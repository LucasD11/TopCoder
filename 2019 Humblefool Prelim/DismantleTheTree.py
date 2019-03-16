# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class DismantleTheTree:
    def dismantle(self, N, X, Y, weight):
        erased = [False for _ in weight]
        W = 0
        while False in erased:
            nodes = []
            index = erased.index(False)
            w = weight[index]
            erased[index] = True
            nodes.append(X[index])
            nodes.append(Y[index])
            l = 0
            while l != len(set(nodes)):
                l = len(set(nodes))
                for j in range(N-1):
                    if (X[j] in nodes or Y[j] in nodes) and \
                            erased[j] == False and \
                            weight[j] == w and \
                            nodes.count(X[j]) < 2 and \
                            nodes.count(Y[j]) < 2:
                        erased[j] = True
                        nodes.append(X[j])
                        nodes.append(Y[j])
            W += w
        return W


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

def do_test(N, X, Y, weight, __expected):
    startTime = time.time()
    instance = DismantleTheTree()
    exception = None
    try:
        __result = instance.dismantle(N, X, Y, weight);
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
    sys.stdout.write("DismantleTheTree (600 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("DismantleTheTree.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            X = []
            for i in range(0, int(f.readline())):
                X.append(int(f.readline().rstrip()))
            X = tuple(X)
            Y = []
            for i in range(0, int(f.readline())):
                Y.append(int(f.readline().rstrip()))
            Y = tuple(Y)
            weight = []
            for i in range(0, int(f.readline())):
                weight.append(int(f.readline().rstrip()))
            weight = tuple(weight)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, X, Y, weight, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1552714436
    PT, TT = (T / 60.0, 75.0)
    points = 600 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
