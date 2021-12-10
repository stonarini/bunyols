from os import path
import pytest
from src.write_to_file import write_to_file


@pytest.mark.test_write_to_file
def test_write_to_file():
    content = "this\nis\na\ntest\n"
    path = "test/write_to_file/"
    write_to_file(path, "test.txt", content)
    with open(path + "test.txt", "r") as test_file:
        assert test_file.read() == content
