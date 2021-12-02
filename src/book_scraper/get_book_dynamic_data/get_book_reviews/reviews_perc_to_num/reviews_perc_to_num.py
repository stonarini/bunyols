import math
from .fix_percentage_sum import fix_percentage_sum


def reviews_perc_to_num(reviews):
    total_reviews = reviews["total_reviews"]
    star_reviews = [key for key in reviews if key != "total_reviews"]
    for key in star_reviews:
        reviews[key] = math.floor((total_reviews / 100) * reviews[key])
    reviews = fix_percentage_sum(reviews)
    return reviews
