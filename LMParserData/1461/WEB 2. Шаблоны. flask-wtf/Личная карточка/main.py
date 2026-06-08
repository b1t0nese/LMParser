from flask import Flask, render_template, request
import random as r
import os
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'GET':
        return render_template('galery.html', title='Красная планета', dirs=os.listdir("static/img/carousel")[1:])
    elif request.method == 'POST':
        f = request.files['file']
        f.save(f'static/img/carousel/{r.randint(100000000, 999999999)}.webp')
        return render_template('galery.html', title='Красная планета', dirs=os.listdir("static/img/carousel")[1:])


@app.route('/members')
def members():
    with open("templates/members.json", "rt", encoding="utf8") as f:
        mb = json.loads(f.read())['members']
        mb = mb[r.randint(0, len(mb) - 1)]
    roles_str = ''
    for obj in sorted(mb['role']):
        roles_str += obj + ', '
    roles_str = roles_str[:-2]
    return render_template('members.html', title='Экипаж', fullname=mb['name']+' '+mb['subname'], img_path=mb['image_path'], roles=roles_str)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')