import requests
from PIL import Image, ImageDraw
from random import randint
from io import BytesIO
import json


# NOTE:

def test_api():
    """
        in This test, we create random image and simulate POST method
        Pillow Don't Support JPG Format
    :return:
    """
    # PNG
    image = Image.new('RGB', size=(randint(100, 1000), randint(100, 1000)), color=(200, 100, 100))
    image.save('image', 'png')

    resp = requests.post(
        url='http://localhost:8000',
        data=open('image', 'rb'),
        headers={'content-type': 'image/png'}
    )
    assert resp.status_code == 200
    resp = resp.json()
    assert resp['width'] == image.width
    assert resp['height'] == image.height
    assert resp['format'] == 'PNG'

    # GIF
    image = Image.new('RGB', size=(randint(100, 1000), randint(100, 1000)), color=(200, 100, 100))
    image.save('image', 'GIF')

    resp = requests.post(
        url='http://localhost:8000',
        data=open('image', 'rb'),
        headers={'content-type': 'image/png'}
    )
    assert resp.status_code == 200
    resp = resp.json()
    assert resp['width'] == image.width
    assert resp['height'] == image.height
    assert resp['format'] == 'GIF'

    # JPEG
    image = Image.new('RGB', size=(randint(100, 1000), randint(100, 1000)), color=(200, 100, 100))
    image.save('image', 'JPEG')

    resp = requests.post(
        url='http://localhost:8000',
        data=open('image', 'rb'),
        headers={'content-type': 'image/png'}
    )
    assert resp.status_code == 200
    resp = resp.json()
    assert resp['width'] == image.width
    assert resp['height'] == image.height
    assert resp['format'] == 'JPEG'
