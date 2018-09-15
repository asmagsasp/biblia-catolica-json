from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import os   
import urllib.request as urllib2

app = Flask(__name__)

URL = "https://www.bibliacatolica.com.br/"

#####################################################################################
#                                    INÍCIO                                         #
# ###################################################################################    

    
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
    testamento = 1
    seta_testamento = 0

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

#####################################################################################
#                          PRIMEIRO TESTAMENTO                                      #
# ###################################################################################    

# 1.Lista de Capitulos do Livro de Genesis
@app.route('/api/biblia/capitulos/1', methods=['GET'])
def genesis_capitulos():
    data = []
    for x in range(1, 51):

        data.append( { "capítulo" : x } ) 
     
    return jsonify( {"Testamento" : 1, "Livro" : 'Gênesis', "Capítulos" : data } )    

###################################################################################    

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

###################################################################################

# 2.Lista de Capitulos do Livro de Exodo
@app.route('/api/biblia/capitulos/2', methods=['GET'])
def exodo_capitulos():
    data = []
    for x in range(1, 41):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Êxodo' , "Capítulos" : data } )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Êxodo', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 3.Lista de Capitulos do Livro de Levítico
@app.route('/api/biblia/capitulos/3', methods=['GET'])
def levitico_capitulos():
    data = []
    for x in range(1, 28):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Levítico' , "Capítulos" : data } )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Levítico', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 4.Lista de Capitulos do Livro de Números
@app.route('/api/biblia/capitulos/4', methods=['GET'])
def numeros_capitulos():
    data = []
    for x in range(1, 37):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Números',"Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Números', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 5.Lista de Capitulos do Livro de Deuteronômio
@app.route('/api/biblia/capitulos/5', methods=['GET'])
def deuteronomio_capitulos():
    data = []
    for x in range(1, 35):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Deuteronômio' , "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Deuteronômio', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 6.Lista de Capitulos do Livro de Josué
@app.route('/api/biblia/capitulos/6', methods=['GET'])
def josue_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Josué', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Josué', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 7.Lista de Capitulos do Livro de Juízes
@app.route('/api/biblia/capitulos/7', methods=['GET'])
def juizes_capitulos():
    data = []
    for x in range(1, 22):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Juízes', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Juízes', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 8.Lista de Capitulos do Livro de Rute
@app.route('/api/biblia/capitulos/8', methods=['GET'])
def rute_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Rute', "Capítulos" : data} )    
    
###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Rute', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 9.Lista de Capitulos do Livro de I Samuel
@app.route('/api/biblia/capitulos/9', methods=['GET'])
def isamuel_capitulos():
    data = []
    for x in range(1, 32):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Samuel', "Capítulos" : data} )    

###################################################################################

# 9.Livro de I Samuel
@app.route('/api/biblia/capitulos/9/versiculos/<capitulo>', methods=['GET'])
def isamuel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-samuel/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'I Samuel', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 10.Lista de Capitulos do Livro de II Samuel
@app.route('/api/biblia/capitulos/10', methods=['GET'])
def iisamuel_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Samuel', "Capítulos" : data} )    

###################################################################################

# 10.Livro de II Samuel
@app.route('/api/biblia/capitulos/10/versiculos/<capitulo>', methods=['GET'])
def iisamuel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-samuel/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'II Samuel', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 11.Lista de Capitulos do Livro de I Reis
@app.route('/api/biblia/capitulos/11', methods=['GET'])
def ireis_capitulos():
    data = []
    for x in range(1, 23):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Reis', "Capítulos" : data} )    

###################################################################################

