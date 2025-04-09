from pydantic import BaseModel
from typing import Literal

class PetRequest(BaseModel):
    tipo: Literal["perro", "gato", "conejo"]
    personalidad: Literal["jugueton", "tranquilo", "valiente", "Tragon"]