from pathlib import Path

import pytest

from task2.main import task


@pytest.mark.skip
def test_task():
    expected = Path('tests/task2/fixtures/expected.txt').read_text()
    result = task()
    assert result == expected
