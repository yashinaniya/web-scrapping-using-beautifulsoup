import requests

from bs4 import BeautifulSoup

#page_content = requests.get('https://quotes.toscrape.com/').content
#soup = BeautifulSoup(page.content, 'html.parser')

class QuoteLocators:
    """
        Locators for an item in the HTML page.
        This allows us to easily see what our code will be looking at
        as well as change it quickly if we notice it is now different.
        """
    CONTENT_LOCATOR = 'span.text'
    AUTHOR_LOCATOR = 'small.author'
    TAGS_LOCATOR = 'div.tags a.tag'


class QuotesPageLocators:
    QUOTE = 'div.quote'

class QuoteParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        content_name = self.parent.select_one(locator).string
        return content_name

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        author_name = self.parent.select_one(locator).string
        return author_name

    @property
    def tags(self):
        locator = QuoteLocators.TAGS_LOCATOR
        tags_name = self.parent.select(locator)
        return tags_name


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        quote_tags = self.soup.select(QuotesPageLocators.QUOTE)
        return [QuoteParser(e) for e in quote_tags]

#Now let's request the content of the page and extract Quotes, Author and tags

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)