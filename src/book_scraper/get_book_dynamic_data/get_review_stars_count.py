from src.book_scraper.get_book_dynamic_data.get_star_count import get_star_count


def get_review_stars_count(soup):
    review_stars_count = dict.fromkeys("54321")
    for key in review_stars_count:
        review_stars_count[key] = get_star_count(soup, key)
    return review_stars_count
