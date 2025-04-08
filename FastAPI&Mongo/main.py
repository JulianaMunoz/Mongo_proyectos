# main.py
from fastapi import FastAPI
from routes.crud_routes import router as crud_router
from db.conexion_db import connect_to_mongo, close_mongo_connection
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()  # Carga las variables de entorno

origins = [
    "http://localhost:5500",  # Ajusta la URL de tu app web
    "http://127.0.0.1:5500",
    # Agrega otros orígenes que necesites
]


app = FastAPI(title="API de Sitios Turísticos en Bogotá")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Permite estos orígenes
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

# Incluye las rutas con sus respectivos prefijos y tags
app.include_router(crud_router, prefix="/crud", tags=["items"])
