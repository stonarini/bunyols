import pytest
from pathlib import Path
import shutil
import os
from src.database import find_all
from src.get_and_write import get_and_write


def test_get_and_write():
    directory = "test/get_and_write/md/"
    os.makedirs(directory)

    books = find_all()
    ISBNs = [book["ISBN_13"] for book in books]
    get_and_write(directory)
    test_dir = Path(directory)
    test_dir_files = [(test_file.name)[:-3] for test_file in test_dir.glob("*.md")]
    try:
        assert sorted(ISBNs) == sorted(test_dir_files)
    finally:
        shutil.rmtree(directory)
