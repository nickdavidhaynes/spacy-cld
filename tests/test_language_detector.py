import spacy
from spacy_cld import LanguageDetector

nlp = spacy.load('en')
language_detector = LanguageDetector()
nlp.add_pipe(language_detector)


def test_english_doc():
    doc = nlp('This is some English text.')
    assert 'en' in doc._.languages
    assert doc._.language_scores['en'] > 0.9


def test_chinese_doc():
    doc = nlp('أفاد مصدر امني في قيادة عمليات صلاح الدين في العراق بأن القوات الامنية تتوقف لليومالثالث على التوالي عن التقدم الى داخل مدينة تكريت بسببانتشار قناصي التنظيم الذي يطلق على نفسه اسم الدولة الاسلامية والعبوات الناسفةوالمنازل المفخخة والانتحاريين، فضلا عن ان القوات الامنية تنتظر وصول تعزيزات اضافية')
    assert 'ar' in doc._.languages
    assert doc._.language_scores['ar'] > 0.9


def test_bilingual_doc():
    doc = nlp("China (simplified Chinese: 中国; traditional Chinese: 中國), officially the People's Republic of China (PRC), is a sovereign state located in East Asia.")
    assert 'en' in doc._.languages
    assert 'zh-Hant' in doc._.languages


def test_english_span():
    doc = nlp('This is a sentence of English text.')
    assert 'en' in doc[1:-1]._.languages


def test_unknown_not_in_languages():
    doc = nlp('This is a sentence of English text.')
    assert 'un' not in doc._.languages


def test_unknown_not_in_language_scores():
    doc = nlp('This is a sentence of English text.')
    assert 'un' not in doc._.language_scores.keys()
