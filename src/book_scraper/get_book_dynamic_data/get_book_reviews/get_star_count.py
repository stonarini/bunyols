from ..amazon_scraper_config import star_tag


def get_star_count(soup, key):
    try:
        star_count = soup.find(
            star_tag["tag_name"],
            attrs={star_tag["tag_type"]: star_tag["tag_id"] + f" {key}star"},
        )["title"][18:20].rstrip("% ")
    except TypeError:
        star_count = 0
    finally:
        return int(star_count)
