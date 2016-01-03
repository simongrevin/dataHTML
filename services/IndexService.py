from urllib2 import urlopen
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

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

def tokenize(lien):

    # download html
    html = downloadLink(lien)

    # create soup with html parser
    soup = BeautifulSoup(html,"html.parser")

    # get all text in the body
    body_text = soup.body.findAll(text=True)

    # loop through all element with text
    texts = []
    for text in body_text:
        # concatenate the words
        text = text.lower()
        exclude = set(string.punctuation)
        text = ''.join(ch for ch in text if ch not in exclude)
        texts.append(text)

    #example_sent = "This is a sample sentence, showing off sample of the stop words filtration."
    stop_words = set(stopwords.words('english'))
    word_tokens = []
    for text in texts:
        word_tokens.append(word_tokenize(text))

    filtered_sentence = []
    for word_token in word_tokens:
        for w in word_token:
            if w not in stop_words:
                filtered_sentence.append(w)
    #print(filtered_sentence)

    counts = wordCounter(filtered_sentence)
    results = []
    for letter, count in counts:
        results.append('%s: %7d' % (letter, count))

    return ', <br>'.join(results)

def wordCounter(words):
    counts = Counter(words).most_common(20)
    print counts
    return counts
