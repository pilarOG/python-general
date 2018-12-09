# -*- coding: utf-8 -*-

import re
import codecs
import urllib
import unicodedata
from bs4 import BeautifulSoup as soup

# Example to do web scraping to obtain synonyms of words from a synonym webpage (in Spanish)

vocabulario = [u'energía', u'bonita', u'bonito']

for v in vocabulario:

    v = ''.join(c for c in unicodedata.normalize('NFKD', v).encode('ascii', 'ignore'))
    url = 'https://www.sinonimosonline.com/{}/'.format(v)
    content = urllib.urlopen(url)
    charset = content.headers.getheader('Content-Type')
    data = content.read().decode(charset.split('=')[-1])

    fragments = re.findall(r'<div class="sentido">(.*?)<span class="ejemplo">', data)
    print v
    for n in fragments:
        sentido = re.findall(r'(.*?)</div>', n)[0].replace(':', '')
        print sentido
        synonym = re.findall(r'<a href=\"\/(.*?)\/\" class=\"sinonimo\">', n)
        synonym += re.findall(r'<span>(.*?)</span>', n)
        for s in synonym:
            print '\t'+s
