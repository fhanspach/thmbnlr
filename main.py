from StringIO import StringIO
from flask import Flask, send_file, request, redirect

from PIL import Image
import requests
import sys

app = Flask(__name__)


def resize_image(file_type, width, height, quality, image):
    size = (width, height)
    img = Image.open(StringIO(image))
    img_io = StringIO()
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(img_io, format=file_type, quality=quality)
    img_io.seek(0)
    return img_io


@app.route("/")
def get_image():
    url = request.args.get('url', None)
    if not url:
        return "URL must not be None!"
    # TODO test if request is an image

    width = int(request.args.get('width', sys.maxint))
    height = int(request.args.get('height', sys.maxint))
    quality = int(request.args.get('quality', 100))
    max_size = int(request.args.get('max_size', 0))

    if max_size > 0:
        max_size *= 1024

    header = requests.head(url).headers

    content_type = header.get("content-type")
    response_type, file_type = content_type.split('/')
    if not response_type == "image":
        return "Not an image!"

    response_size = header.get('Content-Length', sys.maxint)
    in_size = int(response_size) <= max_size

    if (height == sys.maxint and width == sys.maxint and quality == 100) or in_size:
        return redirect(url)

    if quality > 100:
        quality = 100
    elif quality < 0:
        # todo better errors
        return "quality must not be under 0!"

    response = requests.get(url)

    img_io = resize_image(file_type, width, height, quality, response.content)

    return send_file(img_io, mimetype=content_type)


if __name__ == "__main__":
    app.run(debug=True)