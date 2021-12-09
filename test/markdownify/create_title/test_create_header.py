import pytest
from src.markdownify.create_title.create_header import create_header

@pytest.mark.test_valid_input
def test_create_header():
    book = {
        "title": "Code Complete",
        "author": ["Steve McConnell"],
        "ISBN_13": "9780735619678",
        "categories": ["IT"],
    }
    
    title = book["title"]
    author = book["author"][0]
    # book["author"] = book["author"][0]

    title_header = create_header(title, 2)
    author_header = create_header(author, 3)
    
        
    assert title_header == '## Code Complete'
    assert author_header == '### Steve McConnell'