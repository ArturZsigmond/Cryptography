import time
import statistics as stats
import math
# fast version of Euclid's algorithm
def gcd_euclid_fast(a, b):
    return a if b == 0 else gcd_euclid_fast(b, a % b)
# robust but slow version of Euclid's algorithm
def gcd_euclid_slow(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        if a % b == 0:
            return b
        return gcd_euclid_slow(a - b, b)
    if b % a == 0:
        return a
    return gcd_euclid_slow(a, b - a)
# very basic version (trial division from min(a,b) down to 1)
def gcd_basic(a, b):
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    if a == b: return a
    if a > b and a % b == 0: return b
    if b > a and b % a == 0: return a

    d = min(a, b)
    while d > 1 and ((a % d != 0) or (b % d != 0)):
        d -= 1
    return d


ALGORITHMS = [
    ("euclid_fast", gcd_euclid_fast),
    ("euclid_slow", gcd_euclid_slow),
    ("basic",       gcd_basic),
]


def make_inputs():
    # chosen to keep gcds reasonably large (so gcd_basic isn’t painfully slow)
    inputs = [
        (8, 12),            # gcd 4
        (27, 18),           # 9
        (840, 630),         # 210
        (20_000, 80_000),   # 20_000
        (1000, 1_000_000),  # 1000
        (640_000, 1_000_000),  # 160_000
        (999_000, 666_000), # 333_000
        (720_720, 27_720),  # 27_720
        (882_000, 378_000), # 126_000
        (999_936, 124_992), # 124_992 
        (599_946, 899_919), # 299_973  
        (456_789, 123_456), # 3  
    ]
    # sanitize to be ≥ 1 for gcd_basic
    inputs = [(max(1, a), max(1, b)) for a, b in inputs]
    return inputs

# ---------- benchmark helpers ----------
def time_once(fn, args):
    start = time.perf_counter_ns()
    fn(*args)
    end = time.perf_counter_ns()
    return end - start

def bench(fn, args, repeats=9, warmup=2):
    for _ in range(warmup):
        fn(*args)
    times = [time_once(fn, args) for _ in range(repeats)]
    return int(stats.median(times)) / 1_000.0  # μs

# ---------- run ----------
def main():
    inputs = make_inputs()
    print(f"Comparing {len(ALGORITHMS)} algorithms on {len(inputs)} inputs (≤ 1,000,000).\n")
    header = f"{'input':>22}  {'gcd':>10}  " + "  ".join([f"{name:>14}" for name, _ in ALGORITHMS])
    print(header)
    print("-" * len(header))

    for a, b in inputs:
        expected = math.gcd(a, b)

        # correctness check
        ok = True
        for name, fn in ALGORITHMS:
            try:
                out = fn(a, b)
                if out != expected:
                    print(f"{str((a,b)):>22}  {'ERR':>10}  " +
                          "  ".join([f'{"-":>14}' for _ in ALGORITHMS]) +
                          f"   <-- {name} returned {out}, expected {expected}")
                    ok = False
                    break
            except Exception as e:
                print(f"{str((a,b)):>22}  {'ERR':>10}  " +
                      "  ".join([f'{"-":>14}' for _ in ALGORITHMS]) +
                      f"   <-- {name} raised {type(e).__name__}: {e}")
                ok = False
                break
        if not ok:
            continue

        # timing (median μs)
        medians = [bench(fn, (a, b)) for _, fn in ALGORITHMS]
        row = [f"{str((a,b)):>22}", f"{expected:>10}"] + [f"{m:>10.2f} μs" for m in medians]
        print("  ".join(row))

    print("\nTimes are median over repeats (μs).")
    print("Note: Very small gcds on large numbers make gcd_basic much slower;")
    print("this set avoids worst co-prime pairs to keep things reasonable under the 1e6 cap.")

if __name__ == "__main__":
    main()