# 11.Livro de I Reis
@app.route('/api/biblia/capitulos/11/versiculos/<capitulo>', methods=['GET'])
def ireis(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-reis/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'I Reis', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 12.Lista de Capitulos do Livro de II Reis
@app.route('/api/biblia/capitulos/12', methods=['GET'])
def iireis_capitulos():
    data = []
    for x in range(1, 26):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Reis', "Capítulos" : data} )    

###################################################################################

# 12.Livro de II Reis
@app.route('/api/biblia/capitulos/12/versiculos/<capitulo>', methods=['GET'])
def iireis(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-reis/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'II Reis', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 13.Lista de Capitulos do Livro de I Cronicas
@app.route('/api/biblia/capitulos/13', methods=['GET'])
def icronicas_capitulos():
    data = []
    for x in range(1, 30):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Crônicas', "Capítulos" : data} )    

###################################################################################

#13.Livro de I Crônicas
@app.route('/api/biblia/capitulos/13/versiculos/<capitulo>', methods=['GET'])
def icronicas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-cronicas/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'I Crônicas', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 14.Lista de Capitulos do Livro de II Cronicas
@app.route('/api/biblia/capitulos/14', methods=['GET'])
def iicronicas_capitulos():
    data = []
    for x in range(1, 37):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Crônicas', "Capítulos" : data} )    

###################################################################################

#Livro de I4 Cronicas
@app.route('/api/biblia/capitulos/14/versiculos/<capitulo>', methods=['GET'])
def iicronicas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-cronicas/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'II Crônicas', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 15.Lista de Capitulos do Livro de Esdras
@app.route('/api/biblia/capitulos/15', methods=['GET'])
def esdras_capitulos():
    data = []
    for x in range(1, 11):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Esdras', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Esdras', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 16.Lista de Capitulos do Livro de I Neemias
@app.route('/api/biblia/capitulos/16', methods=['GET'])
def neemias_capitulos():
    data = []
    for x in range(1, 14):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Neemias', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Neemias', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 17.Lista de Capitulos do Livro de Tobias
@app.route('/api/biblia/capitulos/17', methods=['GET'])
def tobias_capitulos():
    data = []
    for x in range(1, 15):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Tobias', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Tobias', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 18.Lista de Capitulos do Livro de Judite
@app.route('/api/biblia/capitulos/18', methods=['GET'])
def judite_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Judite', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Judite', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 19.Lista de Capitulos do Livro de Ester
@app.route('/api/biblia/capitulos/19', methods=['GET'])
def ester_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Ester', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Ester', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 20.Lista de Capitulos do Livro de Jó
@app.route('/api/biblia/capitulos/20', methods=['GET'])
def jo_capitulos():
    data = []
    for x in range(1, 43):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Jó', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Jó', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 21.Lista de Capitulos do Livro de Salmos
@app.route('/api/biblia/capitulos/21', methods=['GET'])
def salmos_capitulos():
    data = []
    for x in range(1, 151):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Salmos', "Capítulos" : data} )    

###################################################################################

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Salmos', "Capítulo" : capitulo , "Versículos" : [] } )  

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

###################################################################################

# 22.Lista de Capitulos do I Macabeus
@app.route('/api/biblia/capitulos/22', methods=['GET'])
def i_macabeus_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'I Macabeus', "Capítulos" : data} )    

###################################################################################

# 22.Livro de I Macabeus
@app.route('/api/biblia/capitulos/22/versiculos/<capitulo>', methods=['GET'])
def i_macabeus(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-macabeus/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'I Macabeus', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'I Macabeus', "Capítulo" : capitulo , "Versículos" : data} )

###################################################################################

# 23.Lista de Capitulos do II Macabeus
@app.route('/api/biblia/capitulos/23', methods=['GET'])
def ii_macabeus_capitulos():
    data = []
    for x in range(1, 16):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'II Macabeus', "Capítulos" : data} )    

###################################################################################

# 23.Livro de II Macabeus
@app.route('/api/biblia/capitulos/23/versiculos/<capitulo>', methods=['GET'])
def ii_macabeus(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-macabeus/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'II Macabeus', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'II Macabeus', "Capítulo" : capitulo , "Versículos" : data} )

###################################################################################

# 24.Lista de Capitulos do Provérbios
@app.route('/api/biblia/capitulos/24', methods=['GET'])
def proverbios_capitulos():
    data = []
    for x in range(1, 32):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Provérbios', "Capítulos" : data} )    

###################################################################################

# 24.Livro de Provérbios
@app.route('/api/biblia/capitulos/24/versiculos/<capitulo>', methods=['GET'])
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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Provérbios', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Proverbios', "Capítulo" : capitulo , "Versículos" : data} )

###################################################################################

# 25.Lista de Capitulos do Eclesiastes
@app.route('/api/biblia/capitulos/25', methods=['GET'])
def eclesiastes_capitulos():
    data = []
    for x in range(1, 13):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Eclesiastes', "Capítulos" : data} )    

###################################################################################

# 25.Livro de Eclesiastes
@app.route('/api/biblia/capitulos/25/versiculos/<capitulo>', methods=['GET'])
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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Eclesiastes', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Eclesiastes', "Capítulo" : capitulo , "Versículos" : data} )    

