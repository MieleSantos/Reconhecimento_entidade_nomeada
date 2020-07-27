import spacy
from spacy import   displacy


def process_entity(texto):
    
    nlp = spacy.load('pt')
    
    doc = nlp(texto)

    # for entidades in doc.ents:
    # print(entidades.text, entidades.label_)

    # displacy.render(doc, style = "ent", jupyter=True)

    obj_html = displacy.render(doc, style='ent')
    # obj_html = displacy.parse_deps(doc)
    return obj_html