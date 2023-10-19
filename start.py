#!/home/vic/houses/venv/bin/python3

from flask import Flask, request
from svggen import housebuilder

app = Flask(__name__)

@app.route('/', defaults={'width': None, 'height': None})
@app.route('/<width>/<height>')
def index(width=None, height=None):
    if not width or not height:
        return """
        <script>
        (() => window.location.href =
        ['', window.innerWidth, window.innerHeight].join('/'))()
        </script>
        """
    return builder(width, height)

def builder(width, height):
    data = housebuilder(width, height) # <- получаем список SVG кодов случайных Домов
    html = []
    # -- Обарачиваем SVG коды в форматированный блок div (для красивого отображения)
    for row in data:
        html.append(f'<div id=row#{data.index(row)} style="width: 100%; display: inline-flex;flex-wrap: wrap;justify-content: space-between;">')
        for block in row:
            html.append(f'<div style="display: grid;justify-content: center;width: fit-content;"> {block} </div>')
        html.append(f'</div>')
    content = '\n'.join(html)
    button = f"""
        <form action="/">
            <input type="submit" value="Обновить" />
        </form>
        """
    body = f'{button} <div> {content} </div>'
    return body

if __name__ == '__main__':
    app.run('0.0.0.0', 8080) # <- запускаем веб-сервер, указываем хост и порт