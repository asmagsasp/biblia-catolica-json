# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import os   
#import urllib.request as urllib2
import urllib2

app = Flask(__name__)

URL = "https://www.bibliacatolica.com.br/"
    
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
                       data.append( { i : current_frase  } )
                       prior_word = ""

               else:   
                  i = i + 1
                  data.append( { i : current_word } )    

    return jsonify({'livros': data})  

@app.route('/api/biblia/genesis', methods=['GET'])
def genesis_capitulos():
    req  = urllib2.Request(URL)
    req.add_header('User-Agent','Mozilla/5.0')
    resp = urllib2.urlopen(req)
    html_doc = resp.read()

    soup = BeautifulSoup(html_doc, "html.parser")
    data = []

    for dataBox in soup.find_all("div", class_="rightsidebar"):
        for ulBox in dataBox.find_all("ul", class_="listChapter"):

            s = ulBox.text

            #verso = s[:3]
            #s = s.replace(verso,"")
            #v = int(verso.replace(".",""))
            #data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 

    even = 1
    for dataBox in soup.find_all("p", class_="even"):
    
        s = dataBox.text
        verso = s[:3]
        s = s.replace(verso,"")
        v = int(verso.replace(".",""))
        data.append( { "verso" : { "versiculo" : v, "texto" : s } } ) 
        even = even + 1

    data = sorted(data, key=lambda k: k['verso'].get('versiculo', 0), reverse=False)
     
    return jsonify({'genesis': data})      

@app.route('/api/biblia/genesis/<capitulo>', methods=['GET'])
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
     
    return jsonify({'genesis': data})    

@app.route('/api/biblia/exodo/<capitulo>', methods=['GET'])
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
    return jsonify({'exodo': data})     

@app.route('/api/biblia/levitico/<capitulo>', methods=['GET'])
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
    return jsonify({'levitico': data})  

@app.route('/api/biblia/numeros/<capitulo>', methods=['GET'])
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
    return jsonify({'numeros': data})  

@app.route('/api/biblia/deuteronomio/<capitulo>', methods=['GET'])
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
    return jsonify({'deuteronomio': data})  

@app.route('/api/biblia/josue/<capitulo>', methods=['GET'])
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
    return jsonify({'josue': data})  

@app.route('/api/biblia/juizes/<capitulo>', methods=['GET'])
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
    return jsonify({'juizes': data})   

@app.route('/api/biblia/rute/<capitulo>', methods=['GET'])
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
    return jsonify({'rute': data})  

@app.route('/api/biblia/isamuel/<capitulo>', methods=['GET'])
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
    return jsonify({'I Samuel': data})  

@app.route('/api/biblia/iisamuel/<capitulo>', methods=['GET'])
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
    return jsonify({'II Samuel': data}) 

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
    app.run(host='127.0.0.1', port=port)    
