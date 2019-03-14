# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


class Flower:
    def __init__(self, height, bloom, wilt):
        self.height = height
        self.bloom = bloom
        self.wilt = wilt
        self.deps = []

    def remove_dependencies(self, value):
        if value in self.deps:
            self.deps.remove(value)

class FlowerGarden:
    def _max_without_deps(self, flowers):
        result = None
        for flower in flowers:
            if flower.deps:
                continue
            if result is None or result.height < flower.height:
                result = flower
        return result

    def _add_deps(self, flowers):
         for f1 in flowers:
            for f2 in flowers:
                if f1 is f2:
                    continue
                if f1.height > f2.height:
                    continue
                if self._intersect(f1, f2):
                    f2.deps.append(f1.height)

    def _intersect(self, f1, f2):
        return not (f1.wilt < f2.bloom or f2.wilt < f1.bloom)

    def getOrdering(self, height, bloom, wilt):
        flowers = [Flower(h, b, w) for h, b, w in zip(height, bloom, wilt)]
        self._add_deps(flowers)

        order = []
        while flowers:
            next_flower = self._max_without_deps(flowers)

            for f in flowers:
                f.remove_dependencies(next_flower.height)

            order.append(next_flower.height)
            flowers.remove(next_flower)

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

    T = time.time() - 1552523779
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
