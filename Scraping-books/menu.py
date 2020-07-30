import logging

from app import books_


logger = logging.getLogger('scraping.menu')


USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''

books_generator = (x for x in books_)


def print_best_books():
    logger.debug('Finding best books by rating...')
    best_books = sorted(books_, key=lambda x: x.rating * -1)[:5]  # top 5 books
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.debug('Finding best books by price...')
    cheapest_books = sorted(books_, key=lambda x: x.price)[:5]  # top 5 books
    for book in cheapest_books:
        print(book)


def get_next_book():
    logger.debug('Getting next book from generator of all books...')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        logger.debug('User did not choose to exit program.')
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('please choose a valid command.')
        user_input = input(USER_CHOICE)
    else:
        logger.debug('Terminating program...')
        print('Thank You')
        exit(0)


print(f'Total Books: {len(books_)}\n')
menu()