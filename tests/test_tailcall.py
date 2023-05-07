"""Tail call optimization tests"""
import pytest
from lemprex.tailcall import async_tail_call
# @async_tail_call()
# def test_fib_optimize(i, current=0, subseq=1):
#     return current if i == 0 else test_fib_optimize(i - 1, subseq, current + subseq)

@pytest.mark.parametrize("i", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)])
@async_tail_call(active=True)
def test_fib_optimize(i, current=0, subseq=1):
    """Deterministic fibonacci test"""
    return current if i == 0 else test_fib_optimize(i - 1, subseq, current + subseq)
