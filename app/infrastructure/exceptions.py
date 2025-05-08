from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_404_NOT_FOUND


class NotFoundError(HTTPException):
    """Not found error."""
    status_code = HTTP_404_NOT_FOUND 