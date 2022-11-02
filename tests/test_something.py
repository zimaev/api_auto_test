import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from jsonschema import validate
from src.schemas.posts import POST_SCHEMA
from src.base_classes.response import Response


def test_get_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(400)
    response.validate(POST_SCHEMA)