###################################################################################

# 26.Lista de Capitulos do Cântico cos canticos
@app.route('/api/biblia/capitulos/26', methods=['GET'])
def cantico_dos_canticos_capitulos():
    data = []
    for x in range(1, 9):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Cântico dos Cânticos', "Capítulos" : data} ) 

###################################################################################

#26. Livro de Cântico dos Cânticos
@app.route('/api/biblia/capitulos/26/versiculos/<capitulo>', methods=['GET']) 
def cantico_dos_canticos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/cantico-dos-canticos/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Cântico dos Cânticos', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Cântico dos Cânticos', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 27.Lista de Capitulos da Sabedoria
@app.route('/api/biblia/capitulos/27', methods=['GET'])
def sabedoria_capitulos():
    data = []
    for x in range(1, 20):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Sabedoria', "Capítulos" : data} ) 

###################################################################################

#27. Livro de Cântico da Sabedoria
@app.route('/api/biblia/capitulos/27/versiculos/<capitulo>', methods=['GET'])
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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Sabedoria', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Sabedoria', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################

# 28.Lista de Capitulos do Eclsiástico
@app.route('/api/biblia/capitulos/28', methods=['GET'])
def eclesiastico_capitulos():
    data = []
    for x in range(1, 52):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Eclesiástico', "Capítulos" : data} ) 

###################################################################################

#28. Livro do Eclesiástico
@app.route('/api/biblia/capitulos/28/versiculos/<capitulo>', methods=['GET'])
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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Eclesiástico', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Eclesiástico', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 29.Lista de Capitulos de Isaías
@app.route('/api/biblia/capitulos/29', methods=['GET'])
def isaias_capitulos():
    data = []
    for x in range(1, 67):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Isaías', "Capítulos" : data} ) 

###################################################################################

#29. Livro de Isaías
@app.route('/api/biblia/capitulos/29/versiculos/<capitulo>', methods=['GET'])
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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Isaías', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Isaías', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 30.Lista de Capitulos de Jeremias
@app.route('/api/biblia/capitulos/30', methods=['GET'])
def jeremias_capitulos():
    data = []
    for x in range(1, 53):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Jeremias', "Capítulos" : data} ) 

###################################################################################

#30. Livro de Cântico de Jeremias
@app.route('/api/biblia/capitulos/30/versiculos/<capitulo>', methods=['GET'])
def jeremias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/jeremias{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Jeremias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Jeremias', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 31.Lista de Capitulos de Lamentações
@app.route('/api/biblia/capitulos/31', methods=['GET'])
def lamentacoes_capitulos():
    data = []
    for x in range(1, 6):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Lamentações', "Capítulos" : data} ) 

###################################################################################

#31. Livro de Cântico de Lamentações
@app.route('/api/biblia/capitulos/31/versiculos/<capitulo>', methods=['GET'])
def lamentacoes(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/lamentacoes{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Lamentações', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Lamentações', "Capítulo" : capitulo , "Versículos" : data} )  
 
###################################################################################

# 31.Lista de Capitulos de Baruc
@app.route('/api/biblia/capitulos/32', methods=['GET'])
def baruc_capitulos():
    data = []
    for x in range(1, 7):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Baruc', "Capítulos" : data} ) 

###################################################################################

# 31. Livro de Cântico de Baruc
@app.route('/api/biblia/capitulos/32/versiculos/<capitulo>', methods=['GET'])
def baruc(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/baruc{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Baruc', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Baruc', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 33.Lista de Capitulos de Ezequiel
@app.route('/api/biblia/capitulos/33', methods=['GET'])
def exequiel_capitulos():
    data = []
    for x in range(1, 49):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Ezequiel', "Capítulos" : data} ) 

###################################################################################

# 33. Livro de Cântico de Ezequiel
@app.route('/api/biblia/capitulos/33/versiculos/<capitulo>', methods=['GET'])
def exequiel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ezequiel{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Ezequiel', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Ezequiel', "Capítulo" : capitulo , "Versículos" : data} )  
    
###################################################################################

# 34.Lista de Capitulos de Daniel
@app.route('/api/biblia/capitulos/34', methods=['GET'])
def daniel_capitulos():
    data = []
    for x in range(1, 15):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Daniel', "Capítulos" : data} ) 

###################################################################################

# 34. Livro de Cântico de Daniel
@app.route('/api/biblia/capitulos/34/versiculos/<capitulo>', methods=['GET'])
def daniel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/daniel{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):
        
        s = dataBox.text

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Daniel', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Daniel', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 35.Lista de Capitulos de Oseias
@app.route('/api/biblia/capitulos/35', methods=['GET'])
def oseias_capitulos():
    data = []
    for x in range(1, 15):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Oseias', "Capítulos" : data} ) 

###################################################################################

# 34. Livro de Cântico de Daniel
@app.route('/api/biblia/capitulos/35/versiculos/<capitulo>', methods=['GET'])
def oseias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/oseias{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):
        
        s = dataBox.text

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Oséias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Oséias', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################

# 36.Lista de Capitulos de Joel
@app.route('/api/biblia/capitulos/36', methods=['GET'])
def joel_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Joel', "Capítulos" : data} ) 

###################################################################################

# 36. Livro de Cântico de Joel
@app.route('/api/biblia/capitulos/34/versiculos/<capitulo>', methods=['GET'])
def joel(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/joel{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):
        
        s = dataBox.text

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Joel', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Joel', "Capítulo" : capitulo , "Versículos" : data} )  

# 37.Lista de Capitulos de Amós
@app.route('/api/biblia/capitulos/37', methods=['GET'])
def amos_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Amós', "Capítulos" : data} ) 

###################################################################################

# 37. Livro de Cântico de Amós
@app.route('/api/biblia/capitulos/37/versiculos/<capitulo>', methods=['GET'])
def amos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/amos{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):
        
        s = dataBox.text

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Amós', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Amós', "Capítulo" : capitulo , "Versículos" : data} )  

