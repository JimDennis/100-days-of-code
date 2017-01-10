#!/usr/bin/env python
'''Fetch the Wikipedia full List of Latin Phrases, and save as a JSON List
   This extracts all the tables from weach section (letter) generates a
   list of dictionaries, each of the form:

        {"Translation": "the voice of the people is the voice of God",
         "Notes": "Said of an argument either for a conclusion that ... ",
          "Quotation": "ab absurdo"},

   ... suitable for use with a "famouse quoations and phrases" application.

'''

import requests, json
from StringIO import StringIO

from lxml import etree

url='https://en.wikipedia.org/wiki/List_of_Latin_phrases_(full)'


def get_raw_data(url):
    parser = etree.HTMLParser()
    contents = requests.get(url)
    tree = etree.parse(StringIO(contents.text), parser)
    rows = tree.xpath('/html/body/div/div/div/table/tr')
    return rows

def extract_quotes(rows):
    quotes = list()
    for i, r in enumerate(rows):
        data = r.xpath('td')
        if len(data) == 0:
            continue # Table Heather <th> lines
        latin = data[0].xpath('b//text()')
        if not latin:
            latin = data[0].xpath('b/a//text()')
        if not latin:
            latin = r.xpath('*//text()')[0]
        trans = data[1].xpath('.//text()')
        if not trans:
            trans = data[1].xpath('*//text()')
        if len(data) > 2:
            notes = data[2].xpath('text()')
            if not notes:
                notes = data[2].xpath('*//text()')
        quotes.append((latin, trans, notes))
    return quotes

def save_json(quotes, filename='./quotes.json.new'):
    output = list()
    for q, t, n in quotes:
        output.append({'Quotation': ''.join(q), 'Translation': ''.join(t), 'Notes': ''.join(n)})

    with open(filename, 'w') as f:
        json.dump(output, f)


if __name__ == '__main__':
    quotes = extract_quotes(get_raw_data(url))
    save_json(quotes)
    print "%d quotes written" % len(quotes)
 
