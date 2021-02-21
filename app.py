import json
from flask import Flask, jsonify, request, render_template, redirect, url_for
from flaskext.markdown import Markdown

from process_entity_named import process_entity, process_parse_dependency


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

app = Flask(__name__)
Markdown(app)

@app.route("/")
def index():
    """
    Rota para pagina index

    Returns:
        [Page]: Retorna a pagina para ser renderizada 
    """
    return render_template('index.html' )


@app.route("/process", methods=['GET','POST'])
def process():
    """
    Rota que vai receber um post com os dados, fazer o processamento na usando a
    função process_entity e retorna as entidades nomeadas
    """
    if request.method == 'POST':
        #obtendo o dado do form
        query = request.form['query']    
        #obtendo as entidades nomeadas pr
        obj_html = process_entity(query)
        #formatando os dados para serem exibidos no front
        result = HTML_WRAPPER.format(obj_html)

    return render_template('result.html', query=query ,result=result)

@app.route("/result")
def result():
    return render_template('result.html')


@app.route("/result_parse", methods=['GET','POST'])
def process_parse():
    """
    Rota que vai receber um post com os dados, fazer o processamento na usando a
    função process_parse_dependency e retorna o parse de denpendencia
    """

    if request.method == 'POST':
        #obtendo o dado do form
        query = request.form['query']    
        #obtendo o parse de dependencia
        obj_html = process_parse_dependency(query)
        #formatando os dados para serem exibidos no front
        result = HTML_WRAPPER.format(obj_html)

    return render_template('result_parse.html', query=query ,result=result)

@app.route("/parse_dep")
def parse_dep():
    return render_template('parse_dep.html')


if __name__ == '__main__':
    app.run(debug=True)
