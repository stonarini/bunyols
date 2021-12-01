def get_authors_address(authors):

    author_page = []
    for author in authors:
        author_page.append(author["author"]["key"])

    return author_page
