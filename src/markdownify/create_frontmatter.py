def create_frontmatter(book):
    params = ["title", "author", "ISBN_13", "categories", "family"]
    front_keys = {key: value for key, value in book.items() if key in params}

    frontmatter = "---\n"
    for key, value in front_keys.items():
        frontmatter += f"{key}: {value}\n"
    frontmatter += "---\n"
    return frontmatter
