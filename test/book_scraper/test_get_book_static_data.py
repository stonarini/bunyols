import pytest
from src.book_scraper.get_book_static_data.request_openlibary_page import request_openlibrary_page
# #que devuelva un diccionario, devuelva dicc con keys title, author, publisher..., author no sea igual a none


@pytest.mark.test_static_data_is_dict
def test_static_data_dicc(): 
    assert isinstance(request_openlibrary_page("books/OL7353617M"), dict)
    
@pytest.mark.test_static_data_dicc_keys
def test_static_data_dicc_keys():
    assert 