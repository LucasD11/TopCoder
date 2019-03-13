# -*- coding: utf-8 -*-
"""
height, bloom, wilt
"""
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class FlowerGarden:
    # TODO: Why is this problem a DP problem
    # TODO: Code is not elegant
    def _intersect(self, i, j, x, y):
        return not(j < x or y < i)

    def getOrdering(self, height, bloom, wilt):
        flowers = [[i, j, k, []] for i, j, k in zip(height, bloom, wilt)]
        flowers.sort(key=lambda x:x[0], reverse=True)
        for i, flower in enumerate(flowers):
            for j in range(i+1, len(flowers)):
                f2 = flowers[j]
                if self._intersect(flower[1], flower[2], f2[1], f2[2]):
                    flower[3].append(f2[0])

        order = []
        while flowers:
            choises = [i for i in flowers if not i[3]]
            choises.sort(key=lambda x:x[0], reverse=True)
            removed = choises[0]
            h = removed[0]
            for flower in flowers:
                if h in flower[3]:
                    flower[3].remove(h)
            order.append(h)

            index = 0
            for i, flower in enumerate(flowers):
                if flower[0] == h:
                    index = i

            flowers.pop(index)

        return order


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

def do_test(height, bloom, wilt, __expected):
    startTime = time.time()
    instance = FlowerGarden()
    exception = None
    try:
        __result = instance.getOrdering(height, bloom, wilt);
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
    sys.stdout.write("FlowerGarden (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("FlowerGarden.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            height = []
            for i in range(0, int(f.readline())):
                height.append(int(f.readline().rstrip()))
            height = tuple(height)
            bloom = []
            for i in range(0, int(f.readline())):
                bloom.append(int(f.readline().rstrip()))
            bloom = tuple(bloom)
            wilt = []
            for i in range(0, int(f.readline())):
                wilt.append(int(f.readline().rstrip()))
            wilt = tuple(wilt)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(height, bloom, wilt, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1552395506
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
