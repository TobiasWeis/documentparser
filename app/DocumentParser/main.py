#!/usr/bin/python3
"""
author: Tobias Weis
"""

from app.DocumentParser.DocumentParser import *

docparse = DocumentParser()
docparse.process("./data/T00018401.pdf")