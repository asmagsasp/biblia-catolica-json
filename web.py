from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   

app = Flask(__name__)

URL = "https://www.bibliacatolica.com.br/"
    
@app.route('/api/biblia', methods=['GET'])
def livros():

    req = Request(URL,headers={'User-Agent': 'Mozilla/5.0'})
    html_doc = urlopen(req).read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    prior_word = ""
    i = 0

    for dataBox in soup.find_all("div", class_="row booksList"):

        s = dataBox.text
        
        s = s.replace("I São","I#São")       
        s = s.replace("II São","II#São")
        s = s.replace("III São","III#São")

        words = s.split(" ")

        for current_word in words:
            
            if current_word != "":

               if current_word == "I" or current_word == "I#São" or current_word == "II" or current_word == "II#São" or  current_word == "III" or current_word == "III#São" or current_word == "São" or current_word == "Cântico" or current_word == "Atos":
                  current_word = current_word.replace("#", " ")
                  prior_word = current_word

               elif prior_word != "":
                    current_frase = prior_word + ' ' + current_word
                    if current_frase == "Atos dos" or current_frase == "Cântico dos":
                       prior_word = current_frase
                    else:       
                       i = i + 1
                       data.append( { i : current_frase  } )
                       prior_word = ""

               else:   
                  i = i + 1
                  data.append( { i : current_word } )    

    return jsonify({'livros': data})  

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='127.0.0.1', port=port)    
