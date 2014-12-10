from StringIO import StringIO
from flask import Flask, send_file
from flask import request
from PIL import Image
import requests
import sys

app = Flask(__name__)


@app.route("/")
def get_image():
    url = request.args.get('url', None)
    if not url:
        return "Url must not be None!"
    # TODO test if request is an image

    width = int(request.args.get('width', sys.maxint))
    height = int(request.args.get('height', sys.maxint))
    quality = int(request.args.get('quality', 100))
    response = requests.get(url)

    if height == sys.maxint and width == sys.maxint and quality == 100:
        return response.content, response.status_code, response.headers.items()
    if quality > 100:
        quality = 100
    elif quality < 0:
        # todo better errors
        return "quality must not be under 0!"

    size = (width, height)

    content_type = response.headers.get("content-type")
    response_type, file_type = content_type.split('/')
    if not response_type == "image":
        return "Not an image!"

    img = Image.open(StringIO(response.content))

    img_io = StringIO()
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(img_io, format=file_type, quality=quality)

    img_io.seek(0)

    return send_file(img_io, mimetype=content_type)


if __name__ == "__main__":
    app.run(debug=True)