# 38.Lista de Capitulos de Abdias
@app.route('/api/biblia/capitulos/38', methods=['GET'])
def abdias_capitulos():
    data = []
    for x in range(1, 2):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Abdias', "Capítulos" : data} ) 

###################################################################################

# 36. Livro de Cântico de Abdias
@app.route('/api/biblia/capitulos/34/versiculos/<capitulo>', methods=['GET'])
def abdias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/abdias{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):
        
        s = dataBox.text
        verso = s[:3]

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Abdias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Abdias', "Capítulo" : capitulo , "Versículos" : data} )  

# 39.Lista de Capitulos de Jonas
@app.route('/api/biblia/capitulos/39', methods=['GET'])
def jonas_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Jonas', "Capítulos" : data} ) 

###################################################################################

# 39. Livro de Cântico de Jonas
@app.route('/api/biblia/capitulos/39/versiculos/<capitulo>', methods=['GET'])
def jonas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/jonas{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Jonas', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Jonas', "Capítulo" : capitulo , "Versículos" : data} )  

# 40.Lista de Capitulos de Miqueias
@app.route('/api/biblia/capitulos/40', methods=['GET'])
def miqueias_capitulos():
    data = []
    for x in range(1, 8):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Miquéias', "Capítulos" : data} ) 

###################################################################################

