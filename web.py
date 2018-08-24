from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import os   
import urllib.request as urllib2

app = Flask(__name__)

URL = "https://www.bibliacatolica.com.br/"
    
# Retorna todos os livros da bíblia
@app.route('/api/biblia', methods=['GET'])
def livros():

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

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
                       data.append( { "id" : i, "nome" : current_frase  } )
                       prior_word = ""

               else:   
                  i = i + 1
                  data.append( { "id" : i,  "nome" : current_word } )    

    return jsonify({'livros': data})  

# Livro de Genesis
@app.route('/api/biblia/1/<capitulo>', methods=['GET'])
def genesis(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/genesis/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 1" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 1" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['Livro 1'].get('versiculo', 0), reverse=False)
     
    return jsonify({'genesis': data})  

# Lista de Capitulos do Livro de Genesis
@app.route('/api/biblia/1/capitulos', methods=['GET'])
def genesis_capitulos():
    data = []
    for x in range(1, 51):

        data.append( { "id" : x } ) 
     
    return jsonify({'genesis': data})    

# Livro de Êxodo
@app.route('/api/biblia/2/<capitulo>', methods=['GET'])
def exodo(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/exodo/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 2" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 2" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1
    
    data = sorted(data, key=lambda k: k['Livro 2'].get('versiculo', 0), reverse=False)
    return jsonify({'êxodo': data})     

# Lista de Capitulos do Livro de Exodo
@app.route('/api/biblia/2/capitulos', methods=['GET'])
def exodo_capitulos():
    data = []
    for x in range(1, 41):

        data.append( { "id" : x } ) 
     
    return jsonify({'êxodo': data})      

# Livro de Levítico
@app.route('/api/biblia/3/<capitulo>', methods=['GET'])
def levitico(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/levitico/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 3" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 3" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Caitulo 3'].get('versiculo', 0), reverse=False) 
    return jsonify({'levítico': data}) 

# Lista de Capitulos do Livro de Levítico
@app.route('/api/biblia/3/capitulos', methods=['GET'])
def levitico_capitulos():
    data = []
    for x in range(1, 28):

        data.append( { "id" : x } ) 
     
    return jsonify({'levítico': data})   

# Livro de Números
@app.route('/api/biblia/4/<capitulo>', methods=['GET'])
def numeros(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/numeros/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 4" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 4" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 4'].get('versiculo', 0), reverse=False) 
    return jsonify({'números': data}) 

# Lista de Capitulos do Livro de Números
@app.route('/api/biblia/4/capitulos', methods=['GET'])
def numeros_capitulos():
    data = []
    for x in range(1, 37):

        data.append( { "id" : x } ) 
     
    return jsonify({'números': data})   

#Livro de Deuteronômio
@app.route('/api/biblia/5/<capitulo>', methods=['GET'])
def deuteronomio(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/deuteronomio/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 5" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 5" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 5'].get('versiculo', 0), reverse=False) 
    return jsonify({'deuteronômio': data})  

# Lista de Capitulos do Livro de Deuteronômio
@app.route('/api/biblia/5/capitulos', methods=['GET'])
def deuteronomio_capitulos():
    data = []
    for x in range(1, 35):

        data.append( { "id" : x } ) 
     
    return jsonify({'deuteronômio': data})       

#Livro de Josué
@app.route('/api/biblia/6/<capitulo>', methods=['GET'])
def josue(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/josue/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 6" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 6" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 6'].get('versiculo', 0), reverse=False) 
    return jsonify({'josue': data})  

# Lista de Capitulos do Livro de Josué
@app.route('/api/biblia/6/capitulos', methods=['GET'])
def josue_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "id" : x } ) 
     
    return jsonify({'josué': data})       

#Livro de Juizes
@app.route('/api/biblia/7/<capitulo>', methods=['GET'])
def juizes(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/juizes/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 7" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 7" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 7'].get('versiculo', 0), reverse=False) 
    return jsonify({'juizes': data})  

# Lista de Capitulos do Livro de Juízes
@app.route('/api/biblia/7/capitulos', methods=['GET'])
def juizes_capitulos():
    data = []
    for x in range(1, 22):

        data.append( { "id" : x } ) 
     
    return jsonify({'juízes': data})   

#Livro de Rute
@app.route('/api/biblia/8/<capitulo>', methods=['GET'])
def rute(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/rute/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 8" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 8" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 8'].get('versiculo', 0), reverse=False) 
    return jsonify({'rute': data})  

# Lista de Capitulos do Livro de Rute
@app.route('/api/biblia/8/capitulos', methods=['GET'])
def rute_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "id" : x } ) 
     
    return jsonify({'rute': data})       

#Livro de I Samuel
@app.route('/api/biblia/9/<capitulo>', methods=['GET'])
def isamuel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/isamuel/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 9" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 9" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 9'].get('versiculo', 0), reverse=False) 
    return jsonify({'I Samuel': data})  

# Lista de Capitulos do Livro de I Samuel
@app.route('/api/biblia/9/capitulos', methods=['GET'])
def isamuel_capitulos():
    data = []
    for x in range(1, 27):

        data.append( { "id" : x } ) 
     
    return jsonify({'i samuel': data})       

#Livro de II Samuel
@app.route('/api/biblia/10/<capitulo>', methods=['GET'])
def iisamuel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/iisamuel/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 10" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Livro 10" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Livro 10'].get('versiculo', 0), reverse=False) 
    return jsonify({'II Samuel': data}) 

# Lista de Capitulos do Livro de II Samuel
@app.route('/api/biblia/10/capitulos', methods=['GET'])
def iisamuel_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "id" : x } ) 
     
    return jsonify({'ii samuel': data})  

################## ATÉ AQUI ESTÁ FINALIZADO ####################

#Livro de I Reis
@app.route('/api/biblia/ireis/<capitulo>', methods=['GET'])
def ireis(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ireis/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'I Reis': data})     

