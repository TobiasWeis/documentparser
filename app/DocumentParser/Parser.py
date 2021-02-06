#!/usr/bin/python3
"""
author: Tobias Weis
"""

import re
import spacy


class Parser:
    def __init__(self):
        self.nlp_de = spacy.load("de_core_news_lg")

    def process(self, pages):
        for pagenumber, page in enumerate(pages.pages):
            print(page)

            print("-------------------------- Page ", pagenumber)

            personen = self.extract_persons(page.text)
            ibans = self.extract_ibans(page.text)
            ustid = self.extract_ustid(page.text)

            page.personen = personen
            page.ibans = ibans
            page.ustids = ustid

            if len(personen):
                print("Personen:")
                for p in personen:
                    print(p)
                print()

            if len(ibans) > 0:
                print("Kontonummern:")

                for r in ibans:
                    print(r.split("\n")[0])

                print()

            if len(ustid) > 0:
                print("UstIds:")
                for r in ustid:
                    print(r.split("\n")[0])

        return pages

    def extract_persons(self, text):
        spacydoc = self.nlp_de(text)

        personen = []
        for ent in spacydoc.ents:
            if ent.label_ == 'PER':
                personen.append(ent.text)
        return personen

    def extract_ibans(self, text):
        return re.findall('DE[0-9\s]{20}', text)

    def extract_ustid(self, text):
        return re.findall('DE\s*[\d\s*]{9}\S*[\n]', text)