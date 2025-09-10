import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

concert_text = (
    "On March 15, 2023, world-famous violinist Anne Summers performed "
    "at the Royal Albert Hall in London. "
    "The event was organized by Global Music Foundation and sponsored by Sony. "
    "Over 5,000 people attended the concert at 7:00 PM. "
    "Tickets were priced at $120 each, making it one of the most expensive events of the year. "
    "BBC News covered the performance and praised it as unforgettable."
)

concert_doc = nlp(concert_text)

for ent in concert_doc.ents:
    print(
        f"""
{ent.text = }
{ent.start_char = }
{ent.end_char = }
{ent.label_ = }
spacy.explain('{ent.label_}') = {spacy.explain(ent.label_)}"""
    )


displacy.serve(concert_doc, style="ent")