# 40. Livro de Cântico de Miqueias
@app.route('/api/biblia/capitulos/40/versiculos/<capitulo>', methods=['GET'])
def miqueias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/miqueias{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Miquéias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Miquéias', "Capítulo" : capitulo , "Versículos" : data} )   

# 41.Lista de Capitulos de Naum
@app.route('/api/biblia/capitulos/41', methods=['GET'])
def naum_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Miquéias', "Capítulos" : data} ) 

###################################################################################

# 41. Livro de Cântico de Naum
@app.route('/api/biblia/capitulos/41/versiculos/<capitulo>', methods=['GET'])
def naum(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/naum{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Naum', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Naum', "Capítulo" : capitulo , "Versículos" : data} )

###################################################################################

# 42.Lista de Capitulos de Habacuc
@app.route('/api/biblia/capitulos/42', methods=['GET'])
def habacuc_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Habacuc', "Capítulos" : data} ) 

###################################################################################

# 42. Livro de Cântico de Habacuc
@app.route('/api/biblia/capitulos/42/versiculos/<capitulo>', methods=['GET'])
def habacuc(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/habacuc{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Habacuc', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Habacuc', "Capítulo" : capitulo , "Versículos" : data} )

###################################################################################    

# 43.Lista de Capitulos de Sofonias
@app.route('/api/biblia/capitulos/43', methods=['GET'])
def sofonias_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Sofonias', "Capítulos" : data} ) 

###################################################################################

# 43. Livro de Cântico de Sofonias
@app.route('/api/biblia/capitulos/43/versiculos/<capitulo>', methods=['GET'])
def sofonias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sofonias{}".format(capitulo)

    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("p", class_="odd"):
        
        s = dataBox.text

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Sofonias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Sofonias', "Capítulo" : capitulo , "Versículos" : data} )    

###################################################################################    

# 44.Lista de Capitulos de Ageu
@app.route('/api/biblia/capitulos/44', methods=['GET'])
def ageu_capitulos():
    data = []
    for x in range(1, 3):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Ageu', "Capítulos" : data} ) 

###################################################################################

# 44. Livro de Cântico de Ageu
@app.route('/api/biblia/capitulos/44/versiculos/<capitulo>', methods=['GET'])
def ageu(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ageu{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Ageu', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Ageu', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################    

# 45.Lista de Capitulos de Zacarias
@app.route('/api/biblia/capitulos/45', methods=['GET'])
def zacarias_capitulos():
    data = []
    for x in range(1, 15):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Zacarias', "Capítulos" : data} ) 

###################################################################################

# 45. Livro de Cântico de Zacarias
@app.route('/api/biblia/capitulos/45/versiculos/<capitulo>', methods=['GET'])
def zacarias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/zacarias{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Zacarias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Zacarias', "Capítulo" : capitulo , "Versículos" : data} )       

###################################################################################    

# 46.Lista de Capitulos de Malaquias
@app.route('/api/biblia/capitulos/46', methods=['GET'])
def malaquias_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 1, "Livro" : 'Malaquias', "Capítulos" : data} ) 

###################################################################################

# 46. Livro de Cântico de Malaquias
@app.route('/api/biblia/capitulos/46/versiculos/<capitulo>', methods=['GET'])
def malaquias(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sofonias{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 1, "Livro" : 'Malaquias', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 1, "Livro" : 'Malaquias', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################
################################   NOVO TESTAMENTO   ##############################
###################################################################################

# 47.Lista de Capitulos de São Mateus
@app.route('/api/biblia/capitulos/47', methods=['GET'])
def mateus_capitulos():
    data = []
    for x in range(1, 29):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'São Mateus', "Capítulos" : data} ) 

###################################################################################

# 47. Livro de Cântico de são Mateus
@app.route('/api/biblia/capitulos/47/versiculos/<capitulo>', methods=['GET'])
def mateus(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/mateus{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'São Mateus', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'São Mateus', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################

# 48.Lista de Capitulos de São Mateus
@app.route('/api/biblia/capitulos/48', methods=['GET'])
def sao_marcos_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'São Mateus', "Capítulos" : data} ) 

###################################################################################

# 48. Livro de Cântico de São Marcos
@app.route('/api/biblia/capitulos/48/versiculos/<capitulo>', methods=['GET'])
def sao_marcos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sao-marcos{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'São Marcos', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'São Marcos', "Capítulo" : capitulo , "Versículos" : data} )       

###################################################################################

# 49.Lista de Capitulos de São Lucas
@app.route('/api/biblia/capitulos/49', methods=['GET'])
def sao_lucas_capitulos():
    data = []
    for x in range(1, 25):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'São Lucas', "Capítulos" : data} ) 

###################################################################################

# 49. Livro de Cântico de São Lucas
@app.route('/api/biblia/capitulos/49/versiculos/<capitulo>', methods=['GET'])
def sao_lucas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sao-lucas{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'São Lucas', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'São Lucas', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 50.Lista de Capitulos de São João
@app.route('/api/biblia/capitulos/50', methods=['GET'])
def sao_joao_capitulos():
    data = []
    for x in range(1, 22):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'São João', "Capítulos" : data} ) 

###################################################################################

