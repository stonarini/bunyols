from .get_total_reviews import get_total_reviews
from .reviews_perc_to_num import reviews_perc_to_num
from .get_review_stars_count import get_review_stars_count


def get_book_reviews(soup):
    reviews = {}
    reviews["total_reviews"] = get_total_reviews(soup)
    if reviews["total_reviews"] != "Na":
        reviews.update(get_review_stars_count(soup))
        reviews = reviews_perc_to_num(reviews)
    return reviews
