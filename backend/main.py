from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import character
from database import client

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost:8002",
    "http://172.0.0.1:8002"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(character.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Убедитесь, что MongoDB подключена
@app.on_event("startup")
def startup_db_client():
    try:
        client.admin.command('ping')
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

@app.on_event("shutdown")
def shutdown_db_client():
    client.close()
