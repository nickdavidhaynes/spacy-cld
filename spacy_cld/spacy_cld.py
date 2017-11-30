from pycld2 import detect
from spacy.tokens import Doc, Span


def get_languages(text, cld_results=None):
    if cld_results is None:
        cld_results = detect_languages(text)
    return [lang for (_, lang, _, _) in cld_results if lang != 'Unknown']


def get_scores(text, cld_results=None):
    if cld_results is None:
        cld_results = detect_languages(text)
    return {lang: score / 100 for (_, lang, score, _) in cld_results}


def detect_languages(text):
    _, _, results = detect(text.text)
    return results


class LanguageDetector(object):

    name = 'cld'

    def __init__(self, attrs=('languages', 'language_scores')):
        self._languages, self._scores = attrs
        Doc.set_extension(self._languages, getter=get_languages)
        Doc.set_extension(self._scores, getter=get_scores)
        Span.set_extension(self._languages, getter=get_languages)
        Span.set_extension(self._scores, getter=get_scores)

    def __call__(self, doc):
        '''Apply the language detector as a pipeline component.'''
        # Make a single call to the language detector and cache the result.
        cld_results = detect_languages(doc)
        doc._.set(self._languages, get_languages(doc, cld_results))
        doc._.set(self._scores, get_scores(doc, cld_results))
        return doc
