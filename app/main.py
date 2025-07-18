from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordBearer
from app.routes import district_route

from app.routes import organization_route

from app.validators.middleware_validation import ValidationErrorMiddleware

app = FastAPI(title='TVK API')

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(ValidationErrorMiddleware)

app.include_router(organization_route.router, prefix="/api/org", tags=["Organization"])
app.include_router(district_route.router, prefix="/api/district", tags=["Districts"])

@app.on_event('startup')
async def startUp():
    print("server Started")
