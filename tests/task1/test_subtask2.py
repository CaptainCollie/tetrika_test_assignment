import pytest

from task1.subtask2 import task


@pytest.mark.parametrize(
    "test_input, expected",
    (
            ((1, 1, 2, 2, 3, 3, 4, 4), -1),
            ((1, 1, 2, 2, 2, 2, 4, 4), 0),
            ((1, 1, 3, 3, 2, 2, 4, 4), 1),
            ((2, 2, 1, 1, 4, 4, 3, 3), -1),
            ((1, 1, 4, 4, 3, 3, -4, -4), 4),
            ((-1, -1, -2, -2, -3, -3, -4, -4), -1),
            ((1, 1, 4, 4, 3, 3, 2, 2), 1),
            ((-3, -3, -2, -2, -1, -1, -4, -4), 1),
            ((1, 1, 3, 3, 0, 2, 2, 4), 1),
    )
)
def test_subtask1(test_input, expected):
    assert task(*test_input) is expected
