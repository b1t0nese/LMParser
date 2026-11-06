from flask import Flask, url_for, request, render_template
import random
import os

app = Flask(__name__)


@app.route("/")
def osn():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return "</br>".join(
        [
            "Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!",
        ]
    )


@app.route("/image_mars")
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


@app.route("/galery", methods=["POST", "GET"])
def galery():
    if request.method == "GET":
        return render_template(
            "galery.html", title="Красная планета",
            dirs=os.listdir("static/img/mars_desert"))
    elif request.method == "POST":
        request.files["file"].save(f"static/img/mars_desert/{random.seed()}.webp")
        return render_template(
            "galery.html", title="Красная планета",
            dirs=os.listdir("static/img/mars_desert"))


if __name__ == "__main__":
    app.run()
