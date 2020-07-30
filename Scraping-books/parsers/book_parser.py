import re
import logging

from locators.book_info_locators import BookInfoLocators


logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page (or part of it), and find properties of an
    item (in this case Book) in it.
    """

    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,parent):
        logger.debug(f'New book parser created from `{parent}`')  # gives a HTML
        self.parent = parent

    def __repr__(self):
        return f'<Book Name: {self.name}, Price: £{self.price}, {self.rating} Stars>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookInfoLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.info(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book page link...')
        locator = BookInfoLocators.LINK_LOCATOR
        item_url = self.parent.select_one(locator).attrs['href']
        logger.info(f'Found book page link, `{item_url}`.')
        return item_url

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookInfoLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        logger.debug(f'Item price element found, `{item_price}`.')

        pattern = '£([0-9]+\.[0-9]+)'   # set pattern £51.77
        logger.debug(' Try to matching price pattern...')
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))  # book price
        logger.info(f'Found book price, `{price}`')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookInfoLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']    # ['star-rating', 'Three']
        # rating = [e for e in classes if e != 'star-rating'] (if not use filter)
        rating_classes = filter(lambda x: x != 'star-rating', classes)  # returns a iterable object
        rating_class = next(rating_classes)

        logger.debug(f'Found rating class, `{rating_class}`.')
        logger.debug('Converting to integer for sorting...')
        rating_number = BookParser.RATING.get(rating_class)    # get 1st data if not found return None
        logger.info(f'Found book rating, `{rating_number}`.')
        return rating_number
