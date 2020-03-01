import falcon
from falcon import Request, Response

from app.controllers.image_controller import ImageController


class ImageResource:
    def on_get(self, req: Request, resp: Response, *args, **kwargs):
        resp.status = falcon.HTTP_200
        resp.body = "use POST method to send Image, Allowed Format: png, jpg, jpeg, gif"

    @falcon.before(ImageController().validate_image_type)
    def on_post(self, req: Request, resp: Response, *args, **kwargs):
        try:
            response = ImageController().get_image_size(req.stream)
            resp.media = response
            resp.status = falcon.HTTP_200
        except Exception as ex:
            raise falcon.HTTPBadRequest('bad request', ex.__str__())
