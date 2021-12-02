def get_book_isbn(website):
    website_content = str(website)
    start = website_content.find("ISBN")
    start = website_content.find("9", start)
    ISBN = website_content[start : start + 14]

    return ISBN.replace("-", "")
