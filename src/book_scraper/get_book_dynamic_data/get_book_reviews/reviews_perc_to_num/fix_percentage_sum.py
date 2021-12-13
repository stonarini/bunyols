def fix_percentage_sum(reviews):
    star_reviews = {
        key: value for key, value in reviews.items() if key != "total_reviews"
    }
    total_dif = reviews["total_reviews"] - sum(star_reviews.values())
    for key, value in reversed(sorted(star_reviews.items(), key=lambda x: x[1])):
        if total_dif == 0:
            break
        reviews[key] = value + 1
        total_dif -= 1
    return reviews
