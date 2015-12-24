from urllib2 import urlopen
from bs4 import BeautifulSoup
from collections import Counter

def downloadLink(lien):
    # dowanload html
    html = urlopen(lien).read()
    return html


def parseHTML(lien):

    # download html
    html = downloadLink(lien)

    # create soup with html parser
    soup = BeautifulSoup(html,"html.parser")

    # get all text in the body
    body_text = soup.body.findAll(text=True)

    # loop through all element with text
    words = []
    for text in body_text:
        # concatenate the words
        words.append(text)

    wordlist = ''.join(words).split()
    counts = wordCounter(wordlist)
    results = []
    for letter, count in counts:
        results.append('%s: %7d' % (letter, count))

    return ', <br>'.join(results)


def wordCounter(words):
    counts = Counter(words).most_common(20)
    return counts
