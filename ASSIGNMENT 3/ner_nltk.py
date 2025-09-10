import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


paragraph = (
    "On March 15, 2023, world-famous violinist Anne Summers performed "
    "at the Royal Albert Hall in London. "
    "The event was organized by Global Music Foundation and sponsored by Sony. "
    "Over 5,000 people attended the concert at 7:00 PM. "
    "Tickets were priced at $120 each, making it one of the most expensive events of the year. "
    "BBC News covered the performance and praised it as unforgettable. "
    "Earlier in the 1990s, similar concerts were also held in New York by the Philharmonic Orchestra."
)


for sent in nltk.sent_tokenize(paragraph):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))
