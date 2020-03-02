from io import BytesIO

import falcon
from PIL import Image


class ImageController:
    _CHUNK_SIZE_BYTES = 4096
    _ALLOWED_IMAGE_TYPES = {
        falcon.MEDIA_JPEG,
        falcon.MEDIA_GIF,
        falcon.MEDIA_PNG,
        "image/jpg",
    }

    def validate_image_type(self, req, resp, resource, *params):
        if req.content_type not in self._ALLOWED_IMAGE_TYPES:
            msg = "Image type not allowed. Must be PNG, JPEG, JPG, or GIF"
            raise falcon.HTTPBadRequest("Bad request", msg)

    def get_image_size(self, image_stream):
        image_bytes = []
        while True:
            chunk = image_stream.read(self._CHUNK_SIZE_BYTES)
            if not chunk:
                break
            image_bytes.append(chunk)

        image = Image.open(BytesIO(b"".join(image_bytes)))
        return {
            "format": image.format,
            "height": image.height,
            "width": image.width,
            "mode": image.mode,
            "doc": "pixel",
        }
