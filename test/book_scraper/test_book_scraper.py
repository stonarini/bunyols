from src.book_scraper import book_scraper
import pytest

links = [
    (
        "https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/",
        ("Rober C Martin Series", ["IT"]),
    )
    # ("https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052/", None, ["IT"]),
    # ("https://www.amazon.com/1984-Signet-Classics-George-Orwell/dp/0451524934/", None, ["Classic", "Alternative"]),
    # ("https://www.amazon.com/Divina-Commedia-Inferno-Purgatorio-Paradiso/dp/B08P3SLT1S/", None, ["Classic"]),
    # ("https://www.amazon.com/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124/", None, ["IT"]),
    # ("https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/", None, ["IT"]),
    # ("https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/", None, ["IT"], )
]


# @pytest.mark.test_book_scraper
# def test_book_scraper():
#   book_scraper.create_book_data(links)
