# spaCy-CLD: Bringing simple language detection to spaCy

This package is a 
[spaCy 2.0 extension](https://spacy.io/usage/processing-pipelines#section-extensions)
that adds language detection to spaCy's text processing pipeline.
Inspired from a discussion [here](https://github.com/explosion/spaCy/issues/1172).

## Installation

`python setup.py install`

If you can't compile it, retry after
 
`export CFLAGS="-Wno-narrowing"`

## Usage

Adding the spaCy-CLD component to the processing pipeline is relatively simple:

```
import spacy
from spacy_cld import LanguageDetector

nlp = spacy.load('en')
language_detector = LanguageDetector()
nlp.add_pipe(language_detector)
doc = nlp('This is some English text.')

doc._.languages  # ['en']
doc._.language_scores['en']  # 0.96
```

spaCy-CLD operates on `Doc` and `Span` spaCy objects. When called on a `Doc` or `Span`,
the object is given two attributes: `languages` (a list of up to 3 language codes) 
and `language_scores` (a dictionary mapping language codes to confidence scores between 
0 and 1).

## Under the hood

spacy-cld is a little extension that wraps the 
[CLD2-CFFI](https://github.com/GregBowyer/cld2-cffi) Python library, which in turn 
wraps the [Compact Language Detector 2](https://github.com/CLD2Owners/cld2) 
C++ library originally built at Google for the Chromium project.
CLD2 uses character n-grams as features and a Naive Bayes classifier to identify 
80+ languages from Unicode text strings (or XML/HTML). 
It can detect up to 3 different languages in a given document, and reports 
a confidence score (reported in with each language.

For additional details, see the linked project pages for CLD2-CFFI and CLD2.
