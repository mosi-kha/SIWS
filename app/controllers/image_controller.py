import falcon
from PIL import Image
import mimetypes

ALLOWED_IMAGE_TYPES = {falcon.MEDIA_JPEG, falcon.MEDIA_GIF, falcon.MEDIA_PNG, 'image/jpg'}


class ImageController:
    _CHUNK_SIZE_BYTES = 4096

    def validate_image_type(self, req, resp, resource, *params):
        if req.content_type not in ALLOWED_IMAGE_TYPES:
            msg = 'Image type not allowed. Must be PNG, JPEG, JPG, or GIF'
            raise falcon.HTTPBadRequest('Bad request', msg)

    def get_image_size(self, image_stream, content_type):
        ext = mimetypes.guess_extension(content_type)
        with open(f'image{ext}', 'wb') as file:
            while True:
                chunk = image_stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break

                file.write(chunk)

        image = Image.open(f'image{ext}')

        return {
            "format": image.format,
            "height": image.height,
            "width": image.width,
            "mode": image.mode,
            "doc": "pixel"
        }
