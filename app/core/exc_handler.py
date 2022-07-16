from fastapi.responses import JSONResponse

from .exception import AppException
from .server import app


@app.exception_handler(AppException)
async def resolve_app_exception(exc: AppException):
    return JSONResponse(content={"error": exc.msg}, status_code=exc.status_code)


@app.exception_handler(Exception)
async def resolve_server_error(exc: Exception):
    return JSONResponse(content={"error": "Server Error."}, status_code=500)
