import functools


def accumulate(doc, sentence):
    if doc:
        return doc + '. ' + sentence
    else:
        return sentence

def accumulate_first_sentences(sentences, n):
    doc = functools.reduce(accumulate, sentences[:n], '')
    if not doc.endswith('.'):
        doc += '.'
    return doc