# 50. Livro de Cântico de São João
@app.route('/api/biblia/capitulos/50/versiculos/<capitulo>', methods=['GET'])
def sao_joao(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sao-joao{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'São João', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'São João', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 51.Lista de Capitulos dos Atos dos Apóstolos
@app.route('/api/biblia/capitulos/51', methods=['GET'])
def atos_dos_apostolos_capitulos():
    data = []
    for x in range(1, 29):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Atos dos Apóstolos', "Capítulos" : data} ) 

###################################################################################

# 51. Livro dos Atos dos Apóstolos
@app.route('/api/biblia/capitulos/51/versiculos/<capitulo>', methods=['GET'])
def atos_dos_apostolos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/atos-dos-apostolos{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Atos dos Apóstolos', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Atos dos Apóstolos', "Capítulo" : capitulo , "Versículos" : data} ) 

###################################################################################

# 52.Lista de Capitulos dos Romanos
@app.route('/api/biblia/capitulos/52', methods=['GET'])
def romanos_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Atos dos Apóstolos', "Capítulos" : data} ) 

###################################################################################

# 52. Livro dos Atos dos Romanos
@app.route('/api/biblia/capitulos/52/versiculos/<capitulo>', methods=['GET'])
def romanos(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/romanos{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Romanos', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Romanos', "Capítulo" : capitulo , "Versículos" : data} )   


###################################################################################

# 53.Lista de Capitulos dos I Corintios
@app.route('/api/biblia/capitulos/53', methods=['GET'])
def i_corintios_capitulos():
    data = []
    for x in range(1, 17):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'I Coríntios', "Capítulos" : data} ) 

###################################################################################

# 53. Livro dos Atos dos Romanos
@app.route('/api/biblia/capitulos/53/versiculos/<capitulo>', methods=['GET'])
def i_corintios(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-corintios{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'I Coríntios', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'I Coríntios', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################

# 54.Lista de Capitulos dos II Corintios
@app.route('/api/biblia/capitulos/54', methods=['GET'])
def ii_corintios_capitulos():
    data = []
    for x in range(1, 14):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II Coríntios', "Capítulos" : data} ) 

###################################################################################

# 52. Livro dos Atos dos Romanos
@app.route('/api/biblia/capitulos/54/versiculos/<capitulo>', methods=['GET'])
def ii_corintios(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-corintios{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'II Coríntios', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'II Coríntios', "Capítulo" : capitulo , "Versículos" : data} ) 


###################################################################################

# 55.Lista de Capitulos dos Gálatas
@app.route('/api/biblia/capitulos/55', methods=['GET'])
def galatas_capitulos():
    data = []
    for x in range(1, 7):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Gálatas', "Capítulos" : data} ) 

###################################################################################

# 55. Livro dos Atos dos Gálatas
@app.route('/api/biblia/capitulos/55/versiculos/<capitulo>', methods=['GET'])
def galatas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/galatas/{}".format(capitulo)

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
        
        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Gálatas', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Gálatas', "Capítulo" : capitulo , "Versículos" : data} ) 


###################################################################################

# 56.Lista de Capitulos dos Efésios
@app.route('/api/biblia/capitulos/56', methods=['GET'])
def efesios_capitulos():
    data = []
    for x in range(1, 7):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Efésios', "Capítulos" : data} ) 

###################################################################################

# 56. Livro dos Atos dos Efésios
@app.route('/api/biblia/capitulos/56/versiculos/<capitulo>', methods=['GET'])
def efesios(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/efesios/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Efésios', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Efésios', "Capítulo" : capitulo , "Versículos" : data} ) 


###################################################################################

# 57.Lista de Capitulos dos Filipenses
@app.route('/api/biblia/capitulos/57', methods=['GET'])
def filipenses_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Filipenses', "Capítulos" : data} ) 

###################################################################################

# 57. Livro dos Atos dos Filipenses
@app.route('/api/biblia/capitulos/57/versiculos/<capitulo>', methods=['GET'])
def filipenses(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/filipenses/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Filipenses', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Filipenses', "Capítulo" : capitulo , "Versículos" : data} ) 


###################################################################################

# 58.Lista de Capitulos dos Colosenses
@app.route('/api/biblia/capitulos/58', methods=['GET'])
def colosenses_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Colossenses', "Capítulos" : data} ) 

###################################################################################

# 58. Livro dos Atos dos Filipenses
@app.route('/api/biblia/capitulos/58/versiculos/<capitulo>', methods=['GET'])
def colosenses(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/colossenses/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Colossenses', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Colossenses', "Capítulo" : capitulo , "Versículos" : data} )     


###################################################################################

# 59.Lista de Capitulos dos I Tessalonicenses
@app.route('/api/biblia/capitulos/59', methods=['GET'])
def i_tessalonicenses_capitulos():
    data = []
    for x in range(1, 6):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'I Tessalonicenses', "Capítulos" : data} ) 

###################################################################################

