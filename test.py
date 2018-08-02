from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   

app = Flask(__name__)

URL = "https://www.bibliacatolica.com.br/"
    
#html_doc = urlopen(URL).read()

req = Request(URL,headers={'User-Agent': 'Mozilla/5.0'})
html_doc = urlopen(req).read()

soup = BeautifulSoup(html_doc, "html.parser")
data = []

for dataBox in soup.find_all("div", class_="row booksList"):
    words = dataBox.text.strip(" ")
    for current_word in words:
        print(current_word)

    #dataBox.text.strip(" ")

    #for ul in soup.find_all("ul", class_="list-unstyled"):
        #print(dataBox.text.strip())

    #print(content.text.strip().split('Gênero')[1][100:])
    