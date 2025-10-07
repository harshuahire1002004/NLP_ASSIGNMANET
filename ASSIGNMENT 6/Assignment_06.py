###  Assignment No 6 ###

"""Assignment Title : : Implement and visualize Dependency Parsing of Textual Input
using Stan- ford CoreNLP and Spacy library"""


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Jupiter is the largest planet in our solar system, known for its giant red storm and many moons. Its strong magnetic field and thick atmosphere of hydrogen and helium make it a fascinating target for space exploration."""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")


'''
**************   OUTPUT     ****************


TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'Jupiter'
token.dep_ = 'dep'

TOKEN: Jupiter
=====
token.tag_ = 'NNP'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'is'
token.dep_ = 'ROOT'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'planet'
token.dep_ = 'det'

TOKEN: largest
=====
token.tag_ = 'JJS'
token.head.text = 'planet'
token.dep_ = 'amod'

TOKEN: planet
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'attr'

TOKEN: in
=====
token.tag_ = 'IN'
token.head.text = 'planet'
token.dep_ = 'prep'

TOKEN: our
=====
token.tag_ = 'PRP$'
token.head.text = 'system'
token.dep_ = 'poss'

TOKEN: solar
=====
token.tag_ = 'JJ'
token.head.text = 'system'
token.dep_ = 'amod'

TOKEN: system
=====
token.tag_ = 'NN'
token.head.text = 'in'
token.dep_ = 'pobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'system'
token.dep_ = 'punct'

TOKEN: known
=====
token.tag_ = 'VBN'
token.head.text = 'system'
token.dep_ = 'acl'

TOKEN: for
=====
token.tag_ = 'IN'
token.head.text = 'known'
token.dep_ = 'prep'

TOKEN: its
=====
token.tag_ = 'PRP$'
token.head.text = 'storm'
token.dep_ = 'poss'

TOKEN: giant
=====
token.tag_ = 'JJ'
token.head.text = 'storm'
token.dep_ = 'amod'

TOKEN: red
=====
token.tag_ = 'JJ'
token.head.text = 'storm'
token.dep_ = 'amod'

TOKEN: storm
=====
token.tag_ = 'NN'
token.head.text = 'for'
token.dep_ = 'pobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'storm'
token.dep_ = 'cc'

TOKEN: many
=====
token.tag_ = 'JJ'
token.head.text = 'moons'
token.dep_ = 'amod'

TOKEN: moons
=====
token.tag_ = 'NNS'
token.head.text = 'storm'
token.dep_ = 'conj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'is'
token.dep_ = 'punct'

TOKEN: Its
=====
token.tag_ = 'PRP$'
token.head.text = 'field'
token.dep_ = 'poss'

TOKEN: strong
=====
token.tag_ = 'JJ'
token.head.text = 'field'
token.dep_ = 'amod'

TOKEN: magnetic
=====
token.tag_ = 'JJ'
token.head.text = 'field'
token.dep_ = 'amod'

TOKEN: field
=====
token.tag_ = 'NN'
token.head.text = 'make'
token.dep_ = 'nsubj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'field'
token.dep_ = 'cc'

TOKEN: thick
=====
token.tag_ = 'JJ'
token.head.text = 'atmosphere'
token.dep_ = 'amod'

TOKEN: atmosphere
=====
token.tag_ = 'NN'
token.head.text = 'field'
token.dep_ = 'conj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'atmosphere'
token.dep_ = 'prep'

TOKEN: hydrogen
=====
token.tag_ = 'NN'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'hydrogen'
token.dep_ = 'cc'

TOKEN: helium
=====
token.tag_ = 'NN'
token.head.text = 'hydrogen'
token.dep_ = 'conj'

TOKEN: make
=====
token.tag_ = 'VBP'
token.head.text = 'make'
token.dep_ = 'ROOT'

TOKEN: it
=====
token.tag_ = 'PRP'
token.head.text = 'target'
token.dep_ = 'nsubj'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'target'
token.dep_ = 'det'

TOKEN: fascinating
=====
token.tag_ = 'JJ'
token.head.text = 'target'
token.dep_ = 'amod'

TOKEN: target
=====
token.tag_ = 'NN'
token.head.text = 'make'
token.dep_ = 'ccomp'

TOKEN: for
=====
token.tag_ = 'IN'
token.head.text = 'target'
token.dep_ = 'prep'

TOKEN: space
=====
token.tag_ = 'NN'
token.head.text = 'exploration'
token.dep_ = 'compound'

TOKEN: exploration
=====
token.tag_ = 'NN'
token.head.text = 'for'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'make'
token.dep_ = 'punct'
'''