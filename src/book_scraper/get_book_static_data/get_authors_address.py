def get_authors_address(address):

    author_page_dict = []
    for work in address["authors"]:
        author_page_dict.append(work["author"])

    author_page_address = []
    for value in author_page_dict:
        author_page_address.append(list(value.values()))

    authors_list = []
    for sublist in author_page_address:
        for item in sublist:
            authors_list.append(item)

    return authors_list
