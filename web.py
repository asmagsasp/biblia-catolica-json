﻿from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import os   
import urllib.request as urllib2

app = Flask(__name__)

URL = "https://www.bibliacatolica.com.br/"
    
# Retorna todos os livros da bíblia
@app.route('/api/biblia/livros', methods=['GET'])
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

    return jsonify( data )  

# 1.Lista de Capitulos do Livro de Genesis
@app.route('/api/biblia/capitulos/1', methods=['GET'])
def genesis_capitulos():
    data = []
    for x in range(1, 51):

        data.append( { "capítulo" : x } ) 
     
    return jsonify( {"Testamento" : 1, "Livro" : 'Gênesis', "Capítulos" : data } )    

# 1.Livro de Genesis
@app.route('/api/biblia/capitulos/1/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Gênesis', "Capítulo" : capitulo , "Versículos" : data} )

# 2.Lista de Capitulos do Livro de Exodo
@app.route('/api/biblia/capitulos/2', methods=['GET'])
def exodo_capitulos():
    data = []
    for x in range(1, 41):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Êxodo' , "Capítulos" : data } )    

# 2.Livro de Êxodo
@app.route('/api/biblia/capitulos/2/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Êxodo', "Capítulo" : capitulo , "Versículos" : data} )

# 3.Lista de Capitulos do Livro de Levítico
@app.route('/api/biblia/capitulos/3', methods=['GET'])
def levitico_capitulos():
    data = []
    for x in range(1, 28):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Levítico' , "Capítulos" : data } )    

# 3.Livro de Levítico
@app.route('/api/biblia/capitulos/3/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Levítico', "Capítulo" : capitulo , "Versículos" : data} )

# 4.Lista de Capitulos do Livro de Números
@app.route('/api/biblia/capitulos/4', methods=['GET'])
def numeros_capitulos():
    data = []
    for x in range(1, 37):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Números',"Capítulos" : data} )    

# 4.Livro de Números
@app.route('/api/biblia/capitulos/4/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Números', "Capítulo" : capitulo , "Versículos" : data} )

# 5.Lista de Capitulos do Livro de Deuteronômio
@app.route('/api/biblia/capitulos/5', methods=['GET'])
def deuteronomio_capitulos():
    data = []
    for x in range(1, 35):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Deuteronômio' , "Capítulos" : data} )    

# 5.Livro de Deuteronômio
@app.route('/api/biblia/capitulos/5/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Deuteronômio', "Capítulo" : capitulo , "Versículos" : data} )

# 6.Lista de Capitulos do Livro de Josué
@app.route('/api/biblia/capitulos/6', methods=['GET'])
def josue_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Josué', "Capítulos" : data} )    

# 6.Livro de Josué
@app.route('/api/biblia/capitulos/6/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Josué', "Capítulo" : capitulo , "Versículos" : data} )

# 7.Lista de Capitulos do Livro de Juízes
@app.route('/api/biblia/capitulos/7', methods=['GET'])
def juizes_capitulos():
    data = []
    for x in range(1, 22):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Juízes', "Capítulos" : data} )    

# 7.Livro de Juizes
@app.route('/api/biblia/capitulos/7/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Juízes', "Capítulo" : capitulo , "Versículos" : data} )

# 8.Lista de Capitulos do Livro de Rute
@app.route('/api/biblia/capitulos/8', methods=['GET'])
def rute_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Rute', "Capítulos" : data} )    
    
# 8.Livro de Rute
@app.route('/api/biblia/capitulos/8/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Rute', "Capítulo" : capitulo , "Versículos" : data } )

# 9.Lista de Capitulos do Livro de I Samuel
@app.route('/api/biblia/capitulos/9', methods=['GET'])
def isamuel_capitulos():
    data = []
    for x in range(1, 32):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Samuel', "Capítulos" : data} )    

