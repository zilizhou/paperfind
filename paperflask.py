## -*- coding: utf-8 -*-
import paperidx
from flask import Flask,request,render_template,redirect
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('paperfind.html')

@app.route('/search',methods=['GET','POST'])
def search():
    result={}
    if request.method == 'POST':
        resu=[]
        if request.form['sel']=='paper':
            paper = request.form['qinfo'].strip().lower()
            resu=paperidx.searInfo(paper)
            result['paper']=resu
            result['journal']=[]
        if request.form['sel']=='journal':
            jour = request.form['qinfo'].strip().lower()
            resu=paperidx.searjInfo(jour)
            print(resu)
            result['paper'] = []
            result['journal'] = resu
        print(result)
        # print(resu)
        # journal = request.form['sel']
        return json.dumps(result,ensure_ascii=False)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)