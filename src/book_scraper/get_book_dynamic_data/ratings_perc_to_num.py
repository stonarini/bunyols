from src.book_scraper.get_book_dynamic_data.fix_percentage_sum import fix_percentage_sum
import math


def ratings_perc_to_num(ratings):
    total_reviews = ratings["total_reviews"]
    star_reviews = [key for key in ratings if key != "total_reviews"]
    for key in star_reviews:
        ratings[key] = math.floor((total_reviews / 100) * ratings[key])
    ratings = fix_percentage_sum(ratings)
    return ratings
