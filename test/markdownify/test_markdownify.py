import pytest
from src.markdownify import markdownify


@pytest.mark.test_markdownify
def test_markdownify():
    book = {
        "title": "Clean Code",
        "author": ["Robert C. Martin"],
        "publisher": "Prentice Hall",
        "ISBN_13": "9780132350884",
        "publish_date": "July 2008",
        "family": "Robert C Martin Series",
        "categories": ["IT"],
    }

    markdown_text = markdownify(book)
    assert (
        markdown_text
        == "---\ntitle: Clean Code\nauthor: Robert C. Martin\nISBN_13: 9780132350884\nfamily: Robert C Martin Series\ncategories: ['IT']\n---\n# Clean Code\n### Robert C. Martin\n- **publisher:** Prentice Hall\n- **ISBN_13:** 9780132350884\n- **publish_date:** July 2008\n- **family:** Robert C Martin Series\n- **categories:** ['IT']\n"
    )
