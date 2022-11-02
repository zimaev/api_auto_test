import requests
from configuration import SERVICE_URL
from src.schemas.posts import POST_SCHEMA
from src.base_classes.response import Response
from src.pydantic_schemas.posts import Post


def test_get_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200)
    response.validate(Post)



