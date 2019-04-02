# -*- coding: utf-8 -*-
#
# Author: Lucas Dai <yuanzhendai@gmail.com>
#
"""
AxAyAzA

min(A + xAyAz, x + yAz
"""
import string, copy

class StripePainter:
    def minStrokes(self, stripes):
        self.cache = {}
        s = ''
        for c in stripes:
            if s and c == s[-1]:
                continue
            s += c
        return self._helper(s)

    def _helper(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        if s in self.cache:
            return self.cache[s]

        v = s[0]
        subs = [i for i in s.split(v) if i]
        result = 1 + self._helper2(subs, v)
        self.cache[s] = result
        return result

    def _helper2(self, subs, c):
        if len(subs) == 0:
            return 0
        if len(subs) == 1:
            return self._helper(subs[0])

        k = c + 'x'.join(subs)
        if k in self.cache:
            return self.cache[k]

        result = min([
            self._helper(c.join(subs[:i])) + self._helper2(subs[i:], c) for i in range(1, len(subs)+1)
        ])
        self.cache[k] = result
        return result


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

def do_test(stripes, __expected):
    startTime = time.time()
    instance = StripePainter()
    exception = None
    try:
        __result = instance.minStrokes(stripes);
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
    sys.stdout.write("StripePainter (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("StripePainter.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            stripes = f.readline().rstrip()
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(stripes, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1554092914
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
