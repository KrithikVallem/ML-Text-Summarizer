# link to article:
# https://dev.to/davidisrawi/build-a-quick-summarizer-with-python-and-nltk

import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


text = """
Four score and seven years ago
our fathers brought forth on
this continent, a new nation,
conceived in Liberty, and
dedicated to the proposition
that all men are created equal.
"""

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

# Originally :12
for sentence in sentences:
    for wordValue in freqTable:
        if wordValue[0] in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += wordValue[1]
            else:
                sentenceValue[sentence] = wordValue[1]

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/ len(sentenceValue))

summary = ''
for sentence in sentences:
        if sentence in sentenceValue and sentenceValue[sentence] > (1.5 * average):
            summary +=  " " + sentence

print(summary)