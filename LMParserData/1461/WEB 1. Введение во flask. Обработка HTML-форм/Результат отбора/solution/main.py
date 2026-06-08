from flask import Flask, request, url_for
import random as r
import os

app = Flask(__name__)
page_is_been_loaded = False


@app.route('/')
def _():
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
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
                    <link rel="stylesheet" href="static/css/style.css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 id="header">
                        Жди нас, Марс!
                    </h1>
                    <img src="https://img.freepik.com/premium-photo/png-outdoors-planet-space-moon_53876-920835.jpg?semt=ais_hybrid&w=740"
                    style='width: 50vh; height:50vh;'></br>
                    <h4 class='bg-secondary p-2 text-dark bg-opacity-25'>Человечество вырастает из детства.</h4>
                    <h4 class='bg-success p-2 text-dark bg-opacity-25'>Человечеству мала одна планета.</h4>
                    <h4 class='bg-secondary p-2 text-dark bg-opacity-25'>Мы сделаем обитаемыми безжизненные пока планеты.</h4>
                    <h4 class='bg-warning p-2 text-dark bg-opacity-25'>И начнем с Марса!</h4>
                    <h4 class='bg-danger p-2 text-dark bg-opacity-25'>Присоединяйся!</h4>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return get_load_photo()
        
    elif request.method == 'POST':
      f = request.files['file']
      f.save(f'static/img/{r.randint(100000000, 999999999)}.webp')
      return get_load_photo()


def get_load_photo():
    string = ''
    for obj in os.listdir("static/img"):
      string += (f'<img class="cell" src="static/img/{obj}">\n') 
    print(string)

    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3-beta1/dist/css/bootstrap.min.css">
                            <link rel="stylesheet" type="text/css" href="static/css/style.css" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1 id="header">Выставка фотографий марса</h1>
                            <div id="grid_for_photo">
                                <form method="post" enctype="multipart/form-data">
                                  <div class="form-group">
                                        <label for="photo" style="font-size: 5vh;">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary" style="font-size: 3vh; padding: 2vh;">Отправить</button>
                                </form>
                                {string}
                            </div>
                          </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
                    <link rel="stylesheet" href="static/css/style.css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 id="header">
                        Пейзажи Марса!
                    </h1>
                    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel" style="position: absolute; width: 70vw; height: 70vh; left: 15vw; top: 5vw">
                    <div class="carousel-inner">
                    <div class="carousel-indicators">
                      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                      <div class="carousel-item active">
                        <img src="static/img/1.jpg" class="d-block w-100" style="height: 75vh;" alt="...">
                      </div>
                      <div class="carousel-item">
                        <img src="static/img/2.webp" class="d-block w-100" style="height: 75vh;" alt="...">
                      </div>
                      <div class="carousel-item">
                        <img src="static/img/3.avif" class="d-block w-100" style="height: 75vh;" alt="...">
                      </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                      <span class="carousel-control-next-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Next</span>
                    </button>
                  </div>
                  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
                    <link rel="stylesheet" href="static/css/style.css">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h2>Эта планеты близка к Земле;</h1>
                    <h4 class='bg-success p-2 text-dark bg-opacity-25'>На ней много необъодимых ресурсов;</h4>
                    <h4 class='bg-secondary p-2 text-dark bg-opacity-25'>На ней есть вода и атмосфера;</h4>
                    <h4 class='bg-warning p-2 text-dark bg-opacity-25'>На ней есть небольшое магнитное поле;</h4>
                    <h4 class='bg-danger p-2 text-dark bg-opacity-25'>Наконец, она просто красива!</h4>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
                    <link rel="stylesheet" href="static/css/style.css">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h1>
                    <h4 class='bg-success p-2 text-dark bg-opacity-25'>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
                    <h3>составляет {rating}!</h3>
                    <h4 class='bg-warning p-2 text-dark bg-opacity-25'>Желаем удачи!</h4>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')