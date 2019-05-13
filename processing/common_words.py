# helper script to get the words

import collections
import os
import sys
import string
import re
from pathlib import Path

def find_word_counts(folder):
    word_counts = {}
    for filename in os.listdir(folder):
        with open("%s/%s/play.txt"%(folder,filename), "r") as filecontents:
            to_replace = "[\\n\\t\\r\\s]+"
            text = filecontents.read()
            text = re.sub(to_replace, " ", text)
            words = text.split(" ")
            for word in words:
                # strip punctuation
                table = str.maketrans({key: None for key in string.punctuation})
                word = word.translate(table) 
                word = word.lower()
                if word in word_counts:
                    word_counts[word] = word_counts[word] + 1
                else:
                    word_counts[word] = 1
    return word_counts

if __name__ == "__main__":
    folder = sys.argv[1]
    if not Path(folder).is_dir():
        print("%s cannot be found" % folder)
    word_counter = collections.OrderedDict(sorted(find_word_counts(folder).items(), key=lambda t: t[1]))
    i = 0
    limit = 75
    for key in reversed(word_counter.keys()):
        print("%d occurrences of %s" % (word_counter.get(key), key))
        if i > limit:
            break
        i += 1
