# -*- coding: utf-8 -*-
import nltk
from wordcloud import WordCloud



text = """I went to Japan. (NOT I went to the Japan.)
He played tennis with Ben. (NOT He played tennis with the Ben.)
They had breakfast at 9 o’clock. (NOT They had a breakfast at 9 o'clock.)
(Some words don't have an article. We don't usually use articles for countries, meals or people.)"""


cloud = WordCloud().generate(text)
cloud.to_file('output.png')