# 59. Livro dos Atos I Tessalonicenses
@app.route('/api/biblia/capitulos/59/versiculos/<capitulo>', methods=['GET'])
def i_tessalonicenses(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-tessalonicenses/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'I Tessalonicenses', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'I Tessalonicenses', "Capítulo" : capitulo , "Versículos" : data} )    


###################################################################################

# 60.Lista de Capitulos dos II Tessalonicenses
@app.route('/api/biblia/capitulos/60', methods=['GET'])
def ii_tessalonicenses_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II Tessalonicenses', "Capítulos" : data} ) 

###################################################################################

# 60. Livro dos Atos I Tessalonicenses
@app.route('/api/biblia/capitulos/60/versiculos/<capitulo>', methods=['GET'])
def ii_tessalonicenses(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-tessalonicenses/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'II Tessalonicenses', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'II Tessalonicenses', "Capítulo" : capitulo , "Versículos" : data} )    


###################################################################################

# 61.Lista de Capitulos do I Timóteo
@app.route('/api/biblia/capitulos/61', methods=['GET'])
def i_timoteo_capitulos():
    data = []
    for x in range(1, 7):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'I Timóteo', "Capítulos" : data} ) 

###################################################################################

# 61. Livro de I Timóteo
@app.route('/api/biblia/capitulos/61/versiculos/<capitulo>', methods=['GET'])
def i_timoteo(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-timoteo/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'I Timóteo', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'I Timóteo', "Capítulo" : capitulo , "Versículos" : data} )  


###################################################################################

# 62.Lista de Capitulos do II Timóteo
@app.route('/api/biblia/capitulos/62', methods=['GET'])
def ii_timoteo_capitulos():
    data = []
    for x in range(1, 5):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II Timóteo', "Capítulos" : data} ) 

###################################################################################

# 62. Livro de II Timóteo
@app.route('/api/biblia/capitulos/62/versiculos/<capitulo>', methods=['GET'])
def ii_timoteo(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-timoteo/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'II Timóteo', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'II Timóteo', "Capítulo" : capitulo , "Versículos" : data} )   


###################################################################################

# 63.Lista de Tito
@app.route('/api/biblia/capitulos/63', methods=['GET'])
def tito_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Tito', "Capítulos" : data} ) 

###################################################################################

# 63. Livro de Tito
@app.route('/api/biblia/capitulos/63/versiculos/<capitulo>', methods=['GET'])
def tito(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/tito/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Tito', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Tito', "Capítulo" : capitulo , "Versículos" : data} )   

###################################################################################

# 64.Lista de Filemon
@app.route('/api/biblia/capitulos/64', methods=['GET'])
def filemon_capitulos():
    data = []
    for x in range(1, 2):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Tito', "Capítulos" : data} ) 

###################################################################################

# 64. Livro de Tito
@app.route('/api/biblia/capitulos/64/versiculos/<capitulo>', methods=['GET'])
def filemon(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/filemon/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'FiLêmon', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Filêmon', "Capítulo" : capitulo , "Versículos" : data} ) 


###################################################################################

# 65.Lista de Hebreus
@app.route('/api/biblia/capitulos/65', methods=['GET'])
def hebreus_capitulos():
    data = []
    for x in range(1, 14):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Hebreus', "Capítulos" : data} ) 

###################################################################################

# 65. Livro de Hebreus
@app.route('/api/biblia/capitulos/65/versiculos/<capitulo>', methods=['GET'])
def hebreus(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/hebreus/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Hebreus', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Hebreus', "Capítulo" : capitulo , "Versículos" : data} )   


###################################################################################

# 66.Lista de São Tiago
@app.route('/api/biblia/capitulos/66', methods=['GET'])
def sao_tiago_capitulos():
    data = []
    for x in range(1, 6):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'São Tiago', "Capítulos" : data} ) 

###################################################################################

# 65. Livro de Hebreus
@app.route('/api/biblia/capitulos/66/versiculos/<capitulo>', methods=['GET'])
def sao_tiago(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/sao-tiago/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'São Tiago', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'São Tiago', "Capítulo" : capitulo , "Versículos" : data} )

###################################################################################

# 67.Lista de livros I São Pedro
@app.route('/api/biblia/capitulos/67', methods=['GET'])
def i_sao_pedro_capitulos():
    data = []
    for x in range(1, 6):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'I São Pedro', "Capítulos" : data} ) 

