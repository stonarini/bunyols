import pytest
from src.markdownify.create_frontmatter import create_frontmatter


@pytest.mark.test_valid_input
def test_valid_input():
    book = {
        "title": "Code Complete",
        "author": ["Steve McConnell"],
        "ISBN_13": "9780735619678",
        "categories": ["IT"],
    }

    create_frontmatter(book)

    book_test = {}
    with open("test/markdownify/create_frontmatter/test.md", "r") as test_file:
        for line in test_file:
            if line != "---":
                colon = line.find(":")
                book_test[line[:colon]] = line[colon+2:]
                
    assert book == book_test


