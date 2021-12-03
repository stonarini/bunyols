from ..amazon_scraper_config import price_tag


def scrap_price(soup):
    try:
        price = (
            soup.find(
                price_tag["tag_name"],
                attrs={price_tag["tag_type"]: price_tag["tag_id"]},
            )
            .string.strip()
            .replace(",", "")
        )
    except:
        price = "Na"
    finally:
        return price
