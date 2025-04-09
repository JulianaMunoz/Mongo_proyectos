from fastapi import APIRouter, HTTPException
from models.pet_model import PetRequest
import random

router = APIRouter()

nombres_por_tipo = {
    "perro": {
        "jugueton": ["Pelusa", "Saltín", "Toby", "Max"],
        "tranquilo": ["Don Siesta", "Coco", "Luna", "Rocky"],
        "valiente": ["Thor", "Rex", "Bruno", "Kira"]
    },
    "gato": {
        "jugueton": ["Mishi", "Zoom", "Pelusín", "Nube"],
        "tranquilo": ["Don Ronroneo", "Chispa", "Sombra", "Mora"],
        "valiente": ["Garfield", "Zelda", "Pantera", "Tigre"]
    },
    "conejo": {
        "jugueton": ["Brinco", "Pompon", "Pelusa", "Saltarín"],
        "tranquilo": ["Nube", "Dumbo", "Luna", "Daisy"],
        "valiente": ["Trueno", "Furia", "Blitz", "Sonic"]
    }
}

@router.post("/pets/")
def generar_nombre(req: PetRequest):
    nombre = random.choice(nombres_por_tipo[req.tipo][req.personalidad])
    return {
        "nombre_sugerido": nombre,
        "tipo": req.tipo,
        "personalidad": req.personalidad
    }
