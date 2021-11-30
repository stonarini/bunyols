from src.book_scraper.get_book_dynamic_data.get_total_reviews import get_total_reviews
from src.book_scraper.get_book_dynamic_data.ratings_perc_to_num import (
    ratings_perc_to_num,
)
from src.book_scraper.get_book_dynamic_data.get_review_stars_count import (
    get_review_stars_count,
)


def get_book_ratings(soup):
    ratings = {}
    ratings["total_reviews"] = get_total_reviews(soup)
    if ratings["total_reviews"] != "Na":
        ratings.update(get_review_stars_count(soup))
        ratings = ratings_perc_to_num(ratings)
    return ratings
