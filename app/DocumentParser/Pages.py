#!/usr/bin/python3
"""
author: Tobias Weis
"""
import base64
from io import BytesIO


class Pages:
    def __init__(self):
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def get_serializable_json(self):
        output = []
        for page in self.pages:
            output.append(page.get_serializable_infos())

        return output


class Page:
    def __init__(self, image, text):
        self.image = image
        self.text = text

        self.personen = []
        self.ibans = []
        self.ustids = []

    def get_serializable_infos(self):
        output = {}
        buffered = BytesIO()
        self.image.convert('RGB').save(buffered, format="JPEG")
        output["image"] = base64.b64encode(buffered.getvalue()).decode('utf-8')
        output["text"] = self.text
        output["personen"] = self.personen
        output["ibans"] = self.ibans
        output["ustids"] = self.ustids

        return output

