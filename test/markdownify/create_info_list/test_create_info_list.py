import pytest
from src.markdownify.create_info_list.create_info_list import create_info_list

@pytest.mark.test_info_list
def test_info_list():
    book = {"ISBN_13": "9780735619678", "categories": ["IT"], "publisher": "Publisher"}

    info_list = create_info_list(book)

    assert (
        info_list
        == "- **ISBN_13:** 9780735619678\n- **categories:** ['IT']\n- **publisher:** Publisher\n"
    )
