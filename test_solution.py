import pytest
from solution import Solution

@pytest.fixture
def solver():
    return Solution()

def test_majority_simple(solver):
    assert solver.majorityElement([3, 2, 3]) == 3
    assert solver.majorityElement([2,2,1,1,1,2,2]) == 2

def test_all_same(solver):
    assert solver.majorityElement([5,5,5,5]) == 5

def test_single_element(solver):
    assert solver.majorityElement([42]) == 42

def test_negative_and_zero(solver):
    assert solver.majorityElement([0, -1, 0, 0, 1, 0, 0]) == 0

def test_type_mismatch_raises(solver):
    with pytest.raises(TypeError):
        solver.majorityElement([1, "a", 1])
