from __future__ import unicode_literals
from pycld2 import detect
from spacy.tokens import Doc, Span


class LanguageDetector(object):

    name = 'cld'

    def __init__(self, attrs=('languages')):
        _detect_languages = attrs
        Doc.set_extension(_detect_languages, getter=self.detect_languages)
        Span.set_extension(_detect_languages, getter=self.detect_languages)

    def __call__(self, doc):
        '''Apply the language detector as a pipeline component.'''
        doc._.languages = self.detect_languages(doc)
        return doc

    def detect_languages(self, text):
        '''Thin wrapper around CLD's language detector.'''
        return detect(text.text)
