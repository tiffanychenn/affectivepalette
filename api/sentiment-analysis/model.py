from lib2to3.pgen2 import token
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.text import TextCollection
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import stopwords
import os

wnl = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 

def clean_text(text):
    '''
    Preprocess text.

    1: Tokenize words
    2: 
    '''
    tokens = nltk.sent_tokenize(text.lower())
    tokens = [w for t in tokens for w in nltk.word_tokenize(t) if w.isalpha() and not w in stop_words]
    tokens = [wnl.lemmatize(t) for t in tokens]
    pos_tags = nltk.pos_tag(tokens)
    pos_tags = [(t[0], penn_to_wn(t[1])) for t in pos_tags if penn_to_wn(t[1])]

    # compute things
    collection = TextCollection(tokens)
    token_set = set(pos_tags)
    new_text = "".join([t + " " for t in tokens])
    pos = 0
    neg = 0
    for t in token_set:
        synsets = wn.synsets(t[0], pos=t[1]) # grab the most common one
        if not synsets:
            continue
        synset = synsets[0]
        swn_synset = swn.senti_synset(synset.name())
        pos += swn_synset.pos_score() * collection.tf_idf(t[0], new_text) 
        neg += swn_synset.neg_score() * collection.tf_idf(t[0], new_text) 

    return (pos, neg)


def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None



def test_model_func():
    pos_count = 0
    neg_count = 0
    for t in ["business", "entertainment", "politics", "sport", "tech"]:
        path = "../../data/bbc/" + t
        for filename in os.listdir(path):
            with open(path + "/" + filename) as f:
                lines = f.readlines()
                text = "".join(lines)
                pos, neg = clean_text(text)
                if pos > neg:
                    pos_count += 1
                else:
                    neg_count += 1
    return pos_count, neg_count

print(test_model_func())
