import pytest
from src.markdownify.create_title import create_title

def test_create_title():
    book = {
        "title": "Code Complete",
        "author": ["Steve McConnell"],
        "ISBN_13": "9780735619678",
        "categories": ["IT"],
    }
    
    title = book["title"]
    author = book["author"][0]
    # book["author"] = book["author"][0]

    formatted_header = create_title(title, author)
    
        
    assert formatted_header == '# Code Complete\n### Steve McConnell\n'
