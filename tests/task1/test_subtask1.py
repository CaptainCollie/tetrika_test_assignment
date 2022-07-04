import pytest

from task1.subtask1 import task


@pytest.mark.parametrize("test_input, expected", (
        ("", -1),
        ("111", -1),
        ("0000", 0),
        ("111000", 3),
        ("1110", 3),
        ("111111111110000000000000000", 11),
        (
            "".join(["1" for _ in range(1000)] + ["0" for _ in range(100)]),
            1000),
        (
            "".join(
                ["1" for _ in range(2 ** 16)] + ["0" for _ in range(2 ** 14)]
            ),
            2 ** 16
        )
)
                         )
def test_subtask1(test_input, expected):
    assert task(test_input) == expected
