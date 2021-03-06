import re
import logging
from bs4 import BeautifulSoup

from locators.all_books_page_locator import AllBookPageLocator
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')


class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBookPageLocator.BOOKS}`...')
        return [BookParser(e) for e in self.soup.select(AllBookPageLocator.BOOKS)]

    @property
    def page_count(self):
        logger.debug(f'Finding all number of catalogue pages available using `{AllBookPageLocator.PAGE}`...')
        content = self.soup.select_one(AllBookPageLocator.PAGE).string
        
        logger.debug('Try to match page content...')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages =int(matcher.group(1))
        logger.info(f'Extracted number of pages as integer: `{pages}`.')
        return pages