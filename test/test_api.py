import requests

from PIL import Image
from random import randint


class TestAPI:
    """
        in This test, we create random image and simulate POST method
        Pillow Don't Support JPG Format
    """

    # PNG
    def test_png(self):
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
    def test_gif(self):
        image = Image.new('RGB', size=(randint(100, 1000), randint(100, 1000)), color=(200, 100, 100))
        image.save('image', 'GIF')

        resp = requests.post(
            url='http://localhost:8000',
            data=open('image', 'rb'),
            headers={'content-type': 'image/gif'}
        )
        assert resp.status_code == 200
        resp = resp.json()
        assert resp['width'] == image.width
        assert resp['height'] == image.height
        assert resp['format'] == 'GIF'

    # JPEG
    def test_jpeg(self):
        image = Image.new('RGB', size=(randint(100, 1000), randint(100, 1000)), color=(200, 100, 100))
        image.save('image', 'JPEG')

        resp = requests.post(
            url='http://localhost:8000',
            data=open('image', 'rb'),
            headers={'content-type': 'image/jpeg'}
        )
        assert resp.status_code == 200
        resp = resp.json()
        assert resp['width'] == image.width
        assert resp['height'] == image.height
        assert resp['format'] == 'JPEG'
