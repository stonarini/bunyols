from .create_frontmatter import create_frontmatter
from .create_title import create_title
from .create_info_list import create_info_list


def markdownify(book):
    book["author"] = book["author"][0]

    markdown_string = (
        create_frontmatter(book)
        + create_title(book["title"], book["author"])
        + create_info_list(book)
    )

    return markdown_string
