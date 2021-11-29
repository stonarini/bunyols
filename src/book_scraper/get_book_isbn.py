from get_book_source import get_page_content 
from bs4 import BeautifulSoup

def get_book_isbn(website):

    start = str(website.content).find('ISBN')
    start = str(website.content).find('9', start)
    ISBN = str(website.content)[start:start+14]
    
    return ISBN.replace('-', '')