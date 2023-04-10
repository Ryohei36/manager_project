import spacy
# nlp = spacy.load("fr_core_news_md")
nlp = spacy.load("ja_core_news_sm")

doc = nlp("はじめまして！みなさんこんにちわ！")
# doc = nlp("Ceci est une phrase d'exemple.")
print(doc.text)
for token in doc:
    print(token.text, token.lemma_, token.pos_,
          token.morph.to_dict(), token.dep_, token.shape_)
