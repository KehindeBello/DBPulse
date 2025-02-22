from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routes.monitor import router as monitor_router
from routes.telex import router as telex_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter()
api_router.include_router(monitor_router, prefix="/api", tags=["Monitor"])
api_router.include_router(telex_router, prefix="/api", tags=["Telex"])
app.include_router(api_router)

@app.get("/")
def index():
    return {"message": "Hello World"}





