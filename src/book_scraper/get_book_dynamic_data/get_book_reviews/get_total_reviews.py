from ..amazon_scraper_config import reviews_tag


def get_total_reviews(soup):
    try:
        total_reviews = (
            soup.find(
                reviews_tag["tag_name"],
                attrs={reviews_tag["tag_type"]: reviews_tag["tag_id"]},
            )
            .string.strip()
            .replace(",", "")
        )
    except TypeError:
        return "Na"
    else:
        return int(total_reviews.split(" ")[0])
