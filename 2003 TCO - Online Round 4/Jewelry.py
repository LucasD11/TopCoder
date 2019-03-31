# -*- coding: utf-8 -*-
import copy


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


Cnk = gen_cnk(30)


class Jewelry:
    def _first_i_item_sum_to_j(self, values):
        total = sum(values)
        result = [{} for _ in range(len(values))]
        for i, value in enumerate(values):
            result[i][value] = 1
            if i == 0:
                continue
            for prev in result[i-1]:
                result[i][prev + value] = result[i-1][prev]
            for prev in result[i-1]:
                if prev not in result[i]:
                    result[i][prev] = 0
                result[i][prev] += result[i-1][prev]
        return result

    def howMany(self, values):
        values = sorted(values)
        max_total = sum(values)

        B = self._first_i_item_sum_to_j(values)
        F = self._first_i_item_sum_to_j(values[::-1])

        result = 0
        for i in range(len(values)-1):
            v_i = values[i]
            n = values.count(v_i)
            k = values[:i+1].count(v_i)
            for total in F[len(values) - i - 2]:
                if total - v_i * k == 0:
                    result += Cnk[n][k] * F[len(values) - i - 2][total]
                elif total - v_i * k > 0 and i - k >= 0:
                    result += Cnk[n][k] * F[len(values) - i - 2][total] * B[i - k].get(total - v_i * k, 0)
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

def do_test(values, __expected):
    startTime = time.time()
    instance = Jewelry()
    exception = None
    try:
        __result = instance.howMany(values);
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
    sys.stdout.write("Jewelry (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Jewelry.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            values = []
            for i in range(0, int(f.readline())):
                values.append(int(f.readline().rstrip()))
            values = tuple(values)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(values, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1553003851
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
