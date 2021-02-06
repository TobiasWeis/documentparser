#!/usr/bin/python3
"""
author: Tobias Weis
"""

from app.DocumentParser.Scanner import *
from app.DocumentParser.Parser import *


class DocumentParser:
    def __init__(self):
        self.scanner = Scanner()
        self.parser = Parser()

    def process(self, filename):
        pages = self.scanner.load_and_parse(filename)
        pages = self.parser.process(pages)

        return pages