#Livro de II Reis
@app.route('/api/biblia/iireis/<capitulo>', methods=['GET'])
def iireis(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/iireis/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'II Reis': data})  

#Livro de I Crônicas
@app.route('/api/biblia/icronicas/<capitulo>', methods=['GET'])
def icronicas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/icronicas/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'I Crônicas': data}) 

#Livro de II Cronicas
@app.route('/api/biblia/iicronicas/<capitulo>', methods=['GET'])
def iicronicas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/iicronicas/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'II Crônicas': data}) 

#Livro de Esdras
@app.route('/api/biblia/esdras/<capitulo>', methods=['GET'])
def esdras(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/esdras/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Esdras': data}) 

#Livro de Neemias
@app.route('/api/biblia/neemias/<capitulo>', methods=['GET'])
def neemias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/neemias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Neemias': data})

#Livro de Tobias
@app.route('/api/biblia/tobias/<capitulo>', methods=['GET'])
def tobias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/tobias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Tobias': data})   

#Livro de Judite
@app.route('/api/biblia/judite/<capitulo>', methods=['GET'])
def judite(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/judite/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Judite': data})

#Livro de Ester
@app.route('/api/biblia/ester/<capitulo>', methods=['GET'])
def ester(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ester/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Ester': data})    

#Livro de Jo
@app.route('/api/biblia/jo/<capitulo>', methods=['GET'])
def jo(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/jo/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Jó': data}) 

#Livro de Salmos
@app.route('/api/biblia/salmos/<capitulo>', methods=['GET'])
def salmos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/salmos/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Salmos': data})

#Livro de I Macabeus
@app.route('/api/biblia/imacabeus/<capitulo>', methods=['GET'])
def imacabeus(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/imacabeus/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'I Macabeus': data})    

#Livro de II Macabeus
@app.route('/api/biblia/iimacabeus/<capitulo>', methods=['GET'])
def iimacabeus(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/iimacabeus/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'II Macabeus': data})  

#Livro de Proverbios
@app.route('/api/biblia/proverbios/<capitulo>', methods=['GET'])
def proverbios(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/proverbios/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Provérbios': data}) 

#Livro de Eclesiastes
@app.route('/api/biblia/eclesiastes/<capitulo>', methods=['GET'])
def eclesiastes(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/eclesiastes/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Eclesiastes': data})     

#Livro de Cântico dos Cânticos
@app.route('/api/biblia/canticodoscanticos/<capitulo>', methods=['GET'])
def canticodoscanticos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/canticodoscanticos/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Cântico dos Cânticos': data}) 

#Livro de Sabedoria
@app.route('/api/biblia/sabedoria/<capitulo>', methods=['GET'])
def sabedoria(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sabedoria/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Sabedoria': data})   

#Livro de Eclesiástico
@app.route('/api/biblia/eclesiastico/<capitulo>', methods=['GET'])
def eclesiastico(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/eclesiastico/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Eclesiástico': data}) 

#Livro de Isaías
@app.route('/api/biblia/isaias/<capitulo>', methods=['GET'])
def isaias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/isaias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Isaías': data}) 

#Livro de Jeremias
@app.route('/api/biblia/jeremias/<capitulo>', methods=['GET'])
def jererimas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/jeremias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Jeremias': data}) 

#Livro de Lamentacoes
@app.route('/api/biblia/lamentacoes/<capitulo>', methods=['GET'])
def lamentacoes(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/lamentacoes/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Lamentações': data})  

#Livro de Baruc
@app.route('/api/biblia/baruc/<capitulo>', methods=['GET'])
def baruc(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/baruc/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Baruc': data}) 

#Livro de Ezequiel
@app.route('/api/biblia/ezequiel/<capitulo>', methods=['GET'])
def ezequiel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ezequiel/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Ezequiel': data})     

#Livro de Daniel
@app.route('/api/biblia/daniel/<capitulo>', methods=['GET'])
def daniel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/daniel/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Daniel': data})     

#Livro de Oseias
@app.route('/api/biblia/oseias/<capitulo>', methods=['GET'])
def oseias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/oseias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Oséias': data})  

#Livro de Joel
@app.route('/api/biblia/joel/<capitulo>', methods=['GET'])
def joel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/joel/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Joel': data}) 

#Livro de Amós
@app.route('/api/biblia/amos/<capitulo>', methods=['GET'])
def amos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/amos/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Amós': data})   

#Livro de Abdias
@app.route('/api/biblia/abdias/<capitulo>', methods=['GET'])
def abdias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/abdias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Abdias': data}) 

#Livro de Jonas
@app.route('/api/biblia/jonas/<capitulo>', methods=['GET'])
def jonas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/jonas/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Jonas': data}) 

#Livro de Miqueias
@app.route('/api/biblia/miqueias/<capitulo>', methods=['GET'])
def miqueias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/miqueias/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Miquéias': data}) 

#Livro de Naum
@app.route('/api/biblia/naum/<capitulo>', methods=['GET'])
def naum(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/naum/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Naum': data})    

#Livro de Habacuc
@app.route('/api/biblia/habacuc/<capitulo>', methods=['GET'])
def habacuc(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/habacuc/{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):

        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False) 
    return jsonify({'Habacuc': data}) 

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='0.0.0.0', port=port)    
