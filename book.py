import re
import collections

# read file, parsing everything into lower case format
text = open("book.txt").read().lower()
# eliminate all whitespace from results
words = re.findall("\w+", text)
# print 10 most commom words
print(collections.Counter(words).most_common(10))