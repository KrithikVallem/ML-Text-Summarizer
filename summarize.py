# link to article:
# https://dev.to/davidisrawi/build-a-quick-summarizer-with-python-and-nltk
# https://towardsdatascience.com/understand-text-summarization-and-create-your-own-summarizer-in-python-b26a9f09fc70

text = """
When you are shopping for vintage jewelry, one way to ensure that you are not buying fake vintage, is to ask the seller about the history of a particular item. If the piece is actually vintage the seller should be able to explain how they came across the item. For instance, it may have been passed down through the family, purchased at an estate sale or auction, or found while antique hunting., Most vintage jewelry was marked by the jewelry maker, either with initials or small emblems. Use a magnifying glass to examine the jewelry for marks before purchasing. If you notice any discrepancies between marks then the piece is likely a fake or replica.Search online for pictures of well-known vintage jewelers' marks.<n>There may be instances when some older items of jewelry were not marked. For example, early pieces of Chanel jewelry were unmarked and different markings were used during different periods.If you can’t locate any markings, then ask the seller about the history of the piece.<n> It is also important to carefully examine the condition of an item of jewelry before purchasing it. Although most vintage jewelry will have some minor signs of wear and tear, you want to make sure they are minimal. For instance, check for broken clasps, missing gems or jewels, as well as major scratches. All of these blemishes will decrease the value of the piece. Try and find gently used pieces that only have minor signs of wear.Most importantly check for good craftsmanship, which includes straight lines, and the symmetrical placement of stones.<n>Be wary of any jewelry marketed as vintage but that appears in mint condition.<n>In these instances ask the seller if the piece has been recently restored. This can decrease the value of the jewelry.<n> When buying vintage jewelry ask the retailer to provide you with documentation concerning the origin of the piece. This documentation can add value to the item, making it more authentic. This will also help to ensure that you are buying legitimate vintage jewelry, instead of mass produced new jewelry designed to look like vintage jewelry. Different types of documentation and authentication include:Certificate of authentication from a professional.<n>Original receipts from when the jewelry was purchased that include the purchasers name.<n>A photograph showing the piece being worn.<n>Handwritten notes from previous owners.<n>Other documents showing the items history.<n> You should always consider the price when you are shopping for vintage jewelry. Items that contain real diamonds and are made of gold will be pricey. If an item is being sold as a designer piece of gold jewelry, but is priced reasonably, it is likely fake. That being said, you do not have to break the bank to buy vintage jewelry. You can find very unique and beautiful pieces of vintage and antique costume jewelry that is reasonable priced.<n>Take into consideration the type of piece you want and make sure that you truly love the piece before purchasing it.
"""


import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
import numpy as np
import networkx as nx


# Steps
# 1: tokenize text
# 2: generate similarity matrix across sentences
# 3: rank sentences in similarity matrix
# 4: sort the ranks and pick top sentences
# 5: join top sentences and output summary

stemmer = PorterStemmer()

def tokenize_text(text):
  text = text.strip().lower()
  sentences = sent_tokenize(text, "english")
  swords = stopwords.words('english')
  all_tokens = [
      [stemmer.stem(w) for w in word_tokenize(sent) if w not in swords] 
    for sent in sentences]
  return all_tokens

# s1 and s2 are two sentences
def get_sentence_similarity(s1, s2):
  # nan's are because we don't return anything here
  all_words = list(set(s1+s2))
  s1_vector = [0]*len(all_words)
  s2_vector = [0]*len(all_words)
  for w in s1:
    s1_vector[all_words.index(w)] += 1 
  for w in s2:
    s2_vector[all_words.index(w)] += 1 
  return 1 - cosine_distance(s1_vector, s2_vector)
  

def generate_similarity_matrix(tokenized_text):
  # make starting state for matrix
  num_sentences = len(tokenized_text)
  similarity_matrix = np.zeros( (num_sentences, num_sentences) )

  for i,sentence_1 in enumerate(tokenized_text):
    for j,sentence_2 in enumerate(tokenized_text):
      # skip if we are trying to compare identical sentences
      if i == j:
        continue

      similarity_matrix[i][j] = get_sentence_similarity(sentence_1, sentence_2)

  return similarity_matrix


if __name__ == "__main__":
  tokenized_text = tokenize_text(text)
  #print(tokenized_text)
  similarity_matrix = generate_similarity_matrix(tokenized_text)
  print(similarity_matrix)








