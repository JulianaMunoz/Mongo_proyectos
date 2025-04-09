from fastapi import APIRouter, HTTPException, Query
from typing import Literal
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

@router.get("/nombre-mascota")
def generar_nombre(
    tipo: Literal["perro", "gato", "conejo"] = Query(..., description="Tipo de mascota"),
    personalidad: Literal["jugueton", "tranquilo", "valiente"] = Query(..., description="Personalidad")
):
    nombre = random.choice(nombres_por_tipo[tipo][personalidad])
    return {
        "nombre_sugerido": nombre,
        "tipo": tipo,
        "personalidad": personalidad
    }
