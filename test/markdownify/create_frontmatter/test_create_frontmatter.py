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

    book["author"] = book["author"][0]

    frontmatter = create_frontmatter(book)

    assert (
        frontmatter
        == "---\ntitle: Code Complete\nauthor: Steve McConnell\nISBN_13: 9780735619678\ncategories: ['IT']\n---\n"
    )
