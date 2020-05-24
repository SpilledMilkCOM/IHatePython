#! python3

import sys
from urllib.request import urlopen


def fetch_words(url):
    """This is a docstring"""

    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()

    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)

# If __name__ == 'words' then it was imported
# If __name__ == '__main__' then it was called as a script

if (__name__ == '__main__'):
    if (len(sys.argv) < 2):
        main('https://parkersmart.com')
    else:
        main(sys.argv[1])
else:
    print('imported words.py.')
