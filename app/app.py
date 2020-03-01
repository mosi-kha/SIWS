import falcon
from app.resources.image_resource import ImageResource

api = application = falcon.API()

api.add_route('/', ImageResource())