# 9.Livro de I Samuel
@app.route('/api/biblia/capitulos/9/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'I Samuel', "Capítulo" : capitulo , "Versículos" : data} )

# 10.Lista de Capitulos do Livro de II Samuel
@app.route('/api/biblia/capitulos/10', methods=['GET'])
def iisamuel_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Samuel', "Capítulos" : data} )    

# 10.Livro de II Samuel
@app.route('/api/biblia/capitulos/10/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'II Samuel', "Capítulo" : capitulo , "Versículos" : data} )


################## ATÉ AQUI ESTÁ FINALIZADO ####################

# 11.Lista de Capitulos do Livro de I Reis
@app.route('/api/biblia/capitulos/11', methods=['GET'])
def ireis_capitulos():
    data = []
    for x in range(1, 27):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Reis', "Capítulos" : data} )    

# 11.Livro de I Reis
@app.route('/api/biblia/capitulos/11/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'I Reis', "Capítulo" : capitulo , "Versículos" : data} )

# 12.Lista de Capitulos do Livro de II Reis
@app.route('/api/biblia/capitulos/12', methods=['GET'])
def iireis_capitulos():
    data = []
    for x in range(1, 26):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Reis', "Capítulos" : data} )    

# 12.Livro de II Reis
@app.route('/api/biblia/capitulos/12/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'II Reis', "Capítulo" : capitulo , "Versículos" : data} )

# 13.Lista de Capitulos do Livro de I Cronicas
@app.route('/api/biblia/capitulos/13', methods=['GET'])
def icronicas_capitulos():
    data = []
    for x in range(1, 30):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Crônicas', "Capítulos" : data} )    

#13.Livro de I Crônicas
@app.route('/api/biblia/capitulos/13/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'I Crônicas', "Capítulo" : capitulo , "Versículos" : data} )

# 14.Lista de Capitulos do Livro de II Cronicas
@app.route('/api/biblia/capitulos/14', methods=['GET'])
def iicronicas_capitulos():
    data = []
    for x in range(1, 37):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Crônicas', "Capítulos" : data} )    

#Livro de I4 Cronicas
@app.route('/api/biblia/capitulos/14/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'II Crônicas', "Capítulo" : capitulo , "Versículos" : data} )

# 15.Lista de Capitulos do Livro de Esdras
@app.route('/api/biblia/capitulos/15', methods=['GET'])
def esdras_capitulos():
    data = []
    for x in range(1, 11):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Esdras', "Capítulos" : data} )    

#15.Livro de Esdras
@app.route('/api/biblia/capitulos/15/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Esdras', "Capítulo" : capitulo , "Versículos" : data} )

# 16.Lista de Capitulos do Livro de I Neemias
@app.route('/api/biblia/capitulos/16', methods=['GET'])
def neemias_capitulos():
    data = []
    for x in range(1, 14):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Neemias', "Capítulos" : data} )    

# 16.Livro de Neemias
@app.route('/api/biblia/capitulos/16/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Neemias', "Capítulo" : capitulo , "Versículos" : data} )

# 17.Lista de Capitulos do Livro de Tobias
@app.route('/api/biblia/capitulos/17', methods=['GET'])
def tobias_capitulos():
    data = []
    for x in range(1, 15):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Tobias', "Capítulos" : data} )    

# 17.Livro de Tobias
@app.route('/api/biblia/capitulos/17/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Tobias', "Capítulo" : capitulo , "Versículos" : data} )

# 18.Lista de Capitulos do Livro de Judite
@app.route('/api/biblia/capitulos/18', methods=['GET'])
def judite_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Judite', "Capítulos" : data} )    

#18. Livro de Judite
@app.route('/api/biblia/capitulos/18/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Judite', "Capítulo" : capitulo , "Versículos" : data} )

# 19.Lista de Capitulos do Livro de Ester
@app.route('/api/biblia/capitulos/19', methods=['GET'])
def ester_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Ester', "Capítulos" : data} )    

#19. Livro de Ester
@app.route('/api/biblia/capitulos/19/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Ester', "Capítulo" : capitulo , "Versículos" : data} )

# 20.Lista de Capitulos do Livro de Jó
@app.route('/api/biblia/capitulos/20', methods=['GET'])
def jo_capitulos():
    data = []
    for x in range(1, 43):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Jó', "Capítulos" : data} )    

#20. Livro de Jo
@app.route('/api/biblia/capitulos/20/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Jó', "Capítulo" : capitulo ,"Versículos" : data} )

# 21.Lista de Capitulos do Livro de Salmos
@app.route('/api/biblia/capitulos/21', methods=['GET'])
def salmos_capitulos():
    data = []
    for x in range(1, 151):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Salmos', "Capítulos" : data} )    

# 21.Livro de Salmos
@app.route('/api/biblia/capitulos/21/versiculos/<capitulo>', methods=['GET'])
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
        data.append( { "versiculo" : v, "texto" : s }  ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "versiculo" : v, "texto" : s }  ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['versiculo'], reverse=False)
    return jsonify({ "Testamento" : 1, "Livro" : 'Salmos', "Capítulo" : capitulo , "Versículos" : data} )

####################### FINALIZADO ATÉ AQUI ###################    

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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } )  
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
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
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "Capítulo " +format(capitulo) : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1


    data = sorted(data, key=lambda k: k['Capítulo ' +format(capitulo)].get('versiculo', 0), reverse=False) 
    return jsonify({'Habacuc': data}) 

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='0.0.0.0', port=port)    
