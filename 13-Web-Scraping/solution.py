#/usr/bin/env python3
# Import any libraries you think you'll need to scrape a website.
import requests
import bs4

# Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
res = requests.get('http://quotes.toscrape.com/')

# print(res.content)

# Get the names of all the authors on the first page.
authors = set()

soup = bs4.BeautifulSoup(res.text, 'lxml')

for name in soup.select('.author'):
    authors.add((name.text).encode('utf-8'))

# print(authors)

# Create a list of all the quotes on the first page.
quotes = []

for quote in soup.select('.text'):
    quotes.append((quote.text).encode('utf-8'))

# print(quotes)

# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text
# shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind
# there are also tags underneath each quote, try to find a class only present in the top right tags,
# perhaps check the span.

top_tags = []

for tag in soup.select('span .tag'):
    top_tags.append(tag.text)

# print(top_tags)

# Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to
# loop through all the pages and get all the unique authors on the website. Keep in mind there are
# many ways to achieve this, also note that you will need to somehow figure out how to check that your
# loop is on the last page with quotes. For debugging purposes, I will let you know that there are
# only 10 pages, so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop
# that is robust enough that it wouldn't matter to know the amount of pages beforehand, perhaps use
# try/except for this, its up to you!

url = 'http://quotes.toscrape.com/page/{}'
authors = set()
page = 1

while True:
    # Get the page content 
    res = requests.get(url.format(page))

    # Check if last page has been reached
    if 'No quotes found!' in res.text:
        break

    # Turn page response into soup object
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add authors to set variable
    for name in soup.select('.author'):
        authors.add(name.text.encode('utf-8'))

    page += 1

# Display all authors scrapped from the page
print(authors)
