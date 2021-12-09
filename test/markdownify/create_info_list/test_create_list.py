import pytest
from src.markdownify.create_info_list.create_list import create_list

def test_create_list():
    key = "ISBN_13"
    value = "9780735619678"
    

    info_list = create_list(key, value)
    

    assert info_list == "- **ISBN_13:** 9780735619678"



