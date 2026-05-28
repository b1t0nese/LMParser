from flask import Flask, request, render_template
import random as r
import os


SCRIPT_PATH = os.path.dirname(__file__)
app = Flask(__name__, template_folder=os.path.join(
    SCRIPT_PATH, 'static', 'templates'))


@app.route('/')
def slesh():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return """<title>Привет, Марс!</title><h1>Жди нас, Марс!</h1>
<img src="https://img.freepik.com/premium-photo/png-outdoors-planet-space-moon_53876-920835.jpg?semt=ais_hybrid&w=740"
style='background-width: 50vh; background-height:50vh; width: 50vh; height:50vh;'></br>
Вот она какая, красная планета!"""


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    images_path = os.path.join(SCRIPT_PATH, 'static', 'img')
    if request.method == 'POST':
        request.files['file'].save(os.path.join(images_path, f'loaded_photo.webp'))
    images = f'<img class="cell" src="/static/img/loaded_photo.webp">\n' if os.path.exists(
        os.path.join(images_path, 'loaded_photo.webp')) else ''
    return render_template('load_photo.html', images=images)


if __name__ == '__main__':
    app.run()