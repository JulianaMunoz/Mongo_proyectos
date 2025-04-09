from pydantic import BaseModel

class PetRequest(BaseModel):
    tipo: Literal["perro", "gato", "conejo"]
    personalidad: Literal["jugueton", "tranquilo", "valiente"]