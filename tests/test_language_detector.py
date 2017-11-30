import spacy
from spacy_cld import LanguageDetector

nlp = spacy.load('en')
language_detector = LanguageDetector()
nlp.add_pipe(language_detector)


def test_english_text():
    doc = nlp('This is some English text.')
    assert 'en' in doc._.languages.keys()
    assert doc._.languages['en']['name'] == 'ENGLISH'
    assert doc._.languages['en']['confidence'] > 0.9


def test_chinese_text():
    doc = nlp('أفاد مصدر امني في قيادة عمليات صلاح الدين في العراق بأن القوات الامنية تتوقف لليومالثالث على التوالي عن التقدم الى داخل مدينة تكريت بسببانتشار قناصي التنظيم الذي يطلق على نفسه اسم الدولة الاسلامية والعبوات الناسفةوالمنازل المفخخة والانتحاريين، فضلا عن ان القوات الامنية تنتظر وصول تعزيزات اضافية')
    assert 'ar' in doc._.languages.keys()
    assert doc._.languages['ar']['name'] == 'ARABIC'
    assert doc._.languages['ar']['confidence'] > 0.9


def test_bilingual_text():
    doc = nlp("China (simplified Chinese: 中国; traditional Chinese: 中國), officially the People's Republic of China (PRC), is a sovereign state located in East Asia.")
    assert 'en' in doc._.languages.keys()
    assert 'zh-Hant' in doc._.languages.keys()
