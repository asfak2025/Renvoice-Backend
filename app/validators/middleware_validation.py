from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.exceptions import RequestValidationError

class ValidationErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except RequestValidationError as exc:
            # Format the 422 error response
            errors = []
            for error in exc.errors():
                errors.append({
                    "field": ".".join(str(loc) for loc in error["loc"]),
                    "message": error.get("msg"),
                    "type": error.get("type")
                })
            
            return JSONResponse(
                status_code=422,
                content={
                    "status": "error",
                    "message": "Validation failed",
                    "errors": errors,
                    "code": 422
                }
            )