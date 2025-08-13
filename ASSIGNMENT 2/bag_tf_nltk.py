import nltk
import re

nltk.download('punkt')

paragraph = paragraph = ("The government announced a new economic policy. "
             "Global markets reacted positively to the news. "
             "Experts predict economic growth in the coming year. "
             "We first tokenize the text into words and create a Dictionary that assigns each word a unique ID.")


sentences = nltk.sent_tokenize(paragraph)

corpus = []


for sent in sentences:
    sent = re.sub('[^a-zA-Z]', ' ', sent)  
    sent = sent.lower()  
    corpus.append(sent)

print("Processed Corpus:", corpus)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
bow_features = cv.fit_transform(corpus).toarray()
print("\nBag of Words Representation:\n", bow_features)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf_features = tfidf.fit_transform(corpus).toarray()
print("\nTF-IDF Representation:\n", tfidf_features)
