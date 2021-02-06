#!/usr/bin/python3
"""
author: Tobias Weis
"""

from collections import OrderedDict
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

from .Pages import *


class Scanner:
    def __init__(self):
        self.pages = Pages()

    def load_and_parse(self, filename):
        if filename.endswith("pdf"):
            print("-- Converting pdf")
            pdfdoc = convert_from_path(filename)
            for page_number, page_data in enumerate(pdfdoc):
                print("-- Extracting text (Page %d)" % page_number)
                image = page_data.convert('LA')
                thistext = pytesseract.image_to_string(image, lang="deu")

                self.pages.add_page(Page(image, thistext))
        else:
            print("-- Loading image")
            image = Image.open(filename).convert('LA')

            print("-- Extracting text")
            self.pages.add_page(Page(image, pytesseract.image_to_string(image, lang="deu")))

        return self.pages
