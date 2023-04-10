from django.shortcuts import render
import datetime
from django.http import JsonResponse
import json, spacy

import spacy
# nlp = spacy.load("fr_core_news_md")
nlp = spacy.load("ja_core_news_sm")

def home(request):
    return render(request, 'home.html')

def variables(request):
    nom = "エドワード"
    hobbies = ["卓球", "読書", "音楽"]

    membres = [
        {"nom": "Dupond", "prenom": "Sophie"},
        {"nom": "Hache", "prenom": "Anne"},
        {"nom": "Von Ergstadt", "prenom": "Émile"},
        {"nom": "Dupuit", "prenom": "Alex"},
    ]

    bigmac = {
        "Énergie": "504kcal",
        "Matières grasses": "25g",
        "Dont acides gras saturés": "9,2g",
        "Sucres": "8,2g",
        "Sel": "2,2g"
    }
    langue = "en"


    date_birthday = datetime.date(1992, 12, 24)

    return render(request, 'variables.html', {"nom": nom, "hobbies": hobbies, "membres": membres, "bigmac": bigmac, "langue": langue, "data_birthday": date_birthday})
    # return render(request, 'variables.html', {"nom": nom, "hobbies": hobbies})

def runThree(request):
    return render(request, 'three.html')

def runSpacy(request):
    colis = json.loads(request.body)
    text = colis['inText']
    print("À analyser :",text)

    output = nlp(text)
    rep = []
    for token in output:
        rep.append((token.text, token.pos_))

    reponse = {
       "reponse":rep
    }

    return JsonResponse(reponse)