###################################################################################

# 67. Livro de I São Pedro
@app.route('/api/biblia/capitulos/67/versiculos/<capitulo>', methods=['GET'])
def i_sao_pedro(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-sao-pedro/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'I São Pedro', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'I São Pedro', "Capítulo" : capitulo , "Versículos" : data} )  

###################################################################################

# 68.Lista de Livros do II São Pedro
@app.route('/api/biblia/capitulos/68', methods=['GET'])
def ii_sao_pedro_capitulos():
    data = []
    for x in range(1, 4):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II São Pedro', "Capítulos" : data} ) 

###################################################################################

# 68. Livro de II São Pedro
@app.route('/api/biblia/capitulos/68/versiculos/<capitulo>', methods=['GET'])
def ii_sao_pedro(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-sao-pedro/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'II São Pedro', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'II São Pedro', "Capítulo" : capitulo , "Versículos" : data} )  


###################################################################################

# 69.Lista de Livros do I São João
@app.route('/api/biblia/capitulos/69', methods=['GET'])
def i_sao_joao_capitulos():
    data = []
    for x in range(1, 6):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II São Pedro', "Capítulos" : data} ) 

###################################################################################

# 69. Livro de I São João
@app.route('/api/biblia/capitulos/69/versiculos/<capitulo>', methods=['GET'])
def i_sao_joao(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/i-sao-joao/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'I São João', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'I São João', "Capítulo" : capitulo , "Versículos" : data} )  


###################################################################################

# 70.Lista de Livros do II São João
@app.route('/api/biblia/capitulos/70', methods=['GET'])
def ii_sao_joao_capitulos():
    data = []
    for x in range(1, 2):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II São João', "Capítulos" : data} ) 

###################################################################################

# 70. Livro de II São João
@app.route('/api/biblia/capitulos/70/versiculos/<capitulo>', methods=['GET'])
def ii_sao_joao(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-sao-joao/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'II São João', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'II São João', "Capítulo" : capitulo , "Versículos" : data} )     


###################################################################################

# 71.Lista de Livros do III São João
@app.route('/api/biblia/capitulos/70', methods=['GET'])
def iii_sao_joao_capitulos():
    data = []
    for x in range(1, 2):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'II São João', "Capítulos" : data} ) 

###################################################################################

# 71. Livro de III São João
@app.route('/api/biblia/capitulos/71/versiculos/<capitulo>', methods=['GET'])
def iii_sao_joao(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/iii-sao-joao/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'III São João', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'III São João', "Capítulo" : capitulo , "Versículos" : data} )   



###################################################################################

# 72.Lista de Livros do São Judas
@app.route('/api/biblia/capitulos/72', methods=['GET'])
def sao_judas_capitulos():
    data = []
    for x in range(1, 2):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'São Judas', "Capítulos" : data} ) 

###################################################################################

# 72. Livro de São Judas
@app.route('/api/biblia/capitulos/72/versiculos/<capitulo>', methods=['GET'])
def ii_sao_judas(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/ii-sao-judas/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'São Judas', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'São Judas', "Capítulo" : capitulo , "Versículos" : data} )     


###################################################################################

# 73.Lista de Livros do Apocalipse
@app.route('/api/biblia/capitulos/73', methods=['GET'])
def apocalipse_capitulos():
    data = []
    for x in range(1, 23):

        data.append( { "capítulo" : x } ) 
     
    return jsonify({ "Testamento" : 2, "Livro" : 'Apocalipse', "Capítulos" : data} ) 

###################################################################################

# 73. Livro do Apocalipse
@app.route('/api/biblia/capitulos/73/versiculos/<capitulo>', methods=['GET'])
def apocalipse(capitulo):
    URL = "https://www.bibliacatolica.com.br/biblia-ave-maria/apocalipse/{}".format(capitulo)

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

        # Se for um livro inexistente, a chamada original retorna o primeiro livro de Genesis
        if s == "No princípio, Deus criou os céus e a terra." :
           return jsonify({ "Testamento" : 2, "Livro" : 'Apocalipse', "Capítulo" : capitulo , "Versículos" : [] } )  

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
    return jsonify({ "Testamento" : 2, "Livro" : 'Apocalipse', "Capítulo" : capitulo , "Versículos" : data} )  

#####################################################################################
#                                   F I M                                           #
# ###################################################################################    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='0.0.0.1', port=port)    
