from .create_header import create_header


def create_title(title, author):

    formatted_title = ""

    if len(title) >= 15:
        formatted_title += create_header(title, 2) + "\n"
    else:
        formatted_title += create_header(title, 1) + "\n"

    formatted_title += create_header(author, 3) + "\n"
    return formatted_title
