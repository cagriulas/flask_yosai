from yosai.web import (
    web_abcs
)

from werkzeug.exceptions import (
    Unauthorized,
    Forbidden,
)

class FlaskWebRegistry(web_abcs.WebRegistry):
