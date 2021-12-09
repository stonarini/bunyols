def create_frontmatter(book):
    frontmatter = "---\n"
    for key, value in book.items():
        frontmatter += f"{key}: {value}\n"
    frontmatter += "---"
    return frontmatter
