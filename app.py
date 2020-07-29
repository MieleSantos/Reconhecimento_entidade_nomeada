import json
from flask import Flask, jsonify, request, render_template, redirect, url_for
from flaskext.markdown import Markdown

from process_entity_named import process_entity, process_parse_dependency


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

app = Flask(__name__)
Markdown(app)

@app.route("/")
def index():

    return render_template('index.html' )


@app.route("/process", methods=['GET','POST'])
def process():

    if request.method == 'POST':

        query = request.form['query']    
        
        obj_html = process_entity(query)
        
        result = HTML_WRAPPER.format(obj_html)

    return render_template('result.html', query=query ,result=result)

@app.route("/result")
def result():
    return render_template('result.html')


@app.route("/result_parse", methods=['GET','POST'])
def process_parse():

    if request.method == 'POST':

        query = request.form['query']    
        
        obj_html = process_parse_dependency(query)
        result = HTML_WRAPPER.format(obj_html)


    return render_template('result_parse.html', query=query ,result=result)

@app.route("/parse_dep")
def parse_dep():
    return render_template('parse_dep.html')


if __name__ == '__main__':
    app.run(debug=True)