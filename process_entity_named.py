import spacy
from spacy import   displacy


def process_entity(texto):
    """[summary]
        Função para retorna o reconhecimento das entidades nemeadas do texto processado
    Args:
        texto (string): Texto enviado para ser processado

    Returns:
        [Objeto]: Objeto html gerado pelo displacy.render
    """
    nlp = obj_nlp()
    doc = nlp(texto)

    obj_html = displacy.render(doc, style='ent')
    
    return obj_html


def process_parse_dependency(texto):
    """
        Função para retorna à análise de dependência do texto processado
    Args:
        texto (string): Texto enviado para ser processado

    Returns:
        [Objeto]: Objeto html gerado pelo displacy.render
    """
    nlp = obj_nlp()
    doc = nlp(texto)

    obj_html = displacy.render(doc, style='dep')

    return obj_html

def obj_nlp():
    """
        Instanciando objet spacy com idioma PT
    Returns:
        [Objeto]: Instancia do spacy
    """
    nlp = spacy.load('pt')
    
    return nlp