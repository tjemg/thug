#!/usr/bin/env python
from __future__ import with_statement

from CSSStyleDeclaration import CSSStyleDeclaration

class ElementCSSInlineStyle(object):
    def __init__(self, doc, tag):
        self.tag = tag

    @property
    def style(self):
        return CSSStyleDeclaration(self.tag['style'] if self.tag.has_key('style') else '')
