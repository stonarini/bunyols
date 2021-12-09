from .create_list import create_list

def create_info_list(dict_values):
    info_list = ""
    for key,value in dict_values.items():
        info_list += create_list(key, value) + "\n"
        
    return info_list