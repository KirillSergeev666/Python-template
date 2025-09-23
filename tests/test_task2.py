import io
import sys

def solve():
    X, Y, Z = map(int, input().split())
    pencil_price = 3
    pen_price = pencil_price + 2
    marker_price = pen_price + 7
    total = X * pencil_price + Y * pen_price + Z * marker_price
    print(total)

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("2 3 1\n") == "23"
def test_case2():
    assert run_io("1 1 1\n") == "15"
def test_case3():
    assert run_io("0 5 2\n") == "31"
