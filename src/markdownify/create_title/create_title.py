from .create_header import create_header


def create_title(title, author):

    formatted_title = "<div> \n\n"

    if len(title) >= 15:
        formatted_title += create_header(title, 2)
    else:
        formatted_title += create_header(title, 1)

    formatted_title += "<br /> \n\n" + create_header(author, 3) + "\n\n </div> \n\n"
    return formatted_title
