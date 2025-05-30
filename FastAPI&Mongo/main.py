# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.crud_routes import router as crud_router
from routes.petNames_routes import router as petNames_router
from datab.conexion_db import connect_to_mongo, close_mongo_connection

load_dotenv() 

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "https://mongoproyectos-production.up.railway.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()
    

app.include_router(crud_router, tags=["items"])
app.include_router(petNames_router, tags=["pets"])

