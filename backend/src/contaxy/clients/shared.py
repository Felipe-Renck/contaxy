from fastapi import HTTPException, status
from requests.models import Response

from contaxy.schema import UnauthenticatedError
from contaxy.schema.exceptions import (
    ClientValueError,
    PermissionDeniedError,
    ProblemDetails,
    ResourceAlreadyExistsError,
    ResourceNotFoundError,
)


def handle_errors(response: Response) -> None:
    if response.status_code < 400 or response.status_code >= 600:
        return

    message = None
    try:
        error = ProblemDetails.parse_raw(response.text)
        message = error.message
    except Exception:
        try:
            # Use full body
            message = response.text
        except Exception:
            pass

    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        raise UnauthenticatedError(message)

    if response.status_code == status.HTTP_403_FORBIDDEN:
        raise PermissionDeniedError(message)

    if response.status_code == status.HTTP_404_NOT_FOUND:
        raise ResourceNotFoundError(message)

    if response.status_code == status.HTTP_409_CONFLICT:
        raise ResourceAlreadyExistsError(message)

    # TODO: already used
    # if response.status_code == status.HTTP_409_CONFLICT:
    #    raise ResourceUpdateFailedError(message)

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        raise ClientValueError(message)

    # If different error, raise generic http exception
    # This should not happen
    raise HTTPException(status_code=response.status_code, detail=response.text)
