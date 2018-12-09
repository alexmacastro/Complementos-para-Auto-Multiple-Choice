# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:10:55 2018

@author: alex
"""

#from BeautifulSoup import BeautifulStoneSoup
import html


def unicodeToHTMLEntities(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    text = html.escape(text).encode('ascii', 'xmlcharrefreplace')
    return text

texto = 'Estimado alumno de Mecánica para ingenieros: Exámen. Acento á'

textoh = unicodeToHTMLEntities(texto)

print (textoh)