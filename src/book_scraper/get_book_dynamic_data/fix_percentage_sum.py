def fix_percentage_sum(ratings):
    star_ratings = {
        key: value for key, value in ratings.items() if key != "total_reviews"
    }
    total_dif = ratings["total_reviews"] - sum(star_ratings.values())
    for key, value in reversed(sorted(star_ratings.items(), key=lambda x: x[1])):
        if total_dif == 0:
            break
        ratings[key] = value + 1
        total_dif -= 1
    return ratings
