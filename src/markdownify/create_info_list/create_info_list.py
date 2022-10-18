from .create_list import create_list


def create_info_list(book):
    title_list = ["title", "author"]
    info_list_dict = {
        key: value for key, value in book.items() if key not in title_list
    }

    info_list = "<div> \n\n"
    for key, value in info_list_dict.items():
        info_list += create_list(key, value) + "\n\n"
    info_list +=  "<br /> \n\n"
    return info_list
