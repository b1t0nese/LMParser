from flask import Flask, url_for
import os

app = Flask(__name__)


@app.route('/')
def osn():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "</br>".join(["Человечество вырастает из детства.", 
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!", "Присоединяйся!"])


@app.route('/image_mars')
def image_mars():
    return f"""<title>Привет Марс!</title><h1>Жди нас, Марс!</h1>
<img src="{url_for('static', filename='img/mars.avif')}">
</br>Вот она какая, красная планета."""


@app.route("/promotion_image")
def promotion_image():
    return f"""
<head>
    <title>Колонизация</title>
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
</head>
<body>
    <h1 class='red_color'>Жди нас, Марс!</h1>
    <img class='image' src="{url_for('static', filename='img/mars.avif')}">
    <h4 class='bg-secondary p-2 text-dark bg-opacity-50'>Человечество вырастает из детства.</h4>
    <h4 class='bg-success p-2 text-success bg-opacity-25'>Человечеству мала одна планета.</h4>
    <h4 class='bg-secondary p-2 text-dark bg-opacity-25'>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
    <h4 class='bg-warning p-2 text-warning bg-opacity-10'>И начнём с Марса!</h4>
    <h4 class='bg-danger p-2 text-danger bg-opacity-25'>Присоединяйся!</h4>
</body>"""


@app.route("/carousel")
def carousel():
    carousel_data = "".join([f"""
            <div class="carousel-item{" active" if i==0 else ""}">
                <img class="d-block w-100" src="{url_for('static', filename=f'img/mars_desert/{f}')}" alt="Mars landscape">
            </div>""" for i, f in enumerate(os.listdir('static/img/mars_desert'))])
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Пейзажи Марса</title>
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
</head>
<body>
    <h1 style="position: relative; text-align: center;">Пейзажи Марса</h1>
    <div id="carouselControls" class="carousel slide" data-bs-ride="carousel" style="width: 70%; margin: 0 auto;">
        <div class="carousel-inner">
{carousel_data}
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselControls" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselControls" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')