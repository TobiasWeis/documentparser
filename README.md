# Document Parser
Recognizes text from scanned documents from different filetypes (pdf, jpg, png) 
and parse their contents. Afterwards extract desired information (names, account-numbers, etc.).

## Usage
* ```flask run```
* navigate your browser to localhost:5000

## Setup
For Linux:
* Install necessary system packages ```sudo apt-get install tesseract-ocr tesseract-ocr-deu```
* Install python requirements ```python3 -m pip install -r requirements.txt```
* Download spacy language model: ```python3 -m spacy download de_core_news_lg```
