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
    for dataBox in soup.find_all("div", class_="row booksList"):
        words = dataBox.text.split(" ")
        for current_word in words:
            prior_word = current_word

            if current_word != "":
               if current_word == "I":
                  data.append( { 'livro' : prior_word + ' ' + current_word } )
                  prior_word = ""        
                  
               elif current_word == "II":
                  data.append( { 'livro' : prior_word + ' ' + current_word } )
                  prior_word = ""        

               else:   
                  data.append( { 'livro' : current_word } )    


            #print(current_word)
        #data.append( { 'livro' : words } ) 
        #for current_word in words:
        #    data.append( { 'livro' : current_word } )    

    return jsonify({'livros': data})  

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='10.1.10.130', port=port)    

    #print(dataBox.text.strip())

    #content = dataBox.find("text", class_="title")
    #print(content.text.strip())

    #print(content.text.strip().split('Gênero')[1][100:])
    