import requests

from pages.quotes_page import QuotePage

page_content = requests.get('http://quotes.toscrape.com/').content
page = QuotePage(page_content)

for quote in page.quotes:
    print(f'Quote: {quote.content}')
    print(f'Author: {quote.author}')
    print(f'Tags: {quote.tags}\n\n')
