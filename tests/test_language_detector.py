import spacy
from spacy_cld import LanguageDetector


def test_language_detector():
    nlp = spacy.load('en')
    language_detector = LanguageDetector()
    nlp.add_pipe(language_detector)
    doc = nlp('This is some English text.')
    assert len(doc._.languages) > 0
