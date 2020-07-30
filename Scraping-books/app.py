import requests
import logging
import time

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt',
                    filemode='w')

logger = logging.getLogger('scraping')

print('Loading books list...')
logger.info('Loading books list...')

book_website = 'http://books.toscrape.com'  # main website link
logger.info(f'Requesting `{book_website}`')
page_content = requests.get(book_website).content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

books_ = []

start_time = time.time()  # initialize time to measure task-time.
logger.info(f'Going through all `{page.page_count}` pages of books...')
for page_num in range(page.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    logger.info(f'Requesting `{url}`')
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    print(f'`{url}` took `{time.time() - page_start}` seconds.')  # Time taken by each url.
    books_.extend(page.books)
print(f'Total time took to extract `{time.time() - start_time}` seconds.')
