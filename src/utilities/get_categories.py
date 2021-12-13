def get_categories(family, topics):
    categories = {}
    if family:
        categories["family"] = family
    if topics:
        categories["categories"] = topics
    return categories
