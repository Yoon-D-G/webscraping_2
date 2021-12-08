
import practice2
import requests
from bs4 import BeautifulSoup
import webscraping3

def get_html_content(url):
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup


# This for loop displays the data for every book in the list on practice2.py (Uncomment with care; it's big!)

# for book in practice2.full_url_booklist:
#     book_html = get_html_content(book[1])
#     book_class = webscraping3.Book_Info(book_html, book[2])
#     book_class.category
#     book_class.Title()
#     book_class.Description()
#     book_class.UPC()
#     book_class.Product_type()
#     book_class.Price_excl__tax__()
#     book_class.Price_incl__tax__()
#     book_class.Tax()
#     book_class.Availability()
#     book_class.Number_of_reviews()


# Below prints out the data for one book along with which category it's in.

full_book_page_html = get_html_content(practice2.full_url_booklist[0][1])

book = webscraping3.Book_Info(full_book_page_html, practice2.full_url_booklist[0][2])

print('Category={}'.format(book.category))
print(book.Title())
print(book.Description())
print(book.UPC())
print(book.Product_type())
print(book.Price_excl__tax__())
print(book.Price_incl__tax__())
print(book.Tax())
print(book.Availability())
print(book.Number_of_reviews())